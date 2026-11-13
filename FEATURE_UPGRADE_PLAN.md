# Dopa-Direct — Feature Upgrade Plan

## Objective

A local Python tool that helps someone notice a distraction, choose a better next task and track short focus sessions.

## P0 — privacy and reliability

- [ ] Audit all persisted fields and confirm the tool stores only user-entered focus metadata, not private browsing content or credentials.
- [ ] Test timer interruption, invalid state files, clock changes, duplicate sessions and corrupted local JSON.

## P1 — user control

- [ ] Add export/import of local progress data and a clear reset/recovery path.
- [ ] Document Windows-specific guardian permissions and provide a safe disable/uninstall path.

## P2 — personalisation and accessibility

- [ ] Evaluate recommendation quality with opt-in user feedback and no invasive telemetry.
- [ ] Add configurable focus workflows and accessibility improvements.

## Contributor tasks

1. Local state schema and recovery tests.
2. Timer correctness and interruption handling.
3. Guardian permissions, opt-in and removal behavior.
4. Privacy review and opt-in feedback workflow.

## Definition of done

- [ ] All data written to disk is documented.
- [ ] Corrupt/old state files recover safely.
- [ ] Guardian is opt-in, visible and reversible.
- [ ] No medical claims or invasive telemetry are introduced.
