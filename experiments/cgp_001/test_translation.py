"""Translation-only tests for the frozen CGP-001 apparatus.

These tests exercise source verification, the pure translation, and the exact
NSS allocation fixture.  They never call ``run_arm`` and therefore never
inspect a primary CGP outcome.
"""

from __future__ import annotations

from dataclasses import replace
import inspect
from itertools import product
import json
import os
from pathlib import Path
import sys
from types import SimpleNamespace
import unittest

from experiments.cgp_001.cgp_001 import (
    ApparatusVerificationError,
    TranslationContractError,
    canonical_episode_records,
    nss_allocate,
    run_arm,
    translate_examples,
    verify_apparatus,
)


REPOSITORY_ROOT = Path(__file__).resolve().parents[2]
WORK_ROOT = REPOSITORY_ROOT.parent
NSS_ROOT = Path(
    os.environ.get("CGP001_NSS_ROOT", WORK_ROOT / "cgp001-negative-space-search")
)
FS_ROOT = Path(
    os.environ.get("CGP001_FS_ROOT", WORK_ROOT / "cgp001-future-sufficiency")
)
FIXTURE_PATH = REPOSITORY_ROOT / "experiments/cgp_001/fixtures/translation_fixtures.json"


def _canonical_bytes(episodes: tuple[object, ...]) -> bytes:
    return json.dumps(
        canonical_episode_records(episodes),
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")


class FrozenTranslationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.parents = verify_apparatus(fs_root=FS_ROOT, nss_root=NSS_ROOT)
        cls.fs = cls.parents.fs
        cls.language = cls.parents.nss_language
        cls.operator = cls.parents.nss_operator
        cls.fixtures = json.loads(FIXTURE_PATH.read_text(encoding="utf-8"))
        cls.valid_by_id = {
            fixture["id"]: fixture
            for fixture in cls.fixtures["valid_fixtures"]
        }

    @classmethod
    def _record(cls, row: dict[str, object]) -> object:
        bits = tuple(row["bits"])  # type: ignore[arg-type]
        task_args = tuple(row["task_args"])  # type: ignore[arg-type]
        if "raw_id" not in row:
            return SimpleNamespace(
                bits=bits,
                task=cls.fs.Task(task_args),
                hidden=row["hidden"],
            )
        return cls.fs.Example(
            bits=bits,
            task=cls.fs.Task(task_args),
            hidden=row["hidden"],
            raw_id=row["raw_id"],
        )

    @classmethod
    def _records(cls, rows: list[dict[str, object]]) -> tuple[object, ...]:
        return tuple(cls._record(row) for row in rows)

    @classmethod
    def _episodes_for(cls, fixture_id: str) -> tuple[object, ...]:
        fixture = cls.valid_by_id[fixture_id]
        return translate_examples(cls._records(fixture["source_records"]))

    @classmethod
    def _signature_partition(cls, episodes: tuple[object, ...]) -> list[list[str]]:
        grouped: dict[tuple[bool, ...], list[str]] = {}
        for episode in episodes:
            signature = cls.language.current_language_signature(episode)
            grouped.setdefault(signature, []).append(episode.episode_id)
        return sorted((sorted(ids) for ids in grouped.values()), key=lambda ids: ids[0])

    @classmethod
    def _label_groups(cls, episodes: tuple[object, ...]) -> list[list[str]]:
        grouped: dict[tuple[bool, ...], set[str]] = {}
        for episode in episodes:
            signature = cls.language.current_language_signature(episode)
            grouped.setdefault(signature, set()).add(episode.resolving_probe)
        return sorted((sorted(labels) for labels in grouped.values()), key=lambda row: row)

    @classmethod
    def _gate(cls, episodes: tuple[object, ...]) -> tuple[int, str]:
        policy = cls.operator.BoundaryGatedGenericSynthesizer()
        policy.fit(episodes)
        expanded = int(policy.expanded_signature_count)
        return expanded, "SKIP" if expanded == 0 else "INVOKE"

    def test_translator_has_only_the_record_sequence_input(self) -> None:
        signature = inspect.signature(translate_examples)
        self.assertEqual(tuple(signature.parameters), ("examples",))

    def test_substantive_entrypoint_requires_runner_capability(self) -> None:
        signature = inspect.signature(run_arm)
        capability = signature.parameters["execution_capability"]
        self.assertEqual(capability.kind, inspect.Parameter.KEYWORD_ONLY)
        self.assertIs(capability.default, inspect.Parameter.empty)

    def test_frozen_source_verification_and_counts(self) -> None:
        self.assertEqual(len(self.language.current_language()), 78)
        self.assertEqual(len(self.fs.READ_ONCE_PROGRAMS), 94)
        self.assertEqual(len(self.fs.FANOUT_PROGRAMS), 127)
        package = sys.modules["negative_space_search"]
        self.assertIsNone(getattr(package, "__file__", None))
        self.assertEqual(
            tuple(Path(item).resolve() for item in package.__path__),
            ((NSS_ROOT / "src/negative_space_search").resolve(),),
        )

    def test_valid_frozen_fixtures(self) -> None:
        for fixture in self.fixtures["valid_fixtures"]:
            with self.subTest(fixture=fixture["id"]):
                records = self._records(fixture["source_records"])
                episodes = translate_examples(records)
                observed = json.loads(_canonical_bytes(episodes).decode("utf-8"))
                self.assertEqual(observed, fixture["expected_episodes"])
                self.assertEqual(
                    self._signature_partition(episodes),
                    fixture["expected_signature_partition_by_episode_id"],
                )
                self.assertEqual(
                    len(self._signature_partition(episodes)),
                    fixture["expected_distinct_signature_count"],
                )
                allocation = nss_allocate(parents=self.parents, examples=records)
                self.assertEqual(
                    allocation["true_collision_signature_count"],
                    fixture["expected_collision_signature_count"],
                )
                self.assertEqual(
                    allocation["expanded_signature_count"],
                    fixture["expected_expanded_signature_count"],
                )
                self.assertEqual(allocation["allocation"], fixture["expected_allocation"])

    def test_source_multiset_permutation_invariance(self) -> None:
        for check in self.fixtures["determinism_checks"]:
            fixture = self.valid_by_id[check["base_fixture_id"]]
            source = fixture["source_records"]
            expected: bytes | None = None
            for permutation in check["source_index_permutations"]:
                permuted = [source[index] for index in permutation]
                records = self._records(permuted)
                episodes = translate_examples(records)
                canonical = _canonical_bytes(episodes)
                if expected is None:
                    expected = canonical
                self.assertEqual(canonical, expected)
                self.assertEqual(
                    nss_allocate(parents=self.parents, examples=records)["allocation"],
                    check["expected_allocation"],
                )

    def test_translation_preserves_duplicate_records_with_distinct_raw_ids(self) -> None:
        fixture = self.valid_by_id["canonical_sort_projection_and_skip"]
        episodes = translate_examples(self._records(fixture["source_records"]))
        self.assertEqual(len(episodes), 3)
        self.assertEqual(episodes[1].paired_measurements, episodes[2].paired_measurements)
        self.assertEqual(episodes[1].resolving_probe, episodes[2].resolving_probe)

    def test_translation_does_not_mutate_source_records(self) -> None:
        fixture = self.valid_by_id["canonical_sort_projection_and_skip"]
        records = self._records(fixture["source_records"])
        before = tuple(records)
        translate_examples(records)
        self.assertEqual(records, before)

    def test_inert_episode_fields_do_not_change_gate(self) -> None:
        for check in self.fixtures["post_translation_inert_field_checks"]:
            base = self._episodes_for(check["base_fixture_id"])
            mutated = list(base)
            for mutation in check["episode_mutations"]:
                index = mutation["episode_index"]
                replacements = {
                    key: value
                    for key, value in mutation.items()
                    if key != "episode_index"
                }
                mutated[index] = replace(mutated[index], **replacements)
            mutated_tuple = tuple(mutated)
            self.assertEqual(
                self._signature_partition(mutated_tuple),
                self._signature_partition(base),
            )
            self.assertEqual(self._label_groups(mutated_tuple), self._label_groups(base))
            expanded, allocation = self._gate(mutated_tuple)
            self.assertEqual(expanded, check["expected_expanded_signature_count"])
            self.assertEqual(allocation, check["expected_allocation"])

    def test_uniform_surface_hint_preserves_partition_not_signature_values(self) -> None:
        for check in self.fixtures["uniform_surface_hint_checks"]:
            with self.subTest(check=check["id"]):
                base = self._episodes_for(check["base_fixture_id"])
                changed = tuple(
                    replace(episode, surface_hint=check["uniform_surface_hint"])
                    for episode in base
                )
                base_signatures = tuple(
                    self.language.current_language_signature(episode)
                    for episode in base
                )
                changed_signatures = tuple(
                    self.language.current_language_signature(episode)
                    for episode in changed
                )
                self.assertEqual(
                    base_signatures == changed_signatures,
                    check["expected_signature_values_equal"],
                )
                self.assertEqual(
                    self._signature_partition(changed),
                    self._signature_partition(base),
                )
                self.assertEqual(self._label_groups(changed), self._label_groups(base))
                self.assertEqual(self._gate(changed)[1], check["expected_allocation"])

    def test_exact_signature_equivalence_equals_full_m0(self) -> None:
        patterns = tuple(product((0, 1), repeat=3))
        rows: list[dict[str, object]] = []
        for raw_id, values in enumerate(patterns):
            bits = [0] * 18
            bits[:3] = values
            rows.append(
                {
                    "bits": bits,
                    "task_args": [0, 1, 2],
                    "hidden": 0,
                    "raw_id": raw_id,
                }
            )
        episodes = translate_examples(self._records(rows))
        by_values = {
            tuple(int(value) for value in episode.ordered_trace[:3]): episode
            for episode in episodes
        }
        for left in patterns:
            for right in patterns:
                signature_equal = (
                    self.language.current_language_signature(by_values[left])
                    == self.language.current_language_signature(by_values[right])
                )
                full_m0_equal = all(
                    program.evaluate_local(left) == program.evaluate_local(right)
                    for program in self.fs.READ_ONCE_PROGRAMS.values()
                )
                self.assertEqual(signature_equal, full_m0_equal)
                self.assertEqual(full_m0_equal, left == right)

    def test_fail_closed_frozen_fixtures(self) -> None:
        for fixture in self.fixtures["fail_closed_fixtures"]:
            with self.subTest(fixture=fixture["id"]):
                records = self._records(fixture["source_records"])
                with self.assertRaises(TranslationContractError):
                    translate_examples(records)

    def test_additional_malformed_record_fails_closed(self) -> None:
        with self.assertRaises(TranslationContractError):
            translate_examples((object(),))

    def test_source_verifier_fails_closed_on_missing_checkout(self) -> None:
        missing = REPOSITORY_ROOT / "definitely-not-a-frozen-parent"
        with self.assertRaises(ApparatusVerificationError):
            verify_apparatus(fs_root=missing, nss_root=NSS_ROOT)


if __name__ == "__main__":
    unittest.main()
