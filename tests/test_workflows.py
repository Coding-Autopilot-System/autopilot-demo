import pathlib
import re
import unittest

import yaml


ROOT = pathlib.Path(__file__).resolve().parents[1]
WORKFLOWS = ROOT / ".github" / "workflows"


class WorkflowContractTests(unittest.TestCase):
    def workflow_text(self, name: str) -> str:
        return (WORKFLOWS / name).read_text(encoding="utf-8-sig")

    def test_all_workflows_are_valid_yaml(self) -> None:
        paths = sorted(WORKFLOWS.glob("*.yml"))
        self.assertTrue(paths, "expected at least one workflow")
        for path in paths:
            with self.subTest(path=path.name):
                self.assertIsInstance(yaml.safe_load(path.read_text(encoding="utf-8-sig")), dict)

    def test_third_party_actions_are_pinned_to_commits(self) -> None:
        action_ref = re.compile(r"uses:\s+[^./\s][^@\s]*@([^\s#]+)")
        for path in WORKFLOWS.glob("*.yml"):
            for ref in action_ref.findall(path.read_text(encoding="utf-8-sig")):
                with self.subTest(path=path.name, ref=ref):
                    self.assertRegex(ref, r"^[0-9a-f]{40}$")

    def test_routine_workflows_are_read_only_and_bounded(self) -> None:
        for name in ("ci.yml", "demo-ci.yml"):
            text = self.workflow_text(name)
            with self.subTest(name=name):
                self.assertIn("permissions:\n  contents: read", text.replace("\r\n", "\n"))
                self.assertIn("timeout-minutes: 5", text)

    def test_demo_failure_is_explicitly_opt_in(self) -> None:
        text = self.workflow_text("demo-ci.yml")
        self.assertIn("simulate_failure:", text)
        self.assertIn("default: false", text)
        self.assertIn("if: ${{ inputs.simulate_failure }}", text)
        self.assertIn("exit 1", text)


if __name__ == "__main__":
    unittest.main()
