# Codex Instructions

## Purpose

Phase 1 inventory, Phase 2 substitutability, L4 interface audit, and the L2 lineage audit are complete.

Current state:

L2 lineage = COMPLETE  
L2 necessity = ACTIVE  
L3 = 0/182 substitutions  
L4 = 0 full mechanism interfaces  
L4' = 1 bounded evidence/provenance transport  
L5 = CLOSED  
L6 = CLOSED  
MINIMIZATION = CLOSED

The active phase is:

## NECESSITY AUDIT

The only question is:

> Does violating a recurring distinction actually break the demonstrated function under the same stated conditions?

The tested object is:

\[
N(I,F,D)
\]

where:

- \(I\) = the exact recurring function/invariant distinction being tested;
- \(F\) = the exact demonstrated function whose success is at issue;
- \(D\) = the exact conditions, dependencies, scope, oracle assumptions, interfaces, budgets, horizons, or other restrictions under which \(F\) was demonstrated.

Do not perform minimization, ranking, architecture design, composition, mechanism deletion, or universalization.

## Frozen evidence base

Use only the completed Phase-1 inventory and already-recorded Phase-2, L4, and L2-lineage records.

Treat those records as authoritative only for facts they explicitly contain.

Do not reread source repositories to add, repair, strengthen, or reinterpret evidence during this audit.

Source repositories may be consulted only to verify an already-recorded citation or reference. They do not become a new evidence stream.

Do not construct new experiments, ablations, adapters, interfaces, formal results, or counterexamples.

If the frozen record does not decide a necessity claim, record `NOT DEMONSTRATED`.

## Candidate set

Begin only with these strongest recurring L2 families:

1. **Evidence / authority / adoption remain distinct.**
2. **Diagnosis / localization precedes adaptation.**
3. **Endpoint or local effect evidence does not establish path / composition / repertoire.**
4. **Information exists does not imply represented, accessible, exploitable, or adopted.**
5. **Preserve history or null standing without manufacturing authority.**
6. **Equivalence is relative to the required future-operation signature.**

Do **not** assume all six qualify for a necessity verdict.

First filter each family by the admissible evidence routes below.

A family with recurrence alone is not enough.

## Eligibility filter

A candidate may proceed to a local necessity judgment only when the frozen evidence contains at least one of:

- an ablation that violates the relevant \(I\);
- a counterexample that violates the relevant \(I\);
- a formal necessity result linking \(I\) to \(F\);
- a demonstrated failure specifically attributable to violation of \(I\).

Independent recurrence, failure-forced lineage status, or formal derivation makes a family eligible for inspection, but does not itself establish necessity.

If no admissible violation evidence is present, record the candidate as:

`NOT DEMONSTRATED`

and do not invent a violation test.

## Deliverable

Use:

| Function / Invariant | Demonstrated Function | Violation Condition | Necessity Evidence | Failure When Violated? | Earned Status |
|---|---|---|---|---|---|

Keep each row local to one exact \(N(I,F,D)\) claim.

If the same recurring family has multiple distinct demonstrated functions or scopes, use separate rows rather than merging them.

Do not produce a global verdict for a family by averaging or combining local rows.

## Status values

`Earned Status` must be exactly one of:

- `NECESSARY`
- `NOT DEMONSTRATED`
- `DISCONFIRMED`

### NECESSARY

Mark `NECESSARY` only when the frozen evidence establishes:

\[
\neg I \Rightarrow F\text{ fails under }D.
\]

The violation and failure must concern the same \(I\), the same demonstrated \(F\), and the same relevant \(D\).

The evidence must establish that the failure follows from the violation, not merely that the two co-occurred.

### NOT DEMONSTRATED

Mark `NOT DEMONSTRATED` when the frozen evidence does not decide the necessity relation.

This includes cases where:

- \(I\) recurs independently but was never violated;
- a failure exists but is not specifically attributable to \(\neg I\);
- the evidence concerns a different function;
- the evidence concerns a different scope or dependency regime;
- a formal result derives \(I\) but does not prove \(I\) necessary for \(F\);
- the relevant success/failure measurement is absent.

`NOT DEMONSTRATED` is not evidence that \(I\) is unnecessary.

### DISCONFIRMED

Mark `DISCONFIRMED` only when the frozen evidence establishes:

\[
\neg I \land F\text{ still demonstrably succeeds under }D.
\]

A missing observed failure is insufficient.

There must be a positive witness that the specified function succeeds despite the relevant violation under the matched conditions.

## Function- and scope-matching rule

Necessity is typed and local.

Do not transfer necessity across:

- different functions;
- different mechanisms;
- different repositories;
- different operation families;
- different oracle assumptions;
- different interfaces;
- different budgets or horizons;
- different evidence standards;
- different claim ceilings.

A result of the form:

\[
N(I,F,D)
\]

never automatically establishes:

\[
N(I,F',D')
\]

for any broader or adjacent \(F'\) or \(D'\).

## Formal-evidence discipline

Preserve:

\[
\text{formal derivation of }I
\neq
\text{formal necessity of }I\text{ for }F.
\]

A formal counterexample or theorem may support `NECESSARY` only for the exact formal property, function, and scope it actually establishes.

Do not translate a formal result into an empirical or architectural necessity claim.

For example, an SRE counterexample may establish a necessity relation for a declared quotient or future-operation property. It does not establish a general necessity result for corrigibility.

## Failure-evidence discipline

A failure-forced lineage result is not automatically a necessity result.

A failure supports `NECESSARY` only when the frozen evidence specifically links violation of \(I\) to failure of the same \(F\) under \(D\).

Do not use:

- post-hoc thematic explanations;
- adjacent-stage failures;
- generic null results;
- broader architecture failures;
- inherited failures from another mechanism;

as necessity evidence unless the exact \(N(I,F,D)\) relation is already supported.

## Anti-inflation rules

Do not treat:

- recurrence as necessity;
- independent rediscovery as necessity;
- failure-forcing as universal necessity;
- formal derivation as formal necessity;
- usefulness as indispensability;
- design intent as necessity evidence;
- absence of a failure as `DISCONFIRMED`;
- necessity in one bounded architecture as universal necessity.

Preserve:

\[
\text{recurs independently}
\not\Rightarrow
\text{necessary}
\]

and:

\[
\text{necessary under }D
\not\Rightarrow
\text{necessary outside }D.
\]

## Candidate filtering discipline

Do not force all six candidate families into positive audit rows.

For each candidate:

1. identify the exact demonstrated \(F\), if any;
2. identify the exact \(D\);
3. identify an admissible violation condition \(\neg I\), if already evidenced;
4. identify the admissible evidence route;
5. assign the status conservatively.

If any required element is absent, use `NOT DEMONSTRATED`.

Do not fill missing fields by analogy to another repository.

## What this phase must NOT answer

Do not:

- rank invariants;
- construct a “core set”;
- call any invariant universal or fundamental;
- infer a common substrate;
- drop or replace mechanisms;
- reopen substitutability;
- reopen interface compatibility;
- test composition;
- infer cumulative gain;
- optimize complexity;
- construct \(S^\star\);
- open minimization.

A local necessity result is only a preservation requirement for the exact function and conditions tested.

## Output discipline

The primary output is the necessity table.

After the table, provide only a compact aggregate:

1. number of `NECESSARY` local relations;
2. number of `NOT DEMONSTRATED` local relations;
3. number of `DISCONFIRMED` local relations;
4. the exact \(N(I,F,D)\) claims, if any, that earned `NECESSARY`.

Do not rank or combine necessary relations into a proposed architecture.

## Positive result

The strongest admissible positive conclusion is:

> Under the specified conditions, this recurring distinction is demonstrably indispensable to this demonstrated function.

Formally:

\[
\exists(I,F,D):N(I,F,D).
\]

Nothing universal follows.

## Null result

The following is fully admissible:

> Recurrence exists, but no recurring distinction has yet earned necessity under the frozen evidence.

Do not manufacture a necessity result merely to advance Corrigibility Distillation.

## Governing sequence

\[
\text{strongest L2 candidates}
\rightarrow
\text{admissible-evidence filter}
\rightarrow
\text{identify }(I,F,D)
\rightarrow
\text{evaluate violation evidence}
\rightarrow
\text{local necessity verdict}
\rightarrow
\boxed{\text{STOP}}
\]

Never reverse this order.

## Final rule

**Test indispensability locally. Infer nothing universally.**
