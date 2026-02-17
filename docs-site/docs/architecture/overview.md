# Architecture Overview

CIRI is a local-first, multi-agent orchestration system built on **LangChain/LangGraph**. It is designed to be highly extensible via pluggable components.

## Core Module Map

- `src/__main__.py`: CLI entrypoint, UI rendering (Rich), and input handling (Prompt Toolkit).
- `src/copilot.py`: The brain. Orchestrates the main agent graph and combines middlewares.
- `src/backend.py`: Interface for tool execution and real-time output streaming.
- `src/controller.py`: Logic for slash commands and thread management.
- `src/serializers.py`: Serialization logic for checkpoints and state persistence.

## Key Middlewares

CIRI uses a sophisticated middleware stack to inject context and manage state:

- **MemoryMiddleware**: Auto-loads long-term workspace context from `.ciri/memory/`.
- **SkillsMiddleware**: Dynamically injects learned capabilities into the agent's toolset.
- **SubAgentMiddleware**: Manages delegation to specialized agents (`web_researcher`, `skill_builder`, etc.).
- **ToolkitInjectionMiddleware**: Hot-swaps MCP toolkits based on the task requirements.
- **FilesystemMiddleware**: Provides scoped and safe access to the user's workspace.

## Data Persistence

- **CIRI Managed Data**: Located in `~/.ciri/` (Global) and `.ciri/` (Workspace-local).
- **SQLite Database**: Stores conversation threads, message history, and LangGraph checkpoints.
- **Checkpoints**: Enable "resume-where-you-left-off" capability even after restarts.

## Design Goals

1. **Autonomy**: High agency to plan and execute multi-step tasks.
2. **Self-Evolution**: Ability to learn new tools and patterns over time.
3. **Workspace-Aware**: Deep integration with local files, history, and domain context.
4. **Safety**: Mandatory Human-in-the-Loop for critical actions.
