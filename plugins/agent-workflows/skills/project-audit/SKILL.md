---
name: project-audit
description: Perform a deep, evidence-based, read-only audit of a software project. Use when Codex needs to map architecture, build and deployment paths, server posture, security risks, unfinished work, and prioritized remediation before proposing or making changes.
---

# Project Audit

Audit the project before changing it. Produce conclusions that a maintainer can verify from evidence.

## Workflow

1. Inventory tracked files and relevant untracked configuration. Identify stack, entry points, package manifests, tests, docs, scripts, CI/CD, containers, infrastructure, environment templates, and git state.
2. Map the system: application and data flow, trust boundaries, auth and permissions, persistence, background jobs, external APIs, and user-facing surfaces.
3. Map operations: configuration, local setup, build, test, deploy, monitoring, backup, rollback, and any server connection instructions found in the repository.
4. Review security using the actual stack: secrets, input validation, authn/authz, dependency and supply-chain risk, file/network access, logging, errors, CI permissions, containers, and exposed configuration.
5. Review engineering health: test coverage, reliability, performance hotspots, maintainability, documentation, TODOs, migrations, release process, and unfinished product work.
6. Run only safe and relevant existing checks. Record each command and outcome; identify checks that could not run and why.

## Safety boundary

- Keep the audit read-only unless the user explicitly approves a fix.
- Do not connect to servers, use credentials, call production APIs, scan networks, or run destructive commands without separate explicit authorization.
- Do not reveal secrets or private data. Cite a redacted location instead.
- Separate verified facts, reasonable concerns, and unknowns.

## Required output

Return these sections: executive summary; scope and coverage; system map; build, test, deploy, and server posture; prioritized findings; quick wins; recommended roadmap; unknowns and excluded scope; and commands or sources inspected.

Rank findings P0–P3. Every finding needs evidence (`path:line`, configuration key, test result, or reproducible command), impact, smallest sensible fix, and validation method. End with the three highest-leverage actions and request approval before remediation.
