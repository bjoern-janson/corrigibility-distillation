from __future__ import annotations

import unittest
from pathlib import Path

from reference_evaluator import audit_family, evaluate_case, flatten_incidence, load_family


ROOT = Path(__file__).resolve().parents[2]
FAMILY_PATH = ROOT / "RG001_CASE_FAMILY.json"


class RG001ReferenceEvaluatorTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.family = load_family(FAMILY_PATH)
        cls.by_id = {case["case_id"]: case for case in cls.family["cases"]}

    def test_family_audit_passes(self) -> None:
        audit = audit_family(self.family)
        self.assertEqual(audit["status"], "PASS")
        self.assertEqual(audit["case_count"], 8)
        self.assertEqual(audit["permutation_checks"], 256)
        self.assertFalse(audit["realizers_admitted"])

    def test_conjunctive_vs_alternative_pair_aliases_when_grouping_is_erased(self) -> None:
        a = self.by_id["RG001-C04"]
        b = self.by_id["RG001-C05"]
        self.assertEqual(flatten_incidence(a), flatten_incidence(b))

        ra = evaluate_case(a)
        rb = evaluate_case(b)
        self.assertFalse(ra["phase_1"]["s_h"])
        self.assertTrue(rb["phase_1"]["s_h"])

    def test_independent_standing_survives(self) -> None:
        result = evaluate_case(self.by_id["RG001-C03"])
        self.assertFalse(result["phase_1"]["s_g"])
        self.assertFalse(result["phase_1"]["s_h"])
        self.assertTrue(result["phase_1"]["s_u"])

    def test_multi_hop_contraction_closes_transitively(self) -> None:
        result = evaluate_case(self.by_id["RG001-C06"])
        self.assertEqual(
            result["phase_1"],
            {"s_g": False, "s_h": False, "s_j": False},
        )

    def test_branch_selective_survival(self) -> None:
        result = evaluate_case(self.by_id["RG001-C07"])
        self.assertFalse(result["phase_1"]["s_g"])
        self.assertFalse(result["phase_1"]["s_h1"])
        self.assertTrue(result["phase_1"]["s_h2"])
        self.assertTrue(result["phase_1"]["s_u"])

    def test_refutation_does_not_authorize_replacement_but_fresh_support_can(self) -> None:
        result = evaluate_case(self.by_id["RG001-C08"])
        self.assertFalse(result["phase_1"]["s_gp"])
        self.assertTrue(result["phase_2"]["s_gp"])


if __name__ == "__main__":
    unittest.main()
