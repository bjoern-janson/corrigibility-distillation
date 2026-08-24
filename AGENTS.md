# Research Execution Instructions

Scientific history is append-only at the level of frozen claims. Later positives do not rewrite earlier nulls, and later conjectures do not become historical evidence.

## Current lane state

```text
Corpus Distillation  CLOSED
CGP-001              CLOSED / NOT EVALUABLE
RIL-001              CLOSED / REPRESENTATION_INDUCED_LEVERAGE
RIL-002              CLOSED / FAMILY_WIDE_LEVERAGE
RIL-003              IMPLEMENTATION FROZEN / PRE-REVEAL AUDIT PASS / TARGETS UNREVEALED
RIL-4+               NOT OPENED
main-line RG-001     CLOSED AT ADMISSION / FUNCTION_EQUIVALENCE_NOT_CONSTITUTED
main-line RG-002+    NOT OPENED
```

RIL and RG are separate evidence lanes. RG results do not alter the frozen RIL-003 boundary.

## Immutable scientific records

Treat as frozen:

```text
CORPUS.md
NECESSITY_AUDIT.md
CGP_001_PREREGISTRATION.md
CGP_001_TRANSLATION_AUDIT.md
experiments/cgp_001/*
RIL_001_PREREGISTRATION.md
RIL_001_PRE_EXECUTION_AUDIT.md
experiments/ril_001/* at a0f8f795...
RIL_001_RESULT.*
RIL_001_FINAL_AUDIT.md
RIL_002_PREREGISTRATION.md
RIL_002_FAMILY.json
RIL_002_PRE_EXECUTION_AUDIT.md
experiments/ril_002/* at d46dffe2...
RIL_002_RESULT.*
RIL_002_FINAL_AUDIT.md
RIL_003_PREREGISTRATION.md
RIL_003_GENERATOR_CONTRACT.json
experiments/ril_003/* at f54d9e1a...
RIL_003_PRE_REVEAL_AUDIT.md
RG001_F_LCC_SEMANTIC_CONSTITUTION.md
RG001_CASE_FAMILY.json
RG001_CASE_FAMILY_AUDIT.md
experiments/rg_001/reference_evaluator.py
experiments/rg_001/test_reference_evaluator.py
RG001_REALIZER_ADMISSION_CONTRACT.md
RG001_REALIZER_ADMISSION_CONTRACT.json
RG001_REALIZER_ADMISSION_AUDIT.md
RG001_REALIZER_ADMISSION_AUDIT.json
RG_NAMESPACE_NOTE.md
archive/rg_parity_calibration/*
```

Mutable narrative files may summarize later state but may not silently strengthen these records.

## RG identifier discipline

Two independent lineages used `RG-001`. `RG_NAMESPACE_NOTE.md` is authoritative.

- **main-line RG-001** = `F_LCC` realizer-admission assay, now terminal at admission.
- **parity calibration RG-001/RG-002** = archived historical calibration under `archive/rg_parity_calibration/`.

Do not merge their claims, numbering, or evidence.

## RIL-003 frozen provenance boundary

Scientific anchors:

```text
preregistration freeze   c5acae018aec09afc9ceece152bb9cdc7a39e112
implementation freeze    f54d9e1a4d8ef35404824d2172ace173af387a96
pre-reveal audit         013435145d7d93985cd056926cfad710dd63e662
entropy target time      2026-08-26T12:00:00.000Z
```

Frozen now:

```text
Q_test
I_shared whitelist
I_target_test forbidden set
R0 = R0_AST
R1 = R1_SEM8
future public entropy rule
held-out family size n=24
generic execution apparatus
member gate G_i=(A_fixed_i,P_i,Lambda_i)
claim ceiling
```

Still absent:

```text
held-out target IDs
held-out truth tables
target reveal manifest
member preservation output
opcode/memory output
Lambda vector
scientific verdict
```

Before the frozen entropy boundary, do not perform any target-specific RIL-003 operation. Do not modify the apparatus after `f54d9e1a...`.

After the first admissible future Beacon pulse is captured:

```text
freeze raw custody artifact
-> validate pulse package
-> materialize F_test exactly once from frozen Q_test
-> commit RIL_003_TARGET_MANIFEST.json
-> audit pulse/manifest provenance
-> only then execute member preservation
-> interpret Lambda only where P_i=1
-> final audit
-> STOP
```

## Main-line RG-001 frozen semantic boundary

The scientific object was constituted before realizer admission:

```text
F_LCC semantic constitution       FROZEN
five LCC obligations              FROZEN
8-case sufficient-support family  FROZEN
C04/C05 death test                FROZEN
reference closure oracle          FROZEN / SELF-TEST PASS
```

The decisive pair is permanently:

```text
C04  Q(H)={{G,w_a}}      -> H contracts after G-warrant withdrawal
C05  Q(H)={{G},{w_a}}    -> H survives after G-warrant withdrawal
```

Do not swap IDs, flatten the hyperedges, or alter the case family.

## Main-line RG-001 admission contract and terminal null

Admission contract freeze:

```text
426062c5baa32ea192b99b9a1c8de574eff6eb1e
```

Admission result freeze:

```text
049a2e088c4ab55bf42668607e84f13235e15e18
```

Exact frozen candidates:

```text
SSI-CALC v0.1
  bjoern-janson/ssi@362594d4337a1c72556b501b6477ff624db919e1
  checker blob 293d373d13bd68b40ed2e5b0f8754146638981d6

OpenCore Nano V0
  bjoern-janson/opencore@d85aac9fa35ea4ba21afebc73b9cb8970c2a1dbf
  nano.py blob d31dacaf893a58a8280c01704fe666a404c1f56c
```

The admission adapter ceiling forbids:

```text
reference-oracle access
expected-output lookup
adapter-side closure
adapter-side descendant computation
adapter-side OR-of-routes rescue
adapter-side successor authorization
case-id / canonical-label semantic branching
cost or robustness measurement
new SSI-CALC rule
new Nano primitive
semantic change to F_LCC or the case family
```

Observed terminal admission results:

```text
SSI-CALC v0.1
  A_trans^RG = FAIL
  first failed gate = A6_NATIVE_DEPENDENCY_CONSEQUENCE
  witness = A8_ALTERNATIVE_ROUTE_NON_ALIASING
  repair would violate A14_NO_SEMANTIC_INVENTION

OpenCore Nano V0
  A_trans^RG = FAIL
  first failed gate = A6_NATIVE_DEPENDENCY_CONSEQUENCE
  witness = A8_ALTERNATIVE_ROUTE_NON_ALIASING
  repair would violate A14_NO_SEMANTIC_INVENTION
```

Terminal:

```text
FUNCTION_EQUIVALENCE_NOT_CONSTITUTED
RG-001 preregistration  NOT OPENED
V_F                     NOT RUN
C_F                     NOT RUN
B_F                     NOT RUN
A_F                     NA
```

### RG-001 stop rule

Do **not** repair either adapter under RG-001 v0.1. Do not add a closure layer, select a challenge-surviving route, OR multiple native outputs in the decoder, extend either native kernel, weaken `F_LCC`, or reopen the preregistration.

Any future attempt that changes one of those conditions requires a **new main-line RG assay identifier** and a fresh freeze before implementation.

The admission null is not `V_F=0`. It does not establish general incapacity of SSI-CALC or Nano. It establishes only that function equivalence was not constituted under the frozen realizer surfaces and adapter ceiling.

## Archived parity calibration

The archived parity lineage remains:

```text
parity RG-001  CLOSED / NOT_EVALUABLE
parity RG-002  CLOSED / COST_ROBUSTNESS_TRADEOFF
```

Its bounded result is:

\[
V_0=V_1=1,\qquad C_1<C_0,\qquad B_1\subsetneq B_0.
\]

Do not promote it to a universal realization-geometry law or use it as evidence for main-line RG-001 or RIL-003.

## Claim ceilings

A positive RIL-003 result can earn only `PROVENANCE_SEPARATED_REPRESENTATION_INDUCED_TRANSFER`.

Main-line RG-001 has no positive cross-realizer claim because it terminated before preregistration and validity measurement.

The archived parity calibration earns only its bounded cost/robustness separation under its exact assay.

## Final rules

**RIL-003:** Freeze the territory generator. Whitelist shared information. Freeze the coordinates and apparatus. Do not let held-out target-specific information enter until the protocol says it may exist.

**Main-line RG-001:** Constitute the function first; admit realizers second. If admission fails, stop before comparison.

**Parity calibration:** Same function. Different realizer. Different geometry.
