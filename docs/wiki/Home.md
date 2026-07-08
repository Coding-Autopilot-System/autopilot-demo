# autopilot-demo Wiki

`autopilot-demo` is the **proof repo** for the Coding-Autopilot-System autonomous CI-repair
platform. It is a deliberately safe target that demonstrates the full failure-to-fix loop
without touching production control-plane infrastructure.

## Role in the CAS portfolio

| Repo | Role |
|---|---|
| [autopilot-core](https://github.com/Coding-Autopilot-System/autopilot-core) | Control plane: queue scanning, Codex invocation, PR creation |
| [ci-autopilot](https://github.com/Coding-Autopilot-System/ci-autopilot) | Worker/runtime reference implementation |
| **autopilot-demo** (this repo) | Demonstration target: shows the failure-to-fix loop end to end |

## Quickstart

```bash
# Trigger the Demo CI workflow (simulates a failure)
gh workflow run demo-ci.yml -R Coding-Autopilot-System/autopilot-demo

# Watch for the intake issue to be created
gh issue list -R Coding-Autopilot-System/autopilot-demo --label autofix --label queued

# Monitor autopilot-demo for the fix PR
gh pr list -R Coding-Autopilot-System/autopilot-demo
```

See the full [Demo runbook](../../README.md#demo-runbook) in the README for the reset and
troubleshooting procedure.

## Where to go next

- [Architecture](Architecture.md) — the demo trigger-to-PR flow
- [Operations](Operations.md) — verified run/test/CI commands
- [Decisions](Decisions.md) — index of recorded architectural decisions

<!-- docs-verified: ec62179aa2c20bc731542de4ac3fec9cc94a831d 2026-07-08 -->
