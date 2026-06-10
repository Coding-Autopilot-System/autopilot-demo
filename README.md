# autopilot-demo

[![CI](https://github.com/Coding-Autopilot-System/autopilot-demo/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/Coding-Autopilot-System/autopilot-demo/actions/workflows/ci.yml)
[![Demo CI](https://github.com/Coding-Autopilot-System/autopilot-demo/actions/workflows/demo-ci.yml/badge.svg?branch=main)](https://github.com/Coding-Autopilot-System/autopilot-demo/actions/workflows/demo-ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

**Demo target for the Coding-Autopilot-System AI repair pipeline** - triggers intake workflows when CI fails, demonstrating the end-to-end path from failure detection to pull request.

Part of the [Coding-Autopilot-System](https://github.com/Coding-Autopilot-System) autonomous CI repair platform. The control plane lives in [autopilot-core](https://github.com/Coding-Autopilot-System/autopilot-core), and the runner-hosted worker/runtime pattern lives in [ci-autopilot](https://github.com/Coding-Autopilot-System/ci-autopilot).

## Repo boundary

- `autopilot-demo` is not the operator and not the worker host. It is the demonstration target repo.
- `autopilot-core` owns queue scanning, Codex invocation, and PR creation.
- `ci-autopilot` shows the worker/runtime implementation used to process queued repair tasks.

## How the demo works

```mermaid
flowchart LR
    A[Trigger Demo CI\nworkflow_dispatch] --> B[demo-ci.yml runs\nubuntu-latest]
    B --> C{CI result}
    C -->|failure| D[autopilot-create-issue.yml\ncreates intake issue]
    D --> E[Issue: autofix + queued]
    E --> F[autopilot-core operator\npicks up issue]
    F --> G[Codex generates fix]
    G --> H[Pull Request opened]
```

1. Trigger `Demo CI` via `workflow_dispatch` to simulate a CI failure.
2. `autopilot-create-issue.yml` detects the failure and creates an issue labeled `autofix + queued`.
3. The [autopilot-core](https://github.com/Coding-Autopilot-System/autopilot-core) operator scans for the issue and invokes Codex.
4. Codex generates a targeted fix and opens a pull request in this repo.

## Running the demo

```bash
# Trigger the Demo CI workflow (simulates a failure)
gh workflow run demo-ci.yml -R Coding-Autopilot-System/autopilot-demo

# Watch for the intake issue to be created
gh issue list -R Coding-Autopilot-System/autopilot-demo --label autofix --label queued

# Monitor autopilot-demo for the fix PR
gh pr list -R Coding-Autopilot-System/autopilot-demo
```

## Demo runbook

1. Trigger [`.github/workflows/demo-ci.yml`](.github/workflows/demo-ci.yml) to produce a known failure signal.
2. Confirm [`.github/workflows/autopilot-create-issue.yml`](.github/workflows/autopilot-create-issue.yml) creates an `autofix + queued` issue.
3. Watch `autopilot-core` pick up the issue and open a PR back into this repo.
4. Use this repo's issue, branch, and PR history as the audit trail for the demo.

## Enterprise proof points

- Demonstrates bounded blast radius: the platform proposes a fix in a dedicated target repo before broader rollout.
- Produces an auditable story for reviewers: failure event, queued issue, operator pickup, and PR are visible artifacts.
- Keeps the demo reproducible with workflow-dispatch entry points rather than hidden local steps.

## Workflows

| Workflow | Purpose |
|----------|---------|
| `ci.yml` | Portfolio CI - YAML validation (always passes) |
| `demo-ci.yml` | Demo trigger - simulates CI activity to test intake flow |
| `autopilot-create-issue.yml` | Intake - creates `autofix + queued` issue on workflow failure |

## Documentation

- [Wiki](https://github.com/Coding-Autopilot-System/autopilot-demo/wiki) - setup guide, architecture, configuration reference
- [autopilot-core](https://github.com/Coding-Autopilot-System/autopilot-core) - operator control plane
- [ci-autopilot](https://github.com/Coding-Autopilot-System/ci-autopilot) - worker/runtime reference
- [Coding-Autopilot-System org](https://github.com/Coding-Autopilot-System)
