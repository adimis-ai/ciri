# CIRI Copilot

CIRI (Ciri Intelligent Runtime & Interface) Copilot is a desktop-class personal AI copilot intended to be run locally. This repository contains the CIRI command-line interface (CLI) which provides tools for managing and interacting with the Ciri AI agent system: compiling agents, running and streaming conversations, viewing and managing conversation history, configuring local settings, and developer utilities for building and testing agents.

Table of contents
- Features
- Requirements
- Installation
- Quickstart
- Common commands
- Configuration
- Development
- Contributing
- License

Features
- Agent compilation and packaging: build and prepare agents for local execution.
- Conversation streaming: run agents and stream responses in real time to the terminal.
- Conversation history: save, list, search, export and replay past conversations.
- Configuration: manage local settings (models, storage paths, logging).
- Developer tooling: test, lint, and iterate on agents quickly.

Requirements
- Python 3.9+ (3.12 recommended)
- Git (for cloning the repo)
- Optional: a virtual environment tool (venv, pipenv, poetry)

Installation
1. Clone the repository
   git clone https://github.com/your-org/ciri-cli-v1.git
   cd ciri-cli-v1

2. Create and activate a virtual environment (recommended)
   python -m venv .venv
   source .venv/bin/activate  # macOS / Linux
   .venv\Scripts\activate     # Windows (PowerShell)

3. Install dependencies
   pip install -r requirements.txt
   # or editable install for development
   pip install -e .

Quickstart
1. Build or compile an agent (example)
   ciri compile path/to/agent_spec.yaml

2. Start an interactive session with an agent
   ciri run --agent my_agent

3. Stream a conversation from the agent
   ciri stream --agent my_agent --session "work session"

4. List conversation history
   ciri history list

Common commands (examples)
- ciri compile <spec>      Compile an agent from a specification file.
- ciri run --agent <name>  Run an agent interactively in the terminal.
- ciri stream [options]    Stream agent outputs (useful for long-form responses).
- ciri history [list|show|export|delete]
- ciri config [get|set|show]
- ciri dev test            Run unit/integration tests for local development.

(Notes) Command names and flags above are representative — see ciri --help for the exact flags and available subcommands in your installed version.

Configuration
CIRI stores local settings in a configuration file and supports environment variables for sensitive values (API keys, model tokens).
- Default config path: ~/.ciri/config.yaml
- Common settings:
  - default_agent: name to use when --agent is not provided
  - storage_path: where conversation history and artifacts are stored
  - model: default model/provider to use

Security & Secrets
- Do NOT commit API keys or secrets to the repository. Use environment variables or a local config file excluded from version control (e.g., add ~/.ciri/config.yaml to your .gitignore if it is in the repository).

Development
- Run tests
  pytest

- Lint
  ruff .
  black .

- Install dev dependencies
  pip install -r dev-requirements.txt

Project layout (high level)
- ciri/           CLI implementation and core runtime
- agents/         example agent specifications and templates
- docs/           additional documentation and guides
- tests/          unit and integration tests

Contributing
Contributions are welcome. Suggested workflow:
1. Fork the repository and create a topic branch.
2. Write tests for your change.
3. Run tests and linters.
4. Open a pull request describing the change.

When opening PRs, include:
- A clear description of what changed and why
- Any migration or compatibility notes
- How to test the change locally

Troubleshooting
- If you encounter permission issues when reading/writing to the storage path, ensure the configured storage directory exists and is writable by your user.
- If an agent fails to start, run with increased logging (e.g., --log-level debug) and check the agent spec for missing fields.

License
Specify your license here (e.g., MIT). Replace this line with the actual license header or a link to the LICENSE file.

Contact
For questions or support, open an issue in this repository or contact the maintainers listed in the project metadata.

Acknowledgements
This project is developed as a local personal AI copilot. Thank you to contributors and the open source ecosystem that makes this work possible.

