# Agent Workflows

[![Validate](https://github.com/bglglzd/agent-workflows/actions/workflows/validate.yml/badge.svg)](https://github.com/bglglzd/agent-workflows/actions/workflows/validate.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-22c55e.svg)](LICENSE)
[![Markdown-first](https://img.shields.io/badge/format-Markdown--first-0ea5e9.svg)](prompts)
[![GitHub stars](https://img.shields.io/github/stars/bglglzd/agent-workflows?style=flat)](https://github.com/bglglzd/agent-workflows/stargazers)

**Portable, safety-aware workflows for AI coding agents.** Capture a session before context disappears, audit a project without guessing, and turn a vague idea into a buildable plan.

> Copy a prompt into any AI agent, install the bundled Codex plugin, or reuse a standalone skill in Claude Code.

## The workflows

| Workflow | Use it when | It produces |
| --- | --- | --- |
| [Session Handoff](prompts/session-handoff.md) | You are ending a coding session | Durable project memory, decisions, validation results, and exact next steps |
| [Deep Project Audit](prompts/project-audit.md) | You need to understand an unfamiliar or risky codebase | Architecture map, operational picture, prioritized findings, and a remediation plan |
| [Idea Discovery Interview](prompts/idea-discovery-interview.md) | You have only a rough product or feature idea | A recorded discovery brief and an evidence-based implementation plan |

```text
Capture context  →  Understand the system  →  Build the right thing
```

## Fastest start

```bash
git clone https://github.com/bglglzd/agent-workflows.git
```

Open a file in [`prompts/`](prompts), paste its **Prompt** section into your agent, and give it the current project directory. The prompts are plain Markdown by design: they work in chat, terminals, IDE agents, and project instructions.

## Install in Codex

This repository ships an installable Codex plugin containing all three skills at [`plugins/agent-workflows`](plugins/agent-workflows). Add its marketplace, then install the plugin:

```powershell
codex plugin marketplace add bglglzd/agent-workflows --ref main
codex plugin add agent-workflows@agent-workflows
```

Start a new session, then invoke a workflow explicitly, for example: `Use $session-handoff to preserve this project's context.` Codex can also select a workflow implicitly when its description matches your task.

For a project-local skill without installing the plugin, copy an individual folder into `.agents/skills/`:

```powershell
New-Item -ItemType Directory -Force .\.agents\skills | Out-Null
Copy-Item .\plugins\agent-workflows\skills\project-audit .\.agents\skills\project-audit -Recurse
```

### Claude Code

Copy a skill folder into the project-local `.claude/skills/` directory. Keeping it in the repository makes the workflow available to collaborators too.

```powershell
New-Item -ItemType Directory -Force .\.claude\skills | Out-Null
Copy-Item .\plugins\agent-workflows\skills\project-audit .\.claude\skills\project-audit -Recurse
```

### Any other agent

Use the canonical Markdown files from [`prompts/`](prompts). Tools such as OpenCode or OpenClaw may use different command and instruction-file conventions; paste the relevant prompt into that tool's project instruction or custom command. This repository deliberately does not claim automatic installation where a tool has no compatible skill format.

## Design principles

- **Evidence before conclusions.** Prompts ask for file paths, commands, validation output, and explicit unknowns.
- **Safe by default.** Audits are read-only and never connect to servers or expose secrets unless the user explicitly authorizes that scope.
- **Durable context.** Handoffs preserve decisions and the exact state needed by the next human or agent.
- **No fake certainty.** If a project, server, or requirement cannot be verified, the workflow says so.
- **Tool-neutral core.** Markdown is the source format; skill wrappers add convenience, not lock-in.

## Contributing

New workflows are welcome when they solve a recurring engineering problem and include clear scope, safety boundaries, concrete outputs, and verification guidance. Read [CONTRIBUTING.md](CONTRIBUTING.md) before opening a pull request.

## Roadmap

- Debugging and incident-response workflow
- Release-readiness workflow
- Migration and modernization workflow
- Community-tested examples for popular AI coding agents

## License

MIT — see [LICENSE](LICENSE).
