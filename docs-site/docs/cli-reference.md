# CLI Reference

CIRI provides a powerful interactive interface with specialized slash commands and autocomplete triggers.

## Interaction Basics

- **Normal Text**: Sent directly to Ciri's core orchestration graph.
- **Slash Commands**: Specialized administrative or configuration tasks.
- **Autocomplete Triggers**: Keywords starting with `@` that trigger filesystem or capability suggestions.

## Slash Commands

| Command | Description |
| :--- | :--- |
| `/new-thread` | Starts a fresh conversation thread with a clean state. |
| `/switch-thread` | Interactively select and switch to a previous thread. |
| `/delete-thread` | Remove a thread and its checkpointed state. |
| `/threads` | List all historical conversation threads. |
| `/change-model` | Change the active LLM (e.g., switch from GPT-4 to Claude 3.5). |
| `/change-browser-profile` | Select a different browser profile for web research. |
| `/sync` | **Critical**: Analyzes your workspace and "self-trains" Ciri by detecting local skills and toolkits. |
| `/help` | Displays the help menu and keyboard shortcuts. |
| `/exit` | Gracefully closes the session. |

## Autocomplete Triggers

Type these at the prompt to trigger interactive selection:

- `@files:<path>`: Search and select files from the workspace.
- `@folders:<path>`: Search and select directories.
- `@skills:<name>`: Map specific skill capabilities to your prompt.
- `@toolkits:<name>`: Reference installed MCP toolkits.
- `@subagents:<name>`: Delegate tasks to specific subagent roles.

## Human-in-the-Loop (HITL)

By default, Ciri requires explicit approval for destructive or external actions:
- `execute`: Running shell scripts or terminal commands.
- `edit_file`: Modifying existing source code.
- `write_file`: Creating new files.

You can **Approve**, **Edit** (modify the proposed arguments), or **Reject** any action request.

## Keyboard Shortcuts

- `Alt+Enter`: Insert a new line (multi-line input).
- `Ctrl+C`: Stop a streaming response.
- `Ctrl+C (twice)`: Exit CIRI.
- `Up/Down Arrow`: Navigate command history.

