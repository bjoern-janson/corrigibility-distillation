# Research Execution Instructions

Scientific history is append-only at the level of frozen claims. Later positives do not rewrite earlier nulls, later nulls do not erase earlier bounded positives, and later conjectures do not become historical evidence.

## Current lane state

```text
Corpus Distillation  CLOSED
CGP-001              CLOSED / NOT EVALUABLE
RIL-001              CLOSED / REPRESENTATION_INDUCED_LEVERAGE
RIL-002              CLOSED / FAMILY_WIDE_LEVERAGE
RIL-003              TARGET MANIFEST FROZEN / MEMBER EXECUTION NOT YET AUTHORIZED
RIL-4+               NOT OPENED
RD-001               TERMINAL / AVAILABLE LEVERAGE DEMONSTRATED / TRAINING NOT OPENED
RD-002+              NOT OPENED
main-line RG-001     CLOSED AT ADMISSION / FUNCTION_EQUIVALENCE_NOT_CONSTITUTED
main-line RG-002+    NOT OPENED
```

RIL, RD, and RG are separate evidence lanes. Results in one lane do not alter another lane's frozen boundary unless a later prospective artifact explicitly constitutes such a dependency.

## Immutable scientific records

Treat frozen scientific artifacts as append-only. In particular:

```text
CORPUS.md
NECESSITY_AUDIT.md

CGP_001_PREREGISTRATION.md
CGP_001_TRANSLATION_AUDIT.md
CGP_001_RECOVERY_NOTE.md
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
RIL_003_CRYPTO_PROVENANCE_AUDIT.md
RIL_003_TARGET_DERIVATION_AUDIT.md
RIL_003_TARGET_MANIFEST.json
experiments/ril_003/custody/*

REPRESENTATION_DISCOVERY_001_PREREGISTRATION.md
RD001_IMPLEMENTATION_CONTRACT.md
RD001_IMPLEMENTATION_REFREEZE_V2.md
RD001_PRE_CALIBRATION_AUDIT_V1.md
RD001_PRE_CALIBRATION_AUDIT_V2.md
RD001_CALIBRATION_BEACON_REQUEST*.md
RD001_CALIBRATION_BEACON_RAW_V2.json
RD001_CALIBRATION_SEED_V2.md
RD001_CALIBRATION_MANIFEST_V2.json
RD001_CALIBRATION_RESULT_V2.json
RD001_LEARNER_TARGET_COMPATIBILITY_AUDIT.md
RD001_TERMINAL_LESSON.md
experiments/rd_001/*

RG001_F_LCC_SEMANTIC_CONSTITUTION.md
RG001_CASE_FAMILY.json
RG001_CASE_FAMILY_AUDIT.md
experiments/rg_001/reference_evaluator.py
experiments/rg_001/test_reference_evaluator.py
RG001_REALIZER_ADMISSION_CONTRACT.md
RG001_REALIZER_ADMISSION_CONTRACT.json
RG001_REALIZER_ADMISSION_AUDIT.md
RG001_REALIZER_ADMISSION_AUDIT.json
RG001_TERMINAL_LESSON.md
RG_NAMESPACE_NOTE.md
archive/rg_parity_calibration/*

ADMISSIBILITY_FAILURE_ATLAS.md
ADMISSIBILITY_FAILURE_ATLAS.json
COMPRESSION_REVOCABILITY_PRINCIPLE.md
REVISION_PROPAGATION_PRINCIPLE.md
```

Mutable narrative files (`README.md`, `STATUS.md`, `ROADMAP.md`, this file) may summarize later state but may not silently strengthen frozen records.

## General execution discipline

Before any new scientific operation, identify the shallowest still-unearned transition. Do not use later measurements to backfill an earlier missing object.

Preferred order:

```text
constitute scientific object
-> constitute admissible implementation / transport / target
-> freeze it
-> audit the freeze
-> execute only what the audit authorizes
-> preserve nulls and uninterpretable outcomes
-> stop at the registered ceiling
```

A structural encoding is not automatically semantic equivalence. An oracle advantage is not automatically a reusable or learnable target. A revision is not automatically propagated into operative descendants. Compression is not automatically safely revocable.

## RG identifier discipline

Two independent lineages used `RG-001`. `RG_NAMESPACE_NOTE.md` is authoritative.

- **main-line RG-001** = `F_LCC` realizer-admission assay, terminal at admission.
- **parity calibration RG-001/RG-002** = archived historical calibration under `archive/rg_parity_calibration/`.

Do not merge their claims, numbering, or evidence.

## RIL-003 frozen provenance boundary

Scientific anchors:

```text
preregistration freeze   c5acae018aec09afc9ceece152bb9cdc7a39e112
implementation freeze    f54d9e1a4d8ef35404824d2172ace173af387a96
pre-reveal audit         013435145d7d93985cd056926cfad710dd63e662
entropy target time      2026-08-26T12:00:00.000Z
target-manifest freeze   236763606dc43a31cf99362857c8ae10b1f72c6d
```

Frozen scientific inputs now include:

```text
Q_test
I_shared whitelist
I_target_test forbidden set
R0 = R0_AST
R1 = R1_SEM8
future public entropy rule
generic execution apparatus
member gate G_i=(A_fixed_i,P_i,Lambda_i)
claim ceiling
captured NIST pulse custody package
ordered 24-member held-out target family
RIL_003_TARGET_MANIFEST.json
```

Current provenance state:

```text
NIST pulse custody           FROZEN
cryptographic source audit   RECORDED
independent target derivation PASS
eligible universe            193
held-out targets             REVEALED / FROZEN: 24
member preservation output   ABSENT
opcode/memory output         ABSENT
Lambda vector                ABSENT
scientific verdict           NONE
```

### RIL-003 current stop rule

The preregistration requires the committed target manifest / entropy provenance to be audited as the execution gate before member execution.

Until that gate is explicitly closed:

```text
DO NOT run member preservation
DO NOT run member opcode/memory measurements
DO NOT interpret target-specific leverage
DO NOT modify the apparatus
DO NOT redraw, replace, rebalance, or filter targets
DO NOT add target-specific caches, preprocessing, features, compilation, or code paths
```

Next legal sequence:

```text
audit committed target manifest / entropy provenance
-> if PASS, authorize member preservation
-> run A_fixed_i / P_i
-> interpret Lambda_i only where both gates permit it
-> freeze ordered result vector
-> final audit
-> STOP
```

A post-reveal representation change requires a new assay identifier.

## RD-001 terminal boundary

RD-001 must preserve both terminal facts:

```text
AVAILABLE_LEVERAGE_DEMONSTRATED
LEARNER_TARGET_CLASS_MISMATCH / TRAINING_NOT_OPENED
```

The positive calibration is instance-conditioned:

\[
R_\star(X_i)=R_{J_i}(X_i),
\]

with `J_i` varying across realized instances. The frozen learner target language permits one reusable global schema; therefore the oracle family is not automatically the learner target.

Do not repair RD-001 by:

```text
replacing varying J_i with one family-wide latent J*
widening R_L after seeing calibration results
redefining R_STAR to match the learner class
consuming Q_train before a compatible learner target is prospectively constituted
treating oracle leverage as reusable or learned leverage
calling the compatibility failure a learner-performance failure
```

No `Q_train` beacon has been consumed, no learner was run, and no RD successor is open. Any new reusable-coordinate or representation-acquisition experiment requires a new assay identifier and prospective freeze.

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

Exact frozen candidates:

```text
SSI-CALC v0.1
  bjoern-janson/ssi@362594d4337a1c72556b501b6477ff624db919e1
  checker blob 293d373d13bd68b40ed2e5b0f8754146638981d6

OpenCore Nano V0
  bjoern-janson/opencore@d85aac9fa35ea4ba21afebc73b9cb8970c2a1dbf
  nano.py blob d31dacaf893a58a8280c01704fe666a404c1f56c
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

Do **not** repair either adapter under RG-001 v0.1. A future attempt that changes a candidate surface, closure layer, semantic function, case geometry, or adapter ceiling requires a new main-line RG assay identifier.

The admission null is not `V_F=0` and does not establish general incapacity of SSI-CALC or Nano.

## Cross-program principle records

Treat these as interpretive/future-selection constraints, not as permission to skip assay-specific tests:

```text
ADMISSIBILITY_FAILURE_ATLAS.md
COMPRESSION_REVOCABILITY_PRINCIPLE.md
REVISION_PROPAGATION_PRINCIPLE.md
```

In particular:

```text
represented distinction != native consequential semantics
successful compression   != safe future revocability
recorded revision         != operative descendant update
```

Prospective necessity still requires matched evidence or formal proof at the relevant scope.

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

Do not promote it to a universal realization-geometry law or use it as evidence for main-line RG-001, RIL-003, or RD-001.

## Claim ceilings

A positive RIL-003 result can earn only `PROVENANCE_SEPARATED_REPRESENTATION_INDUCED_TRANSFER` within its exact frozen schema and runtime contract.

RD-001 earns instance-specific evaluator-supplied available leverage plus a learner-target-class mismatch; it earns no reusable or learned representation claim.

Main-line RG-001 has no positive cross-realizer claim because it terminated before preregistration and validity measurement.

The archived parity calibration earns only its bounded cost/robustness separation under its exact assay.

## Final rules

**RIL-003:** The held-out territory now exists. Do not touch the representation or targets; close the execution-provenance gate before measuring members.

**RD-001:** Useful oracle geometry is not automatically one reusable learnable object. Stop before training when the target class is mismatched.

**Main-line RG-001:** Constitute the function first; admit realizers second. If admission fails, stop before comparison.

**Program-wide:** Preserve every bounded positive and every null, localize failure at the shallowest evidenced transition, and do not manufacture the missing semantics or authority in an adapter, evaluator, or summary file.
