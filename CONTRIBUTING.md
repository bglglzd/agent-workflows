# Contributing

Thanks for improving Agent Workflows.

## What belongs here

Add a workflow only when it solves a recurring engineering task and gives an agent enough structure to act safely. A good workflow has:

- a precise trigger and outcome;
- explicit scope and safety boundaries;
- steps that work across stacks where possible;
- a concrete output format;
- guidance for uncertainty, validation, and secrets.

Avoid generic role prompts, vendor marketing, and instructions that invent facts or bypass user approval.

## Pull requests

1. Start from `main` and keep the change focused.
2. Add the canonical prompt under `prompts/`.
3. Add or update a matching standalone skill under `plugins/agent-workflows/skills/` when the workflow suits skill-based agents.
4. Update the workflow table in `README.md`.
5. Run `python scripts/validate_skills.py`.

Use clear English. Prompt text should be imperative, concise, and safe by default.

## Reporting issues

Use the issue templates. Never paste credentials, private URLs, customer data, or other sensitive information into a public issue.
