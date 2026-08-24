from __future__ import annotations
import json
import sys
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
PARENT = ROOT / "parent" / "meta_language_repair.py"
FAMILY = ROOT / "RIL_002_FAMILY.json"
RIL001 = ROOT / "experiments" / "ril_001"
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

from family_audit import family_selection_audit, static_pre_execution_audit
from family_contract import MemberSpec, build_member_dataset, load_family, load_inherited


class RIL002PreFreezeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.inherited = load_inherited(RIL001)
        cls.parent = cls.inherited.contract.import_parent(PARENT)
        cls.members = load_family(FAMILY)

    def test_parent_and_inherited_source_integrity(self) -> None:
        audit = self.inherited.contract.verify_parent(self.parent)
        self.assertEqual(audit.source_git_blob, self.inherited.contract.PARENT_SOURCE_GIT_BLOB)
        self.assertTrue(static_pre_execution_audit(RIL001, self.inherited)["passed"])

    def test_family_is_exact_K_enumeration(self) -> None:
        report = family_selection_audit(self.parent, self.members)
        self.assertTrue(report["passed"])
        self.assertEqual(report["member_count"], 24)

    def test_dataset_builder_reproduces_ril001_majority_exactly(self) -> None:
        majority = MemberSpec("CONTROL_17", (0,0,0,1,0,1,1,1), "0x17", "", 0, 0.875, 1.0)
        p2, h2 = build_member_dataset(self.parent, majority, self.inherited)
        p1, h1 = self.inherited.contract.build_dataset(self.parent)
        self.assertEqual(p1, p2)
        self.assertEqual(h1, h2)

    def test_no_primary_cost_files_exist(self) -> None:
        results = HERE / "results"
        if results.exists():
            bad = list(results.rglob("opcode_*.json")) + list(results.rglob("memory_*.json"))
            self.assertEqual(bad, [])


if __name__ == "__main__":
    unittest.main()
