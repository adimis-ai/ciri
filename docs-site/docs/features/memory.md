# Persistent Workspace Memory

CIRI maintains a long-term understanding of your workspace through a simple but effective markdown-based memory system located in `.ciri/memory/`.

## Why Memory Matters

Standard LLM contexts are volatile and limited. CIRI's `MemoryMiddleware` ensures that critical architectural decisions, project conventions, and past "lessons learned" are present in Every. Single. Turn.

## How it works

1. **Automatic Loading**: On every turn, the `MemoryMiddleware` scans `.ciri/memory/` and injects the content of all `.md` files into the system prompt.
2. **Context Indexing**: The `AGENT.md` file (if present) acts as a primary index for your workspace.
3. **Active Updates**: Ciri is instructed to update these files after completing significant tasks (e.g., "Updated memory with the new API endpoint structure").

## Best Practices

- **Keep it Concise**: Focus on actionable facts, not logs.
- **Project DNA**: Document the "flavor" of the project (e.g., "We prefer functional components over classes").
- **External Docs**: If you have huge external documentation, don't copy it. Point Ciri to it and store a high-level summary in memory.
