# Agent Instructions — Dopa-Direct

Read README.md, CONTRIBUTING.md and FEATURE_UPGRADE_PLAN.md first.

- Preserve local-first behavior and user control.
- Do not collect browsing content, credentials or sensitive user data.
- Treat the optional Windows guardian as sensitive OS integration: inspect permissions, make it opt-in and reversible.
- Add deterministic timer and persistence tests, including corrupt-state recovery.
- Never add medical diagnosis/treatment claims.
- Run checks and report exact commands/platform; use a branch and submit a PR.
- Do not merge, deploy or change OS settings on behalf of a user.
