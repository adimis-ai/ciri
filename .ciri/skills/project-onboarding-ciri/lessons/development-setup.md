# Development Setup

1) Prerequisites

- Python 3.12+
- Git
- uv (https://docs.astral.sh/uv/) — used for managing the virtual environment and installs

2) Create and sync virtual environment (Linux / macOS)

```bash
# From repo root
uv sync --dev
# Activate (uv creates and manages venv; use `uv shell` if installed)
# Install editable package
uv pip install -e .
# Verify
ciri --help
```

Windows (PowerShell)

```powershell
uv sync --dev
uv pip install -e .
ciri --help
```

Notes

- Alternative global install: `uv tool install .` — this installs the `ciri` CLI globally for the current user (~/.local/bin).
- To set environment variables temporarily:
  - macOS/Linux: `export OPENROUTER_API_KEY="your-key"`
  - Windows PowerShell: `$env:OPENROUTER_API_KEY="your-key"`
- You can persist the API key using the CLI (first run prompts) or by creating a `.env` file in the repo root: `echo 'OPENROUTER_API_KEY=your-key' > .env`.
