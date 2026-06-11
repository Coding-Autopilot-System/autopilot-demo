# F-06 serialized intake processing

Issue Description: Intake processing had no concurrency guard or execution timeout.
State: Multiple failures for the same commit could race while updating the same signature issue.
Action: Serialized intake by workflow head SHA, preserved queued runs, and bounded the job to five minutes.
Result: Intake updates are deterministic and cannot run indefinitely.
Diff Patch: Updated the intake workflow and its contract tests.
Rationale: Idempotent issue handling still needs race protection at the workflow boundary.
