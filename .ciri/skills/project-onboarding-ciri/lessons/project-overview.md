# Project Overview

What it is

- Project: CIRI Copilot (ciri-copilot)
- Purpose: Local CLI AI copilot for interactive chat, thread-based conversations, file- and skill-aware autocompletion, and extensible skills/toolkits.
- Entry point: src/__main__.py (console script `ciri` configured in pyproject.toml)

Key files & directories

- src/ — Primary Python package code. Key modules:
  - src/__main__.py — CLI entrypoint and /sync handling
  - src/copilot.py — Copilot creation and runtime
  - src/controller.py — Controller logic
  - src/utils.py — Utility helpers: load_all_dotenv(), list_skills(), get_app_data_dir(), sync_default_skills()
  - src/skills/ — Built-in skill packages loaded by the app
  - src/toolkit/ — Toolkit adapters and MCP integration
  - src/subagents/ — Built-in subagent definitions
- pyproject.toml — Packaging, dependencies, hatchling build backend, console script `ciri`
- build.py — PyInstaller helper to produce standalone binaries (dist/, build/)
- .env — repository `.env` (ignored) for local secrets
- README.md, CONTRIBUTING.md — Developer docs and contributing workflow
- tests/ — pytest test suite

Architecture notes

- Pure Python CLI package, packaged with hatchling (wheel target) and optional PyInstaller standalone binary via build.py.
- Uses uv (astral.sh/uv) as the recommended developer workflow and package manager for syncing virtualenv and installing in editable mode.
- Model access via OpenRouter by default (OPENROUTER_API_KEY environment variable).

Monorepo? No — single package under src/ (not multi-package).
