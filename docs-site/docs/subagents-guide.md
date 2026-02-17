# Subagents & Delegation

Subagents are specialized, semi-autonomous agents that handle complex, multi-step tasks that would overwhelm the main copilot graph.

## Built-in Subagents

CIRI comes with several highly trained roles:
- **web_researcher**: Specialist in browser automation and data extraction.
- **skill_builder**: Expert in writing and packaging Python skills.
- **trainer_agent**: Orchestrator for the self-evolution process.

## The Delegation Pattern

CIRI uses a **Router-Worker** pattern:
1. **Main Copilot** receives the request.
2. **SubAgentMiddleware** detects if the task fits a specialized subagent's description.
3. **Hand-off**: The state is transferred to the subagent.
4. **Fulfillment**: The subagent works (possibly taking many steps) and returns a structured result to the main agent.

## Creating Specialized Subagents

You can define custom subagents in `.ciri/subagents/`. Each subagent needs:
- A clear **Name** and **Description** (used by the router to decide when to delegate).
- A **System Prompt** defining its persona and expertise.
- A **Model Config** (optional, subagents can use cheaper/faster models).

To register a new subagent, run `/sync`.
