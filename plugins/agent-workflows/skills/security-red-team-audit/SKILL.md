---
name: security-red-team-audit
description: Run an authorized, safety-bounded red-team security assessment of an application, API, website, mobile client, or service, then fix verified weaknesses with regression tests. Use when Codex must review auth, access control, input handling, rate limits, Burp Suite findings, secrets, dependencies, infrastructure, or abuse paths without testing unapproved targets.
---

# Security Red-Team Audit

Assess and improve security through evidence, minimal-impact verification, and tested remediation.

## Authorization gate

Before active testing, identify the approved assets and environment, allowed tools, test accounts, request budget, time window, stop contact, and excluded systems. Default to local or staging. If scope is absent or ambiguous, perform only source review and passive analysis.

Never target third parties, unapproved domains, production data, or other users' accounts. Never perform denial-of-service, credential attacks, persistence, data exfiltration, destructive writes, phishing, or lateral movement.

## Workflow

1. Map the system, data flow, trust boundaries, entry points, sensitive operations, deployment path, and unknowns.
2. Build a threat model for the actual project.
3. Review source, dependencies, configuration, CI/CD, and infrastructure for authorization gaps, injection, SSRF, file handling, secrets, session handling, insecure defaults, crypto misuse, dependency risk, and unsafe error handling.
4. Review rate limits, quotas, idempotency, and tenant or user boundaries on login, reset, signup, upload, export, search, expensive compute, and other sensitive actions.
5. Run approved dynamic checks with harmless fixture data. When Burp Suite is approved, begin with proxy observation, passive checks, and carefully replayed requests. Use active scans or fuzzing only with explicit approval and within the request budget.
6. Classify every result as verified, suspected, or not reproducible. Preserve only redacted, minimal evidence.
7. For a verified finding, implement the smallest root-cause fix, add a regression test, run relevant checks, and rerun the safe proof.
8. Write or update `docs/security/SECURITY_AUDIT.md` when no project convention exists. Include scope, threat model, coverage, prioritized findings, rate-limit results, completed remediation, owner actions, remaining risk, and commands used.

## Guardrails

- Do not reveal or commit secrets, cookies, tokens, private URLs, raw sensitive responses, or exploit artifacts.
- Do not deploy, rotate secrets, alter infrastructure, or call external systems without separate approval.
- Keep every dynamic test inside the agreed environment and request budget. Stop on instability or unexpected impact.
- Separate verified facts from suspected concerns and unknowns. Do not report scanner output as a confirmed vulnerability.
