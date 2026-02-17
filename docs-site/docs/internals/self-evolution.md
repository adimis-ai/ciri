# Self-Evolution & Training

CIRI is designed to be a self-improving system. Through the **Trainer Agent** and the `/sync` command, Ciri analyzes its environment and its own limitations to permanently expand its capabilities.

## The Trainer Agent Loop

The `trainer_agent` orchestrates several specialized builder subagents:

1. **Skill Builder**: Creates reusable Python packages in `.ciri/skills/`.
2. **Toolkit Builder**: Generates new MCP (Model Context Protocol) servers for API integrations in `.ciri/toolkits/`.
3. **SubAgent Builder**: Defines new specialized agent roles in `.ciri/subagents/`.

## How it Works

When you run `/sync` or when Ciri identifies a gap in its tools:

1. **Analysis**: Ciri scans the workspace, existing skills, and recent interaction history.
2. **Strategy**: It decides whether it needs a new primitive tool (Skill), a complex integration (Toolkit), or a specialized role (SubAgent).
3. **Execution**: The relevant builder agent is invoked to write, test, and package the new capability.
4. **Hot-Reloading**: The `SkillsMiddleware` and `ToolkitInjectionMiddleware` immediately detect and load the new capability without needing a restart.

## Writing Your Own Builders

Advanced users can customize the builder prompts in `src/subagents/` to change how Ciri implements new skills. This allows you to enforce specific coding standards or library preferences across all self-generated code.
