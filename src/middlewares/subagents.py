import os
import yaml
import json
import logging
from pathlib import Path
from pydantic import BaseModel, Field, ValidationError, ConfigDict
from langchain.agents.middleware import InterruptOnConfig
from typing import List, Optional, Dict, Any, Literal, Union
from deepagents.middleware import (
    SubAgentMiddleware as BaseSubAgentMiddleware,
    SubAgent as DeepAgentSubAgent,
)
from ..utils import get_default_filesystem_root

logger = logging.getLogger(__name__)


class SubAgent(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    name: str = Field(..., description="Unique name for the sub-agent")
    description: str = Field(
        ..., description="Brief description of the sub-agent's purpose"
    )
    system_prompt: str = Field(
        ..., description="System prompt to guide the sub-agent's behavior"
    )
    model: Optional[str] = Field(
        None, description="Model to use for this sub-agent (overrides default)"
    )
    interrupt_on: Optional[dict[str, Any]] = Field(
        None, description="Configuration for interrupting the sub-agent's execution"
    )
    tools: Optional[Union[List[str], Literal["all"]]] = Field(
        None,
        description="List of tool names the sub-agent can use, or 'all' to allow all tools",
    )


class SubAgentMiddleware(BaseSubAgentMiddleware):
    def __init__(
        self,
        *,
        default_model,
        default_tools=None,
        default_middleware=None,
        default_interrupt_on=None,
        subagents=None,
        system_prompt=...,
        general_purpose_agent=True,
        task_description=None,
        scan_root: Optional[Union[str, Path]] = None,
    ):
        if subagents is None:
            subagents = []
        else:
            # Ensure subagents is a list if it was a single item or None
            if not isinstance(subagents, list):
                subagents = [subagents]

        # 1. Determine scan root
        root = Path(scan_root) if scan_root else get_default_filesystem_root()
        logger.debug(f"Scanning for subagents in: {root}")

        # 2. Discover subagent files
        subagent_files = self._discover_subagent_files(root)

        # 3. Load and validate subagents
        discovered_subagents = []
        available_tool_names = set()
        if default_tools:
            available_tool_names = {t.name for t in default_tools}

        for file_path in subagent_files:
            try:
                subagent_data = self._load_subagent_file(file_path)
                # Validate against SubAgent model
                sub_agent_config = SubAgent(**subagent_data)

                # Check if tools are available
                if sub_agent_config.tools and sub_agent_config.tools != "all":
                    for tool_name in sub_agent_config.tools:
                        if tool_name not in available_tool_names:
                            raise ValueError(
                                f"Tool '{tool_name}' defined for subagent '{sub_agent_config.name}' "
                                f"in {file_path} but not found in available tools list."
                            )

                discovered_subagents.append(
                    DeepAgentSubAgent(
                        name=sub_agent_config.name,
                        description=sub_agent_config.description,
                        system_prompt=sub_agent_config.system_prompt,
                        model=sub_agent_config.model,
                        interrupt_on=sub_agent_config.interrupt_on,
                        tools=sub_agent_config.tools,
                    )
                )
                logger.info(
                    f"Loaded subagent '{sub_agent_config.name}' from {file_path}"
                )
            except (
                ValidationError,
                ValueError,
                json.JSONDecodeError,
                yaml.YAMLError,
            ) as e:
                logger.error(f"Failed to load subagent from {file_path}: {e}")
                raise  # Re-raise to alert user of misconfiguration

        # 4. Merge subagents: Explicitly passed first, then discovered
        final_subagents = list(subagents)
        seen_names = set()
        for s in subagents:
            if isinstance(s, dict):
                seen_names.add(s["name"])
            else:
                seen_names.add(s.name)

        for ds in discovered_subagents:
            if ds["name"] not in seen_names:
                final_subagents.append(ds)
                seen_names.add(ds["name"])
            else:
                logger.warning(
                    f"Subagent '{ds['name']}' (discovered) skipped as it's already defined."
                )

        self._subagents_input = final_subagents
        super().__init__(
            default_model=default_model,
            default_tools=default_tools,
            default_middleware=default_middleware,
            default_interrupt_on=default_interrupt_on,
            subagents=final_subagents,
            system_prompt=system_prompt,
            general_purpose_agent=general_purpose_agent,
            task_description=task_description,
        )
        self.all_available_tools = set()

    def _discover_subagent_files(self, root: Path) -> List[Path]:
        """Recursively find all .ciri/subagents/*.{yaml,yml,json} files."""
        discovered = []
        try:
            for ciri_dir in root.rglob(".ciri"):
                if ciri_dir.is_dir():
                    subagents_dir = ciri_dir / "subagents"
                    if subagents_dir.is_dir():
                        for ext in ["*.yaml", "*.yml", "*.json"]:
                            discovered.extend(list(subagents_dir.glob(ext)))
        except Exception as e:
            logger.error(f"Error while scanning for subagent files: {e}")
        return discovered

    def _load_subagent_file(self, path: Path) -> Dict[str, Any]:
        """Load subagent configuration from a YAML or JSON file."""
        with open(path, "r", encoding="utf-8") as f:
            if path.suffix in [".yaml", ".yml"]:
                return yaml.safe_load(f)
            elif path.suffix == ".json":
                return json.load(f)
            else:
                raise ValueError(f"Unsupported file extension: {path.suffix}")

    def wrap_model_call(self, request, handler):
        available_tools = set()
        for tool in request.tools:
            available_tools.add(tool.name)
        self.all_available_tools.update(available_tools)
        return super().wrap_model_call(request, handler)
