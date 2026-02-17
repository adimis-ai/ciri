# Skills & Toolkits

Where to add skills

- Repo supports skills under `src/skills/` for built-in skills, and `.ciri/skills/` for local user skills.
- Each skill is a directory with a required `SKILL.md` that contains YAML frontmatter (name, description) and concise instructions.

Create a skill (example)

```bash
# Create folder
mkdir -p .ciri/skills/my-skill
# Add SKILL.md with YAML frontmatter
cat > .ciri/skills/my-skill/SKILL.md <<'EOF'
---
name: my-skill
description: Short description
---
# My Skill

One-page instructions.
EOF
```

Registering & testing

- CIRI loads skills by scanning the filesystem (see `list_skills()` in src/utils.py).
- No explicit registry required; place your skill under `.ciri/skills/` or `src/skills/` and run `ciri` or use `/sync` to let the CLI detect new skills.

Toolkits

- Toolkit adapters live under `src/toolkit/` and external MCP toolkits are expected under `.ciri/toolkits/` if present.
- To add an MCP toolkit, follow existing patterns in `src/toolkit/` and place a toolkit server under `.ciri/toolkits/<name>/` (see other repository examples).

Subagents

- Subagents are plugin-like roles under `src/subagents/` and `.ciri/subagents/` for local ones.
- Add YAML configs or Python modules following existing examples in `src/subagents/`.

Testing skills/toolkits

- Run `ciri` and use `@skills:` completion or `/sync` to detect. For toolkit servers, start the toolkit MCP server and configure the toolkit path in CIRI settings if required.
