# Product Growth Audit & Improvement Plan

Use this when an application already exists but its next best improvements are unclear. It works for consumer, B2B, internal, niche, and open-source products — not only mass-market apps.

## Prompt

Perform a product growth audit of this existing application. Combine product strategy, UX/UI critique, customer-value analysis, business thinking, and technical judgment to identify the highest-leverage improvements. Produce an evidence-based roadmap, not a generic feature brainstorm. Do not implement, redesign, publish marketing, contact users, or change production systems until I approve a chosen plan.

### Ground rules

- Start with evidence from the repository, product documentation, current UI, tests, issues, support feedback, analytics, release notes, and any data I explicitly provide.
- Do not invent users, metrics, revenue, competitors, market demand, or analytics. Mark missing evidence as an assumption or a research question.
- Do not assume the product should serve a broad market. Evaluate whether its best path is a focused niche, internal workflow, prosumer tool, B2B product, open-source project, or something else.
- Preserve the product's real differentiators. Do not recommend AI, social features, gamification, paywalls, or growth tactics merely because they are fashionable.
- Use external market or competitor research only when I authorize it; cite sources and separate observed facts from inferences.
- Keep recommendations feasible for the actual team, codebase, budget, platform, privacy posture, and operating environment.

### Understand the product first

1. Inspect the repository and available product materials. Identify who the product appears to serve, its promise, key workflows, platform, current capabilities, technical constraints, business model if any, and current maturity.
2. Map the user journey from discovery or installation through activation, first value, repeated use, support, upgrade, and exit. Include onboarding, empty states, error states, settings, permissions, and recovery paths.
3. Build a short product snapshot with **verified facts**, **assumptions**, **unknowns**, and the highest-value questions that would change the roadmap.
4. If a safe local build or demo exists, experience the primary flows as a user. Do not use production accounts or alter real data without explicit authorization.

### Audit every improvement surface

Evaluate the product through these lenses, using only the ones that apply:

1. **Problem, user, and positioning** — job to be done, user segments, urgency, alternatives, differentiation, and clarity of the product promise.
2. **UX and UI** — information architecture, navigation, onboarding, visual hierarchy, interaction feedback, copy, defaults, empty/loading/error states, responsive behavior, keyboard flow, accessibility, localization, and perceived quality.
3. **Core value and features** — workflow friction, missing capabilities, integrations, automation, collaboration, import/export, configurability, trust, and the smallest improvement that unlocks more value.
4. **Activation, retention, and distribution** — time to first value, reasons to return, documentation, templates, demos, sharing or referral loops, developer adoption, sales-assisted motion, community, app-store or landing-page needs, and niche-specific distribution. Consider monetization only when relevant.
5. **Trust, reliability, and quality** — privacy, security, permissions, data ownership, backups, performance, offline behavior, error recovery, supportability, observability, accessibility, and release confidence.
6. **Technical leverage** — architecture bottlenecks, tests, design system, API quality, cost, maintainability, instrumentation, operational toil, and improvements that make future product work faster or safer.
7. **AI-specific product quality** — only if AI is part of the product: control, transparency, latency, cost, evaluation, failure recovery, user trust, data boundaries, and whether AI solves a real user problem.

### Turn observations into opportunities

Create a non-duplicative opportunity map. Seek breadth, but prefer a smaller set of strong opportunities over an unprioritized idea dump. For every opportunity, include:

- category and affected user or workflow;
- evidence and current pain or missed value;
- the improvement hypothesis and proposed change;
- expected user outcome and business or product outcome when relevant;
- success signal or metric to measure;
- impact, confidence, and effort as **High / Medium / Low**, with rationale;
- dependencies, risks, and the smallest safe experiment or validation step.

Separate quick quality wins, strategic product bets, business or distribution bets, and technical enablers. Do not score an opportunity as high-confidence without evidence.

### Required deliverable

Write or update the project's established product documentation. If none exists, create `docs/product/PRODUCT_GROWTH_AUDIT.md` with this structure:

```markdown
# Product growth audit

## Product snapshot: facts, assumptions, and unknowns
## Primary users, jobs, and current value proposition
## Journey and experience map
## Findings by lens
## Opportunity map
| Priority | Opportunity | Evidence | Expected outcome | Impact | Confidence | Effort | Validation |
## Recommended product direction
## UI/UX improvements
## Technical enablers and quality work
## Growth, business, and distribution options
## 30 / 60 / 90-day roadmap
## Questions that need answers before commitment
```

Prioritize the roadmap into:

- **Now** — the next one or two validated, high-leverage actions;
- **Next** — work that follows after the first outcomes are measured;
- **Later** — larger bets, dependencies, or ideas that need more evidence.

For each roadmap item, specify an owner type, scope, expected outcome, acceptance criteria, measurement plan, and dependency. End with the top three recommended next actions and ask for approval before implementation.
