# Codex Instructions

## Purpose

This repository is for **Corrigibility Distillation**.

Phase 1 is **reconstructive inventory only**: describe what already exists across the prior research corpus.

The phase-1 deliverable is:

| Repo | Mechanisms | Functions | Invariants | Claim Ceiling | Dependency Limit |
|---|---|---|---|---|---|

## Hard boundary

Do **not** invent, propose, infer, or synthesize a corrective architecture during Phase 1.

Do not create:
- candidate substrates
- missing components
- new mechanisms
- new invariants
- new functions
- unearned theory
- cross-repository abstractions presented as established facts

A component may enter the inventory only when it is concretely instantiated or demonstrably earned by the source repository.

## Extraction rule

For each repository, record only:

**Mechanisms**
What was actually implemented, constructed, or experimentally exercised.

**Functions**
What transformation or capability the mechanism actually performed.

**Invariants**
Properties or distinctions actually preserved, demonstrated, or formally earned.

**Claim Ceiling**
The strongest claim justified by the repository's evidence.

**Dependency Limit**
Conditions, assumptions, oracle requirements, fixed families, horizons, budgets, interfaces, or other restrictions without which the claim does not hold.

Do not silently strengthen any claim.

## Evidence discipline

Preserve the distinction between:
- implemented vs proposed
- measured vs inferred
- demonstrated vs assumed
- independently rediscovered vs inherited
- positive result vs negative result
- scientific result vs apparatus result

A failed experiment is still evidence when its failure boundary is informative.

Do not reinterpret a negative result as support for a preferred theory.

## Repository parsing

Read repositories in chronological order where possible.

Use the repository's actual:
- source
- experiment specifications
- executable code
- audits
- results
- frozen commits

as the primary evidence.

Do not rely on memory or summaries when the source repository is available.

## Claim compression

Compress descriptions, but do not remove distinctions that would change the earned claim.

The goal is a compact inventory, not a chronological transcript.

## No distillation yet

Phase 1 ends with the inventory.

Only after the inventory is complete may the project proceed to:

1. compare mechanisms/functions/invariants;
2. test substitutability and redundancy;
3. construct a minimal faithful realization.

If a supposedly necessary component is absent from the corpus, do **not** add it.

Instead record:

> Distillation gap: unsupported by current corpus.

That becomes a future research question.

## Null result

The following is a valid outcome:

> No materially smaller faithful realization exists.

Do not force a unifying structure merely because one is aesthetically appealing.

## Governing sequence

\[
\text{extract}
\rightarrow
\text{compare}
\rightarrow
\text{test substitutability}
\rightarrow
\text{minimize}
\]

Never reverse this order.

## Final rule

**Distill what already exists. Do not invent what seems necessary.**
