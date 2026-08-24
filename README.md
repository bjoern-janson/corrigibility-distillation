# Corrigibility Distillation

A provenance-preserving research repository for extracting, testing, and then **leaving behind** claims about corrective systems when the evidence ceiling is reached.

The repository began as a reconstructive distillation of a frozen 14-repository corpus. That lane is now closed. The repository now also houses **new prospective experiments** that are downstream of, but do not rewrite, the frozen corpus record.

## Current state

| Lane | Status | Strongest earned result |
|---|---|---|
| Corpus Distillation | **CLOSED** | Recurring corrective constraints exist; three local necessities were earned; no common reducible core, mechanism substitutability, or full cross-repository interface was demonstrated. |
| CGP-001 — Constraint-Geometry Prediction | **CLOSED / NOT EVALUABLE** | The first prospective NSS→FS corridor attempt failed before composition: its adapter was not semantically well-typed under the frozen parent definitions. `H_CG` was not tested. |
| RIL-001 — Representation-Induced Leverage | **PREREGISTERED / NOT EXECUTED** | No RIL result yet. The assay asks whether changing only representation can reduce the cost of one already-earned FS007 corrective transformation while preserving its identity, scope, authority, and required operations. |

See [`STATUS.md`](STATUS.md) for the exact freeze state and [`ROADMAP.md`](ROADMAP.md) for conjectures that are explicitly **not yet evidence**.

---

## 1. Frozen corpus-distillation result

The canonical corpus is defined in [`CORPUS.md`](CORPUS.md).

The closed lane established the following bounded record:

```text
Phase 1 inventory                 COMPLETE
Phase 2 substitutability          0 / 182 YES or PARTIAL
L4 full mechanism interfaces      0
L4' bounded evidence transport    1
local necessity                   3 NECESSARY
                                  5 NOT DEMONSTRATED
                                  1 DISCONFIRMED
necessity relations               0 DEPENDENT
                                  0 INDEPENDENT
                                  2 NOT COMPARABLE
                                  1 NOT DEMONSTRATED
common reducible core             NOT EARNED
global minimization               CLOSED
L5 composition                    CLOSED
L6 cumulative gain                CLOSED
```

The exact local-necessity audit is preserved in [`NECESSITY_AUDIT.md`](NECESSITY_AUDIT.md).

The durable corpus conclusion is:

> **The corpus contains recurring corrective constraints and several locally indispensable distinctions, but the frozen evidence does not show that those necessities are interchangeable, composable, or instances of one smaller common object.**

Nothing in the newer experimental lanes retroactively changes that result.

---

## 2. CGP-001 — first prospective constraint-geometry test

CGP-001 asked whether the **shape of previously observed separations** could prospectively predict a new cross-mechanism corridor.

The preregistered candidate was:

```text
Negative-Space Search search allocation
-> Future Sufficiency Experiment 007 repair search
```

with the authority firewall:

```text
Psi_NSS != U_FS
```

The full frozen contract is [`CGP_001_PREREGISTRATION.md`](CGP_001_PREREGISTRATION.md).

### Terminal result

The independent translation audit found:

```text
A_trans = FAIL
failed criteria = [8, 9]
CGP-001 = NOT EVALUABLE
H_CG = NOT TESTED
CGP arm execution = NOT AUTHORIZED
```

The two failures were structurally different:

1. **Semantic type mismatch**

   ```text
   FS target/scoring output
   !=
   NSS resolving-probe identity
   ```

2. **Scope/search-object mismatch**

   ```text
   NSS per-signature local expansion
   !=
   one global FS repair-search invocation
   ```

So the attempted corridor was never faithfully constituted. No L0–L3 score was assigned and no primary CGP arm was executed.

The frozen audit is [`CGP_001_TRANSLATION_AUDIT.md`](CGP_001_TRANSLATION_AUDIT.md). The exact recovered apparatus is preserved under [`experiments/cgp_001/`](experiments/cgp_001/). See [`CGP_001_RECOVERY_NOTE.md`](CGP_001_RECOVERY_NOTE.md) for why those artifacts entered the public branch after a local recovery.

The correct interpretation is deliberately narrow:

> **CGP-001 discovered an attempted cross-mechanism coupling that was not semantically well-typed under the frozen definitions.**

It is not evidence that constraint geometry is false, and it is not evidence that another NSS/FS interface must fail.

---

## 3. RIL-001 — Representation-Induced Leverage

RIL opens a different question.

Constraint Geometry asks:

> **Is a transformation semantically/legalistically available at all?**

Representation-Induced Leverage asks only after that question is already settled:

> **Given an already-earned legal transformation, can a change of representation make it cheaper without changing what it means or what it is allowed to do?**

The frozen RIL-001 hypothesis is:

```text
H_RIL001:
P(F,D,R0,R1) = 1
and
C_op_R1(F) < C_op_R0(F)
```

with the intervention:

```text
algorithm A        fixed
function F         fixed
conditions D       fixed
required ops       fixed
authority ceiling  fixed
representation R   varied
```

The assay uses one already-demonstrated Future Sufficiency Experiment 007 correction:

```text
F = low-cost NEEDS_FANOUT repair
```

and compares two coordinate systems already present in the frozen parent implementation:

```text
R0_AST   = canonical Program AST
R1_SEM8  = exact 8-pattern semantic tuple
```

The scientific branch is only candidate prediction:

```text
R0: program.evaluate_local((x,y,z))
R1: semantic_tuple[4*x + 2*y + z]
```

Everything else must remain shared.

The complete preregistration is frozen in [`RIL_001_PREREGISTRATION.md`](RIL_001_PREREGISTRATION.md) at commit `204fe919159145ac9c29f1becfb92b0c511af02b`.

### Preservation before speed

A cheaper arm gets no leverage credit unless the preservation gate passes:

```text
same semantic transformation
same D / scope
same authority ceiling
same required operations
same candidate set and order
same exhaustive search policy
same repair/adoption rule
same held-out behavior
```

The terminal result classes are:

```text
NOT_EVALUABLE
DISQUALIFIED_PRESERVATION_FAILURE
NO_DEMONSTRATED_LEVERAGE
COMPUTE_FOR_MEMORY_TRADEOFF
REPRESENTATION_INDUCED_LEVERAGE
```

**RIL-001 currently has no implementation and no outcome.**

---

## 4. Candidate affordance-geometry notation — not an earned theory

The motivating notation is:

\[
\mathcal A(R)=(\Omega_R,\tau_R,c_R,\mathcal C_R),
\]

where, provisionally:

- `Omega_R` denotes transformations available under representation `R`;
- `tau_R` denotes their semantic/type signatures;
- `c_R` denotes realization cost;
- `C_R` denotes constraints defining the legal transformation region.

A resource-bounded effective repertoire can then be written as the **candidate** object:

\[
\Omega_{\mathrm{eff}}(R;B)
=
\{\omega:\tau_R(\omega)\text{ is valid and }c_R(\omega)\le B\}.
\]

This is roadmap notation, not a corpus result and not something RIL-001 can establish globally.

The motivating conjecture is only:

> **A representation may enlarge the practically reachable repertoire of a fixed substrate by moving useful typed transformations below a resource boundary.**

The repository does **not** claim that representation creates computation, that intelligence is representation, or that the above tuple is a general theory of corrigibility.

---

## 5. Research discipline

This repository uses a strict claim ceiling.

- `mechanism != function != invariant`
- recurrence does not imply necessity
- local necessity does not imply common structure
- similarity does not imply substitution
- serialization does not imply semantic typing
- a new adapter is experimental apparatus, not evidence that an interface already exists
- cheaper does not imply equivalent
- representation construction/translation cost is not free
- a null or `NOT EVALUABLE` result is admissible and must be preserved

When an experiment fails before its intended scientific object is instantiated, the result is recorded at that boundary rather than repaired retrospectively until it works.

---

## 6. Repository map

```text
README.md
    front door and current scientific narrative
STATUS.md
    exact lane-by-lane freeze state
ROADMAP.md
    prospective RIL ladder and effective-repertoire conjectures
AGENTS.md
    execution / preservation rules for future work
CORPUS.md
    frozen 14-repository corpus boundary
NECESSITY_AUDIT.md
    frozen local-necessity result
CGP_001_PREREGISTRATION.md
    frozen CGP-001 prospective contract
CGP_001_TRANSLATION_AUDIT.md
    terminal CGP-001 A_trans failure
CGP_001_RECOVERY_NOTE.md
    recovery/integration provenance
experiments/cgp_001/
    exact recovered CGP-001 apparatus; never executed after A_trans failed
RIL_001_PREREGISTRATION.md
    frozen RIL-001 one-function leverage contract
```

## Governing maxim

> **Preserve the scientific identity of the transformation before claiming anything about making it cheaper.**
