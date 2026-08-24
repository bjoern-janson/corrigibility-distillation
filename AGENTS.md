# Codex Instructions

## Purpose

This repository is for **Corrigibility Distillation**.

Phase 1 is complete.

Phase 2 is **comparison only** over the fixed 14-row Phase-1 inventory.

The active question is:

> Which existing things can actually replace other existing things?

Do not design a final system.

## Phase 2 input

Use only the completed Phase-1 inventory:

| Repo | Mechanisms | Functions | Invariants | Claim Ceiling | Dependency Limit |
|---|---|---|---|---|---|

Treat those 14 rows as the complete and immutable Phase-2 evidence base.

Do not add new mechanisms, functions, invariants, claims, dependencies, repositories, or theoretical objects during comparison.

Do **not** reread source repositories to add, correct, strengthen, or reinterpret Phase-1 entries. If an inventory row appears incomplete or ambiguous, record the limitation rather than repairing it from source material during Phase 2.

Source repositories may be consulted only to verify an existing citation or reference. They do not become a new Phase-2 evidence stream.

## Phase 2 deliverable

Use:

| Repo A | Repo B | Mechanism overlap | Function overlap | Invariant overlap | Claim/dependency conflict | Substitutability |
|---|---|---|---|---|---|---|

`Substitutability` must be one of:

- `YES`
- `NO`
- `PARTIAL`

## Hard boundary

Phase 2 may relate existing inventory entries.

It may not create new corpus elements.

Do not introduce:

- candidate architectures
- distilled substrates
- missing components
- new mechanisms
- new functions
- new invariants
- new operation signatures
- new theories
- optimization targets
- proposed final systems

Do not reinterpret comparison as synthesis.

## Comparison rules

Preserve:

\[
\text{mechanism overlap}
\neq
\text{mechanism equivalence}
\]

\[
\text{function overlap}
\neq
\text{substitutability}
\]

\[
\text{invariant overlap}
\neq
\text{shared mechanism}
\]

\[
\text{shared vocabulary}
\neq
\text{shared evidence}
\]

Similarity of language is not evidence of substitutability.

## Substitutability rule

Treat substitutability as **directional**.

\[
R_A \rightsquigarrow R_B
\]

does not imply:

\[
R_B \rightsquigarrow R_A.
\]

If the two directions differ, record them separately.

A substitution may be marked `YES` only when the relevant demonstrated functions and invariants of the replaced item survive under the replacement without requiring a stronger unavailable dependency or exceeding the replacement's earned claim ceiling.

`PARTIAL` means a specific, explicitly identified function, invariant, or scope is substitutable, while the repository or mechanism as a whole is not shown substitutable.

Otherwise mark it `NO`.

Do not infer repository-level substitution from a local substitution.

## Typed substitution

Every substitution judgment is implicitly relative to:

\[
(F_R,I_R,\Omega,D)
\]

where applicable.

Do not generalize a substitution beyond the exact function, invariant, operation family, scope, and dependency conditions supported by the inventory.

Do not infer transitivity.

\[
R_A\rightsquigarrow R_B
\quad\land\quad
R_B\rightsquigarrow R_C
\]

does not establish:

\[
R_A\rightsquigarrow R_C.
\]

Check each relation directly.

## Claim and dependency discipline

A replacement is not valid merely because it appears more capable.

Check both:

**Claim Ceiling**  
Does the replacement's earned evidence justify the exact function or invariant being substituted?

For a valid directional substitution:

\[
R_A\rightsquigarrow R_B
\Rightarrow
C_B \succeq C_A
\]

only for the substituted claim and under the same stated conditions.

The replacement does **not** need a globally stronger evidence record. It needs an earned claim ceiling sufficient for the exact thing being replaced.

**Dependency Limit**  
Does the replacement require assumptions, oracles, interfaces, fixed families, budgets, horizons, supplied structures, or other conditions that make the proposed substitution invalid?

Do not silently strengthen either repository's claim.

Do not erase dependency differences to manufacture equivalence.

## Evidence discipline

Preserve the Phase-1 distinctions between:

- proposed vs implemented
- implemented vs demonstrated
- formal vs empirical
- positive vs negative/null evidence
- apparatus result vs scientific result
- inherited distinction vs independently earned result

A proposed mechanism cannot substitute for an empirically demonstrated mechanism merely because their descriptions align.

A formal result cannot automatically substitute for an empirical mechanism.

A negative result cannot be converted into a positive capability claim.

## Overlap discipline

Record overlap only when the Phase-1 inventory actually supports it.

Prefer narrow descriptions.

For example:

> both perform bounded candidate filtering

is preferable to:

> both implement corrective search

unless the broader relation is explicitly earned.

Do not normalize terminology merely to increase apparent overlap.

## Redundancy boundary

Do not call anything redundant merely because overlap exists.

Redundancy is not earned until substitutability is demonstrated.

\[
\text{overlap}
\not\Rightarrow
\text{redundancy}.
\]

A `NO` result is fully admissible.

A corpus with recurring functions or invariants but no valid substitutions is a valid Phase-2 outcome.

## Minimization remains closed

Do not:

- minimize the corpus
- choose preferred mechanisms
- remove repositories
- propose a minimal faithful realization
- optimize complexity
- design the student
- infer the final corrigibility substrate

Those operations occur only after Phase 2 is complete and redundancy has been earned.

## Phase 2 sequence

\[
\text{existing inventory}
\rightarrow
\text{overlap}
\rightarrow
\text{substitutability}
\rightarrow
\text{earned redundancy}
\]

Do not reverse this order.

## Null result

The following is a valid Phase-2 conclusion:

> Shared functions and recurring invariants were observed, but no meaningful mechanism-level substitutability was demonstrated.

Do not force substitutions merely to make later distillation possible.

## Final rule

**Compare what already exists. Replace only what the evidence permits. Minimize nothing yet.**
