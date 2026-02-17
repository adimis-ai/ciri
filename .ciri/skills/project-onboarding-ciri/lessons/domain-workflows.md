# Domain-specific Workflows

Adding a model provider

- CIRI expects model access via an LLM gateway. By default it uses OpenRouter (`OPENROUTER_API_KEY`).
- To add another provider:
  1. Update env var handling or add a new gateway option respecting `LLM_GATEWAY_PROVIDER`.
  2. Implement or wire a provider adapter in `src/serializers.py` or `src/copilot.py` where LLM clients are created.
  3. Add docs and tests.

Adding a Toolkit or SubAgent

- Add toolkit code under `src/toolkit/` and local MCP servers under `.ciri/toolkits/<name>/`.
- Subagents: create modules under `src/subagents/` or YAML configs under `.ciri/subagents/` and follow existing patterns.
- Use `/sync` inside the running CLI to detect new toolkits/subagents and load them.

How /sync self-trains

- Trigger: run `ciri` and enter `/sync` or call `sync_default_skills()` from code.
- Behavior: `src/__main__.py` calls `sync_default_skills()` (see utils.sync_default_skills) which scans the workspace and `.ciri/` for skills, toolkits, and subagents, updates settings and any local storage needed.
- The `/sync` command is meant to analyze the workspace and add onboarding knowledge into the runtime, enabling CIRI to answer project-specific queries and use new skills/toolkits.
