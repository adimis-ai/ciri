Workspace Overview

- Name: CIRI Copilot (ciri-copilot)
- Purpose: Local desktop-class CLI AI copilot for interactive chat, thread-based conversations, and extensible skills/toolkits.

Structure

- src/ — Main Python package (entrypoint: src/__main__.py)
- src/skills/, src/toolkit/, src/subagents/ — built-in extensions
- .ciri/skills/ — local skills (added by contributors)
- pyproject.toml — packaging (hatchling), dependencies, console script `ciri`
- build.py — PyInstaller build script to create a standalone binary
- tests/ — pytest test suite

Key Patterns & Commands

- Dev environment: uv sync --dev; uv pip install -e .
- Run CLI: ciri or python -m src.__main__
- Add skills: place SKILL.md under .ciri/skills/<name>/ (YAML frontmatter: name, description)
- /sync inside the CLI scans the repo and .ciri/ and updates in-memory skills/toolkits

Common Tasks

- Run tests: pytest
- Lint & format: ruff check src/ --fix; black src/; mypy src/
- Build wheel: python -m build --wheel or hatch build -t wheel
- Build standalone binary: python build.py --target <triple>

Links

- Onboarding skill: .ciri/skills/project-onboarding-ciri/SKILL.md
