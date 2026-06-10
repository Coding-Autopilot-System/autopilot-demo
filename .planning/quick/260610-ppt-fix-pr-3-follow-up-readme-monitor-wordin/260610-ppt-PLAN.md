---
quick_id: 260610-ppt
mode: quick-full
status: complete
date: 2026-06-10
---

# Correct README monitor wording to match autopilot-demo

## Goal

Correct the PR #3 follow-up wording so the README comment names the same repository queried by the following command.

## Tasks

1. Update the README monitoring comment from `autopilot-core` to `autopilot-demo`.
2. Record the successful fix in `memory/examples/` as required by `AGENTS.md`.
3. Verify the intended wording, unchanged command target, branch, and patch formatting.

## Must Haves

- The monitoring comment says `Monitor autopilot-demo for the fix PR`.
- The following command remains `gh pr list -R Coding-Autopilot-System/autopilot-demo`.
- `git diff --check` passes.
- The work remains on `docs/portfolio-hardening-20260610`.

## Plan Check

Passed: the plan covers the requested wording correction, repo-local memory requirement, branch constraint, and explicit validation gate without unrelated changes.
