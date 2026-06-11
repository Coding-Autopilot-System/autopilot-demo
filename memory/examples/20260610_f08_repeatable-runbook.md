# F-08 repeatable operator runbook

Issue Description: The runbook lacked prerequisites, reset steps, and troubleshooting, while repeat demonstrations could leave the matching issue closed.
State: Operators had no defined recovery path and intake updated closed matching issues without reopening them.
Action: Documented prerequisites, expected results, reset and troubleshooting; reopen matching intake issues on repeat failures.
Result: The user journey is repeatable and common failure modes have concrete diagnostics.
Diff Patch: Updated the intake workflow, README, UAT record, and contract tests.
Rationale: A portfolio demo must be operable repeatedly by someone other than its author.
