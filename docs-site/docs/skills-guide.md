# Skills Guide

Skills are the fundamental building blocks of CIRI's capability set. A skill is a standalone Python package that exposes specific tools to Ciri.

## Skill Structure

A well-formed skill lives in `.ciri/skills/<skill-name>/` and contains:

1. **`skill.json`**: Metadata defining the skill.
   ```json
   {
     "name": "git-helper",
     "version": "1.0.0",
     "description": "Advanced git operations and commit labeling"
   }
   ```
2. **`module.py`**: The implementation.
   ```python
   from langchain_core.tools import tool

   @tool
   def generate_commit_msg(diff: str) -> str:
       """Generates a conventional commit message based on a git diff."""
       # Implementation logic here
       return "feat: update documentation"
   ```
3. **`README.md`**: Documentation for the human user.

## Creation Workflow

1. **Manual**: Create the folder and files manually under `.ciri/skills/`.
2. **Autonomous**: Ask Ciri "Create a skill to search my Jira tickets"—it will invoke the `skill_builder_agent` to do it for you.
3. **Activation**: Run `/sync` in the CLI to hot-reload the new skill.

## Advanced: Skill Dependencies
If your skill requires external libraries, Ciri will attempt to install them via `uv` during the self-training phase. You can specify these in a `requirements.txt` inside the skill folder.
