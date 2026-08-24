# RG namespace note

Status: **PROVENANCE NOTE — IDENTIFIER COLLISION PRESERVED, NOT SILENTLY RESOLVED**

On 2026-08-24, two independently developed Realization Geometry lineages used the label `RG-001` for different scientific objects.

## Main-line RG-001

Current `main` contains:

```text
RG001_F_LCC_SEMANTIC_CONSTITUTION.md
RG001_CASE_FAMILY.json
experiments/rg_001/reference_evaluator.py
experiments/rg_001/test_reference_evaluator.py
```

Its constituted object is `F_LCC`. The semantic constitution explicitly states `Realizers admitted: NO`. This lineage is not the parity cost/robustness assay.

## Parity calibration lineage

The branch `rg-001-realization-geometry` independently froze and executed a 12-bit parity calibration lineage whose internal identifiers are:

```text
RG-001  CLOSED / NOT_EVALUABLE
RG-002  CLOSED / COST_ROBUSTNESS_TRADEOFF
```

Terminal branch commit:

```text
e94aed7943cf31ecfed33e408da82a72404fdac6
```

That lineage is imported into `main` byte-for-byte under:

```text
archive/rg_parity_calibration/
```

The frozen files retain their original identifiers and contents. They are **not renamed retroactively**.

## Interpretation rule

Do not treat the two `RG-001` labels as the same assay, continuation, replication, or evidence lineage.

When referring to the parity result from `main`, use a disambiguating phrase such as:

```text
parity RG calibration / original branch RG-002
```

Its bounded earned result remains:

\[
V_0=V_1=1,\qquad C_1<C_0,\qquad B_1\subsetneq B_0.
\]

with terminal verdict `COST_ROBUSTNESS_TRADEOFF` under the exact frozen 12-bit parity, CPython opcode-cost, and one-bit auxiliary-memory fault contracts.

This note does not strengthen either lineage and does not modify RIL-003.
