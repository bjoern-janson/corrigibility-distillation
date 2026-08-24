# RG-001 Case Family Audit v0.1

**Object:** `RG001_CASE_FAMILY_AUDIT_V0.1`  
**Semantic parent:** `RG001_F_LCC_SEMANTIC_CONSTITUTION.md`  
**Case family:** `RG001_CASE_FAMILY.json`  
**Reference evaluator:** `experiments/rg_001/reference_evaluator.py`  
**Status:** `PASS`  
**Realizers admitted:** `NO`

## 1. Audit scope

This audit tests only the externally constituted support-hypergraph semantics and the reference closure apparatus.

It does not inspect, encode, adapt, execute, or score SSI-CALC or OpenCore Nano.

## 2. Frozen family

```text
case count                 8
expected outputs in cases  NONE / mechanically derived
realizer-specific fields   FORBIDDEN
standing-support cycles    FORBIDDEN
permutation audit          REQUIRED
```

The eight cases cover:

```text
C01 direct contraction
C02 single dependent descendant
C03 independent preservation
C04 conjunctive support
C05 alternative sufficient support
C06 multi-hop contraction
C07 branch-selective mixed survival
C08 replacement firewall + independent re-entry
```

The case identifiers are neutral identifiers, not difficulty levels.

## 3. Matched semantic death test

`RG001-C04` and `RG001-C05` contain the same standings, primitive warrants, initial active warrants, challenged warrant, and flattened parent-to-standing incidence.

They differ only in sufficient-support grouping:

```text
C04: Q(s_h) = {{s_g, w_a}}
C05: Q(s_h) = {{s_g}, {w_a}}
```

Therefore a representation that erases sufficient-set grouping aliases the pair.

The reference evaluator confirms:

```text
flattened pairwise incidence equal  PASS
C04 after challenge: s_h=False      PASS
C05 after challenge: s_h=True       PASS
post-challenge semantics differ     PASS
```

Thus the family contains an externally constituted information-preservation obligation before either candidate realizer enters.

## 4. Permutation audit

For each of the 8 cases, the reference evaluator applies 32 deterministic type-preserving opaque renamings of all standing and warrant identities.

Required invariant:

\[
F_{\mathrm{LCC}}(\pi X)=\pi F_{\mathrm{LCC}}(X).
\]

Authoring-time execution result:

```text
cases                       8
permutations per case      32
total permutation checks  256
failures                     0
status                    PASS
```

The test changes names only; it does not alter support-set structure.

## 5. Reference self-test

The frozen reference test suite contains six tests covering:

```text
family-wide audit and permutation count
conjunctive-vs-alternative matched-pair death test
independent-standing preservation
multi-hop closure
branch-selective survival
replacement firewall plus fresh-evidence re-entry
```

Authoring-time execution result:

```text
Ran 6 tests
failures  0
errors    0
status    PASS
```

This is an authoring-time execution record, not a GitHub Actions provenance claim.

## 6. Mechanically derived semantic consequences

```text
C01 phase 1: s_g=False
C02 phase 1: s_g=False, s_h=False
C03 phase 1: s_g=False, s_h=False, s_u=True
C04 phase 1: s_g=False, s_h=False
C05 phase 1: s_g=False, s_h=True
C06 phase 1: s_g=False, s_h=False, s_j=False
C07 phase 1: s_g=False, s_h1=False, s_h2=True, s_u=True
C08 phase 1: s_g=False, s_gp=False
C08 phase 2: s_g=False, s_gp=True
```

These consequences are generated from the support semantics. They are not stored as answer labels in `RG001_CASE_FAMILY.json`.

## 7. Earned state

The strongest earned statement is:

> The RG-001 v0.1 semantic case family is finite, realizer-blind at the case-schema level, contains a death test for loss of sufficient-support grouping, and is equivariant under the registered opaque identity permutations in the reference evaluator.

This earns:

```text
F_LCC semantic constitution       FROZEN
RG001 case family                 FROZEN
reference closure oracle          IMPLEMENTED
case-family self-test             PASS
permutation audit                 PASS
realizer admission                NEXT
RG-001 preregistration            NOT YET FROZEN
A_trans^RG                        NOT RUN
V_F                               NOT MEASURED
C_F                               NOT MEASURED
B_F                               NOT MEASURED
```

## 8. Next legal transition

Only now may candidate realizers enter for adapter constitution.

The next sequence is:

```text
admit candidate realizers
-> freeze realizer-specific adapters
-> audit adapter information noninterference
-> run A_trans^RG
-> only if both pass, test V_F
-> only if common validity is established, measure C_F
-> derive B_F only from the already frozen challenge family
-> STOP
```

No case-family repair is permitted in response to realizer difficulty under RG-001 v0.1.

> **Adapt the realizer to F. Never adapt F to the realizer.**
