# F-01 reproducible demo failure

Issue Description: The documented demo could not produce a failure because Demo CI always succeeded.
State: Pushes and manual dispatches both ran only a non-blocking step.
Action: Added an explicit `simulate_failure` dispatch input and documented the required command.
Result: Operators can intentionally exercise intake while normal pushes and default dispatches stay green.
Diff Patch: Updated `.github/workflows/demo-ci.yml` and `README.md`.
Rationale: A demo repair pipeline must expose a safe, deliberate, and reproducible failure path.
