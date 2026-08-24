# Codex Instructions

## Purpose

Phase 1 inventory, Phase 2 substitutability, and L4 interface audit are complete.

Current state:

L2 = recurring functions/invariants  
L3 = 0/182 substitutions  
L4 = 0 full mechanism interfaces  
L4' = 1 bounded evidence/provenance transport  
L5 = CLOSED  
L6 = CLOSED  
MINIMIZATION = CLOSED

The active phase is:

## L2 LINEAGE AUDIT

The only question is:

> Which recurring functions/invariants were inherited, independently
> rediscovered, failure-forced, or formally derived?

Do not perform minimization, architecture design, composition, or necessity analysis.

## Frozen evidence base

Use only the completed Phase-1 inventory and already-recorded Phase-2/L4 records.

Do not add new corpus elements.

Do not infer an invariant merely because repositories use similar language.

## Deliverable

Use:

| Function / Invariant | Repo | Inherited? | Independent evidence? | Failure-forced? | Formally derived? | Strongest earned status |
|---|---|---|---|---|---|---|

Each provenance property is assessed per `(Function/Invariant, Repo)` pair.

They are not mutually exclusive.

An invariant may be:
- inherited in one repository;
- independently rediscovered in another;
- failure-forced in another;
- formally derived in another.

Do not aggregate these into a single global label.

## Provenance definitions

### Inherited

Mark only when the repository explicitly carries the distinction forward
from an earlier research result.

Do not infer inheritance merely from chronological similarity.

### Independently rediscovered

Mark only when the repository reaches the same function/invariant through
a distinct mechanism or evidence path without relying on the earlier result.

Independent means independent in evidentiary origin, not merely appearing in
a different file or repository.

### Failure-forced

Mark only when an observed failure, counterexample, null result, or failed
assumption specifically forced the distinction to be introduced or retained.

### Formally derived

Mark only when the distinction follows from an explicit formal result,
proof, theorem, or mathematically necessary construction already present
in the frozen record.

## Anti-inflation rules

Do not treat:

- shared vocabulary as independence;
- repeated inheritance as independent rediscovery;
- implementation coincidence as an invariant;
- a proposed invariant as an earned invariant;
- a useful design choice as a failure-forced invariant;
- a post-hoc explanation as a failure-forced result.

If evidence is insufficient, record:

`NOT DEMONSTRATED`

rather than inferring a category.

## What this phase must NOT answer

Do not ask whether an invariant is necessary.

Do not ask whether removing it breaks a function.

Do not construct ablations.

Do not propose a minimal substrate.

Do not group mechanisms into an architecture.

Do not infer universal corrigibility principles.

Those belong to later phases.

## Output discipline

The primary output is the per-repository lineage table.

After the table, provide only a compact aggregate showing:

1. which functions/invariants recur across multiple repositories;
2. which of those have at least one independently rediscovered instance;
3. which have failure-forced instances;
4. which have formal-derivation instances.

Do not call any invariant “fundamental,” “necessary,” or “universal.”

## Null result

A valid result is:

> Apparent recurrence is predominantly inherited or genealogical, with little or no independent rediscovery.

That is a result, not a failure.

## Governing sequence

\[
\text{recurrence}
\rightarrow
\text{lineage attribution}
\rightarrow
\text{independence assessment}
\rightarrow
\text{earned recurrence}
\]

Then STOP.

## Final rule

**Trace why the distinction exists. Do not decide yet whether it must exist.**
