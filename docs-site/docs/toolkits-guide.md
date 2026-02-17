# Toolkits Guide (MCP)

Toolkits in CIRI are built on the **Model Context Protocol (MCP)**. This allows Ciri to connect to any standard MCP server (like those for Google Drive, Slack, or Database connections).

## Architecture

CIRI's `ToolkitInjectionMiddleware` acts as an MCP client. It dynamically connects to servers defined in your configuration or in `.ciri/toolkits/`.

## Adding a Toolkit

### Using the Toolkit Builder
Ask Ciri: "Build a toolkit to connect to my local PostgreSQL database at localhost:5432".
Ciri will:
1. Initialize an MCP server implementation.
2. Store configuration in `.ciri/toolkits/<name>`.
3. Test the connection.

### Manual Addition
You can add third-party MCP servers by adding them to your global configuration in `~/.ciri/settings.json`.

## Toolkit Security
- **Isolation**: Toolkits run in separate processes.
- **Secrets**: Use environment variables (via `.env`) for credentials. Ciri will never hardcode keys into the toolkit code.
