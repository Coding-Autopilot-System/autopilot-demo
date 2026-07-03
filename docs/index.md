# Autopilot Demo - Developer Landing Page

Welcome to the **autopilot-demo** documentation. This repository serves as the demonstration target for the **Coding-Autopilot-System (CAS)** autonomous CI repair platform.

It triggers intake workflows when Continuous Integration (CI) fails, showcasing the end-to-end path from a failure detection all the way to an autonomous pull request generation.

## Purpose

- **Demonstration Target**: It acts as a sandbox for the CAS repair pipeline to operate against.
- **Bounded Blast Radius**: The platform proposes fixes in this dedicated target repository before any broader rollout.
- **Auditable Story**: Provides a clear and reproducible flow for reviewers—from the initial failure event, through the queued issue, operator pickup, and finally to the proposed pull request.

## Key Components

- **`autopilot-demo`**: This repository itself. It is neither the operator nor the worker host.
- **`autopilot-core`**: The control plane that owns queue scanning, Codex/AI invocation, and PR creation.
- **`ci-autopilot`**: The runner-hosted worker/runtime pattern used to process queued repair tasks.

## Quick Start

To see the system in action:
1. Trigger the Demo CI workflow to simulate a failure.
2. Watch as an intake issue (`autofix + queued`) is automatically created.
3. Observe the `autopilot-core` operator picking up the issue and opening a fix PR.

Check out the [Architecture Document](architecture.md) for a deeper technical dive into the workflow!
