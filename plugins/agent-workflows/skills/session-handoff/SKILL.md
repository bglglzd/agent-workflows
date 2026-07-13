---
name: session-handoff
description: Capture a durable, privacy-safe handoff at the end of a coding or research session. Use when Codex must preserve repository state, decisions, validation results, blockers, and exact next steps so the next human or AI agent can resume without rediscovering context.
---

# Session Handoff

Preserve the state needed to resume work accurately. Do not treat a chat summary as durable project memory.

## Workflow

1. Inspect the workspace before writing: git status, current branch, latest commit, relevant changed files, project docs, and safe command output from this session.
2. Reuse the project's existing memory or handoff convention. If none exists, create `docs/ai/SESSION_CONTEXT.md` as the current source of truth and `docs/ai/SESSION_LOG.md` as an append-only dated record.
3. Update the current-context file with:
   - goal and current repository state;
   - completed changes with relevant file paths;
   - decisions and rationale;
   - system, deployment, PR, issue, or external-service context that is safe to record;
   - commands run and validation results;
   - risks, blockers, and unknowns;
   - ordered next actions and a precise resume checklist.
4. Append a concise dated log entry with the completed work, validation, and next action.
5. Finish by naming the updated files, the highest-priority next action, and the remaining unknowns.

## Guardrails

- Never copy tokens, passwords, private URLs, connection strings, `.env` values, or customer data into project memory.
- Do not modify application code, infrastructure, or external systems merely to create a handoff.
- Preserve history instead of overwriting useful records.
- Mark unverified details as **Unknown**. Do not infer them from incomplete context.
- Include exact file paths, branch or PR identifiers, and commands wherever they make resumption faster.
