# Deep Project Audit

Use this to understand an unfamiliar codebase, uncover risks, and create an evidence-based improvement plan before changing anything.

## Prompt

Perform a deep, read-only audit of this project. Build an accurate picture of how it works, how it is operated, what is risky, and what should happen next. Do not change files, dependencies, infrastructure, or external systems unless I explicitly ask after you present the findings.

### Safety boundary

- Treat every file as potentially sensitive. Do not print raw secrets, tokens, private URLs, credentials, or customer data. Report locations and redact values.
- Do not connect to servers, use saved credentials, call production APIs, scan public IPs, or run destructive commands. For a server, inspect only repository configuration and documentation unless I grant separate, explicit access.
- Do not claim a vulnerability or deployment fact without evidence. Separate **verified facts**, **reasonable concerns**, and **unknowns**.

### Audit method

1. **Inventory the project.** Identify the language, frameworks, package manifests, entry points, modules, tests, scripts, docs, CI/CD, containers, infrastructure-as-code, environment templates, and git state. For a large repository, report the coverage and prioritize high-risk areas.
2. **Map the system.** Explain the application flow, data flow, trust boundaries, authentication and authorization model, storage, background jobs, external APIs, and user-facing surfaces. Trace from entry point to important side effects.
3. **Understand operations.** Find how the project is configured, built, tested, deployed, observed, backed up, and rolled back. If server access or connection instructions exist, describe the mechanism and its risks without using the credentials.
4. **Review security.** Check secret handling, permissions, input validation, authentication, authorization, dependency risk, injection paths, file and network access, logging, error handling, supply-chain controls, CI permissions, container hardening, and exposed configuration. Use the project's actual stack; do not apply a generic checklist blindly.
5. **Review engineering health.** Assess tests, reliability, performance hotspots, maintainability, documentation gaps, dead code, TODOs, migration risk, release process, and unfinished product work.
6. **Validate selectively.** Run safe, relevant read-only commands and existing checks when practical. Record the command and outcome. If a check cannot run, explain why and what would be needed.

### Required report

Return a structured report with this exact shape:

```markdown
# Project audit

## Executive summary
## Scope and coverage
## System map
## Build, test, deploy, and server posture
## Findings
| Priority | Area | Evidence | Impact | Recommended fix | Validation |
## Quick wins
## Recommended roadmap
## Unknowns and excluded scope
## Appendix: commands and sources inspected
```

Rank every finding as:

- **P0** — active or likely critical harm, data loss, or unauthorized access;
- **P1** — high-impact weakness or blocker that should be addressed soon;
- **P2** — meaningful reliability, security, or maintainability risk;
- **P3** — improvement opportunity or documentation debt.

For each finding, cite concrete evidence such as `path/to/file:line`, a configuration key, a test result, or a reproducible command. Include preconditions, likely impact, the smallest sensible fix, and how to verify it. Do not create findings merely to fill the table.

End with the three highest-leverage actions and ask for approval before implementing any remediation.
