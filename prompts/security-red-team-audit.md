# Security Red-Team Audit & Remediation

Use this workflow to adversarially assess an application, API, website, mobile client, service, or infrastructure repository that you are explicitly authorized to test — then fix verified weaknesses in the codebase.

## Prompt

Run a security-focused red-team assessment of this authorized project, then remediate verified findings. Work like a careful application-security engineer: establish scope, gather evidence, test safely, fix root causes, and prove the fixes with regression tests. Do not mistake scanning output or a theoretical concern for a confirmed vulnerability.

### Authorization gate — complete this first

Before active testing, identify or ask for:

- the explicitly authorized assets, hostnames, repositories, environments, and time window;
- whether the target is local, test, staging, or production;
- approved test accounts, roles, tenants, and non-sensitive fixture data;
- permitted tools and test types, including whether Burp Suite active checks or fuzzing are allowed;
- a hard request-rate and total-request budget, plus a stop contact;
- systems, endpoints, actions, and data that are out of scope.

Default to local or staging. If this authorization is absent or ambiguous, perform **source-only and passive review** and list the active checks that need approval. Never test third-party targets, unrelated domains, production data, or other users' accounts.

### Safety rules

- Do not perform denial-of-service, high-volume enumeration, credential attacks, persistence, data exfiltration, phishing, social engineering, destructive writes, privilege escalation beyond a harmless proof, or lateral movement.
- Use only supplied test accounts and fixture data. Stop immediately if a test can affect real users, money, availability, or irreversible state.
- Do not print or commit secrets, private URLs, tokens, session cookies, raw sensitive responses, or scan artifacts containing them. Redact evidence.
- Do not deploy fixes, rotate secrets, change firewall rules, or contact external systems without separate explicit approval.
- Treat rate limits as a protective control: test them with the smallest pre-agreed request budget and stop on errors, degradation, or unexpected behavior.

### Assessment workflow

1. **Model the target.** Inspect the codebase, dependency manifests, configuration templates, CI/CD, infrastructure, deployment docs, entry points, data stores, trust boundaries, and authentication flows. Record the actual attack surface and unknowns.
2. **Create a threat model.** Identify assets, attackers, trust boundaries, entry points, sensitive operations, abuse cases, and high-value failure modes. Cover web, API, mobile, desktop, background jobs, and infrastructure components that exist in this project.
3. **Review the source.** Look for authorization gaps, insecure direct object references, session and token handling errors, input validation failures, injection risks, unsafe deserialization, SSRF, path traversal, file-upload flaws, command execution, insecure cryptography, secrets exposure, dependency risk, insecure defaults, missing audit logs, unsafe error handling, and insecure CI/CD or infrastructure configuration.
4. **Check abuse controls.** Verify that authentication, password reset, account creation, invitation, upload, search, expensive AI or compute actions, exports, and other sensitive routes have the right rate limits, quotas, idempotency behavior, and per-user/per-tenant boundaries. Confirm failures return safe status codes and messages without revealing useful attack detail.
5. **Test dynamically only within the approved scope.** Start with harmless, minimal proofs using your own test data. When Burp Suite is allowed, use it to observe authorized traffic, run passive checks, and replay carefully selected requests. Use active scanning, Intruder, or fuzzing only when explicitly approved, against non-production targets, and within the agreed request budget. Prefer one controlled proof over broad payload spraying.
6. **Assess browser and API defenses.** Inspect authentication and authorization enforcement, CORS, CSRF, cookies, security headers, caching, request parsing, schema validation, error responses, upload/download handling, webhooks, API versioning, and tenant isolation.
7. **Assess operational controls.** Review secret management, dependency pinning and updates, least-privilege permissions, logging and alerting, backup and rollback paths, CI permissions, container or cloud configuration, and release controls.
8. **Validate every finding.** Classify it as **verified**, **suspected**, or **not reproducible**. Preserve the smallest safe reproduction and evidence needed to support the conclusion. Never store exploit payloads or sensitive captures in the repository.

### Remediation workflow

For each verified finding:

1. Explain the root cause and affected trust boundary.
2. Implement the smallest maintainable fix in the current workspace; do not paper over the symptom.
3. Add or update a regression test that would have failed before the fix.
4. Run relevant unit, integration, and security checks. Re-run the safe reproduction to confirm the issue is closed.
5. Document any deployment, migration, configuration, monitoring, or secret-rotation step that a project owner must perform. Do not perform those external steps automatically.

If you discover a real secret, redact it, report only its location and exposure path, and recommend an owner-led revocation and rotation plan.

### Required deliverable

Write or update the project's established security documentation. If none exists, create `docs/security/SECURITY_AUDIT.md`. Use this structure:

```markdown
# Security audit

## Authorization and scope
## System and threat model
## Coverage and excluded tests
## Findings
| Priority | Status | Area | Evidence | Impact | Root cause | Fix | Regression proof |
## Rate-limit and abuse-control results
## Remediation completed
## Owner actions required
## Remaining risks and unknowns
## Commands and tools used
```

Rank findings as **P0** (critical, immediate harm), **P1** (high impact), **P2** (meaningful risk), or **P3** (hardening or documentation). Cite safe evidence such as a file path and line, a redacted request shape, a test name, or a command result.

End with a concise summary of verified fixes, tests run, owner actions still required, and anything that was intentionally not tested.
