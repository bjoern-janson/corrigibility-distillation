"""RIL-001 tests. Primary tests are opt-in only after implementation freeze."""
from __future__ import annotations
import os
import sys
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import audit
import algorithm
import contract
import instrument

PARENT = Path(os.environ.get("RIL001_PARENT", ""))


@unittest.skipUnless(PARENT.is_file(), "set RIL001_PARENT to frozen FS007 source")
class PreFreezeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.parent = contract.import_parent(PARENT)
        contract.verify_parent(cls.parent)

    def test_candidate_counts(self) -> None:
        self.assertEqual(len(self.parent.READ_ONCE_PROGRAMS), 94)
        self.assertEqual(len(self.parent.FANOUT_PROGRAMS), 127)

    def test_all_eight_pattern_semantic_equivalence(self) -> None:
        for language, programs in (("M0", self.parent.READ_ONCE_PROGRAMS),
                                   ("M1", self.parent.FANOUT_PROGRAMS)):
            manifest = contract.build_manifest(language, programs)
            ast = contract.build_candidate_view(contract.Representation.R0_AST, programs, manifest)
            sem = contract.build_candidate_view(contract.Representation.R1_SEM8, programs, manifest)
            for left, right in zip(ast, sem, strict=True):
                self.assertEqual(left.identity, right.identity)
                for pattern in self.parent.LOCAL_PATTERNS:
                    self.assertEqual(contract.predict_ast(left.payload, pattern),
                                     contract.predict_sem8(right.payload, pattern))

    def test_fixed_algorithm_static_shape(self) -> None:
        result = audit.static_fixed_algorithm_audit()
        self.assertTrue(all(result.values()), result)

    def test_unmapped_representation_fails_closed(self) -> None:
        with self.assertRaises(contract.RILContractError):
            contract.parse_representation("OTHER")

    def test_opcode_instrumentation_on_tiny_nonprimary_data(self) -> None:
        task = self.parent.Task((0, 1, 2))
        example = self.parent.Example(bits=(0, 1, 1) + (0,) * 15, task=task,
                                      hidden=1, raw_id=999999)
        m0man = contract.build_manifest("M0", self.parent.READ_ONCE_PROGRAMS)[:1]
        m1man = contract.build_manifest("M1", self.parent.FANOUT_PROGRAMS)[:1]
        m0dict = dict(list(self.parent.READ_ONCE_PROGRAMS.items())[:1])
        m1dict = dict(list(self.parent.FANOUT_PROGRAMS.items())[:1])
        m0 = contract.build_candidate_view(contract.Representation.R0_AST, m0dict, m0man)
        m1 = contract.build_candidate_view(contract.Representation.R0_AST, m1dict, m1man)
        counter = instrument.OpcodeCounter(self.parent)
        counter.start()
        try:
            algorithm.run_transform(self.parent, contract.Representation.R0_AST,
                                    m0, m1, [example], [example], contract.predict_ast)
        finally:
            counter.stop()
        self.assertGreater(counter.counts["eval"], 0)
        self.assertGreater(counter.counts["search"], 0)
        self.assertGreater(counter.counts["update"], 0)


@unittest.skipUnless(PARENT.is_file() and os.environ.get("RIL001_ENABLE_PRIMARY") == "1",
                     "primary tests permitted only after implementation freeze")
class PostFreezePrimaryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.parent = contract.import_parent(PARENT)
        contract.verify_parent(cls.parent)
        cls.probe, cls.heldout = contract.build_dataset(cls.parent)

    def test_parent_positive_control(self) -> None:
        self.assertTrue(audit.parent_positive_control(self.parent)["passed"])

    def test_preservation(self) -> None:
        report = audit.preservation_check(self.parent, self.probe, self.heldout)
        self.assertTrue(report.passed, report.to_dict())


if __name__ == "__main__":
    unittest.main()
