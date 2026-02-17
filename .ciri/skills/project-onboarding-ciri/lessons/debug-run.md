# Debugging & Running Locally

Run the CLI

- After editable install or `uv tool install .`, run:

```bash
ciri
```

- Alternatively, run directly from source (no install):

```bash
python -m src.__main__
```

Common flags & commands

- `--help` for CLI help (typer-powered)
- Inside CIRI, use `/sync` to analyze the workspace and self-train (this reads `.ciri/` and workspace files and updates internal state)

Logs & troubleshooting

- CIRI reads a global .env at the app data dir (~/.local/share/ciri/.env on Linux). Use `load_all_dotenv()` behavior in src/utils.py.
- For debugging, set verbose logging via environment variables or adjust logging in src/__main__.py or src/copilot.py.
- If PLAYWRIGHT is used, ensure browsers are installed: `playwright install` (dev environment).

Notes

- To persist API keys for OpenRouter, the CLI prompts on first run and persists to the global .env in the app data dir. See `_persist_env_var()` in src/__main__.py.
