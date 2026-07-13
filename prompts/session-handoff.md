# Session Handoff

Use this at the end of a coding or research session to leave the next human or AI agent with trustworthy, project-local context.

## Prompt

You are closing this work session. Preserve durable context for the next agent without inventing facts or leaking secrets.

### Operating rules

1. Inspect the current workspace before writing. Prefer the repository's existing documentation, handoff, and naming conventions.
2. Do not modify application code, deployment configuration, or external systems as part of this handoff.
3. Never copy secrets into documentation: redact tokens, passwords, private URLs, connection strings, customer data, and `.env` values. State only that a secret or configuration is required when relevant.
4. If information cannot be verified from the workspace, command output, or this conversation, label it **Unknown**. Do not infer it.
5. Preserve useful existing history. Update a canonical current-state file instead of overwriting prior records without reason.

### Capture the actual state

Inspect at least:

- the repository status, current branch, latest commit, and any modified or untracked files;
- the files changed during this session and the reason for each change;
- architecture or product decisions made, including alternatives rejected and why;
- commands run, their results, and validation that remains undone;
- relevant pull requests, issues, releases, deployments, servers, or third-party services — using identifiers and links only when already known and safe to record;
- blockers, risks, assumptions, and the exact next actions.

### Write project memory

If the project already has an established agent-memory or handoff location, extend it. Otherwise create:

- `docs/ai/SESSION_CONTEXT.md` — the current source of truth for the next session;
- `docs/ai/SESSION_LOG.md` — an append-only dated summary of this session.

Keep the current-context document concise but complete. It must contain these sections:

```markdown
# Session context

## Goal
## Current repository state
## What changed
## Decisions and rationale
## System and operational context
## Validation performed
## Known risks and open questions
## Next actions, in order
## How to resume
```

For **How to resume**, name the most relevant files, the branch or PR, and the first safe command to run. For **Next actions**, include dependencies and a clear definition of done.

Append a short dated entry to the session log with the goal, completed work, verification, and next action.

### Final response

Reply with:

1. the documentation files created or updated;
2. a short summary of the durable context saved;
3. the single highest-priority next action;
4. any information that remains unknown or needs user input.
