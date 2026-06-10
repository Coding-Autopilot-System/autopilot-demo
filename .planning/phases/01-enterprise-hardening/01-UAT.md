# Enterprise Hardening UAT

**Date:** 2026-06-10
**Source:** `gsd-audit-fix --severity all --max 8`
**Scope:** demo reproducibility, security, tests, CI, user journey, failure modes, and docs

## Classification

| ID | Severity | Classification | Finding | Files |
|---|---|---|---|---|
| F-01 | high | auto-fixable | The documented demo cannot produce a failure because Demo CI always succeeds. | `.github/workflows/demo-ci.yml`, `README.md` |
| F-02 | high | auto-fixable | CI prints YAML parse warnings but still exits successfully. | `.github/workflows/ci.yml` |
| F-03 | high | auto-fixable | Third-party Actions use mutable major-version tags instead of immutable commit SHAs. | `.github/workflows/ci.yml`, `.github/workflows/autopilot-create-issue.yml` |
| F-04 | medium | auto-fixable | CI and Demo CI do not declare least-privilege token permissions or job timeouts. | `.github/workflows/ci.yml`, `.github/workflows/demo-ci.yml` |
| F-05 | medium | auto-fixable | No automated contract tests protect workflow behavior and security invariants. | `tests/test_workflows.py`, `.github/workflows/ci.yml` |
| F-06 | medium | auto-fixable | Intake processing has no concurrency guard or timeout, allowing duplicate/racing issue updates. | `.github/workflows/autopilot-create-issue.yml` |
| F-07 | low | auto-fixable | Intake issues omit run attempt, event, actor, and failure conclusion from the audit evidence. | `.github/workflows/autopilot-create-issue.yml` |
| F-08 | low | auto-fixable | The demo runbook lacks prerequisites, reset steps, and failure-mode troubleshooting. | `README.md` |

## Manual-only Findings

- M-01: Protect `main` and require the `CI` status check. The GitHub API reports that `main` is not protected.
- M-02: Configure the organization Actions policy to allow only approved actions and require immutable SHA pinning where supported. The current GitHub token cannot read or change this setting.

