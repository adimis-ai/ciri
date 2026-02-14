import os
import yaml
import json
from pydantic import BaseModel, Field
from langchain.agents.middleware import InterruptOnConfig
from typing import List, Optional, Dict, Any, Literal, Union
from deepagents.middleware import SubAgentMiddleware as BaseSubAgentMiddleware, SubAgent as DeepAgentSubAgent

# TODO: Extend SubAgent Middleware: Auto scan & inject subagents from **`<root_dir>/.ciri/subagents`** and also recursively scan all nested .ciri folders in root_dir other folders
# In subagents folder the subagents file will be in yaml or json format and will have the following structure: <subagent_name>.yaml or <subagent_name>.json
# The structure of the subagent file should be validated against the SubAgent model defined below. and the extracted subagents will be added to the subagents list in the SubAgentMiddleware initialization. This will allow users to easily define and manage their subagents without having to manually add them to the code. The middleware will automatically discover and load all subagents defined in the specified directory, making it more flexible and user-friendly, ensure to throw error if a tool is defined for the subagent but not found in the available tools list, also ensure to throw error if the subagent file is not in the correct format or if the required fields are missing. This will help users to quickly identify and fix any issues with their subagent definitions.

class SubAgent(BaseModel):
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
    interrupt_on: Optional[dict[str, bool | InterruptOnConfig]] = Field(
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
    ):
        super().__init__(
            default_model=default_model,
            default_tools=default_tools,
            default_middleware=default_middleware,
            default_interrupt_on=default_interrupt_on,
            subagents=subagents,
            system_prompt=system_prompt,
            general_purpose_agent=general_purpose_agent,
            task_description=task_description,
        )
        self.all_available_tools = set()

    def wrap_model_call(self, request, handler):
        available_tools = set()
        for tool in request.tools:
            available_tools.add(tool.name)
        self.all_available_tools.update(available_tools)
        return super().wrap_model_call(request, handler)
