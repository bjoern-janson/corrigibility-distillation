# Codex Instructions

## Purpose

This repository is for **Corrigibility Distillation**.

Phase 1 inventory is complete.

Phase 2 substitutability analysis is complete.

Current status:

\[
\text{L2: shared functions/invariants}\quad\checkmark
\]

\[
\text{L3: substitutability}\quad 0/182
\]

\[
\text{L4: interface compatibility}\quad\textbf{ACTIVE}
\]

\[
\text{L5: composition}\quad\textbf{CLOSED}
\]

\[
\text{L6: cumulative gain}\quad\textbf{CLOSED}
\]

L4 is a **pure interface audit**.

The only active question is:

> Does an output already produced by one existing mechanism already satisfy an input required by another existing mechanism?

Do not design a common interface.

## Frozen evidence base

Use only the completed Phase-1 inventory and completed Phase-2 comparison as the evidence base.

Treat Phase-1 and Phase-2 records as authoritative only for the facts they explicitly contain. Do not infer an output/input role from a descriptive phrase unless that role is explicitly present in the frozen record.

Do not reread source repositories to:

- add evidence
- repair inventory rows
- strengthen claims
- reinterpret mechanisms
- infer new interfaces
- introduce missing semantics

If the frozen evidence base is insufficient, record the limitation.

Do not repair it during L4.

## L4 deliverable

Use:

| Mechanism A | Output type/function | Mechanism B | Required input/function | Existing interface evidence | Compatible? |
|---|---|---|---|---|---|

`Compatible?` must be one of:

- `YES`
- `NO`
- `PARTIAL`

## Interface relation

Treat interface compatibility as directional.

\[
M_A\leadsto M_B
\]

means an output already produced by \(M_A\) is already admissible as an input required by \(M_B\).

Formally, compatibility requires an already-supported mapping:

\[
\phi_{AB}:Y_A\rightarrow X_B.
\]

The mapping must already be supported by the frozen corpus.

Do not invent it.

## Hard boundary

L4 may discover existing interface edges.

It may not create them.

Do not introduce:

- adapters
- translation layers
- bridge mechanisms
- common schemas
- shared buses
- common handles
- new semantic mappings
- new authority mappings
- new operation signatures
- hidden state
- new mechanisms
- new functions
- new invariants
- proposed architectures

If compatibility would require any such construction, record:

> Interface gap: no existing supported mapping.

That is `NO`, not a design task.

## Compatibility criteria

Mark `YES` only when the frozen evidence already establishes that:

1. \(M_A\) produces the relevant output;
2. \(M_B\) requires or accepts the relevant input;
3. the output and input have matching meaning, not merely matching representation;
4. any required authority or admissibility conditions are already satisfied;
5. no new adapter, oracle, interpretation, state, or transformation is required.

The compatibility must be evidenced as an actual relation in the frozen record, not merely reconstructed by interpreting two descriptions as semantically equivalent.

Otherwise mark `NO` or `PARTIAL`.

## PARTIAL

`PARTIAL` means:

> A specific, explicitly identified, bounded output/input relation is already supported, while broader mechanism-to-mechanism compatibility is not demonstrated.

Always state the exact bounded relation.

Do not use `PARTIAL` for:

- thematic similarity
- adjacent stages
- shared vocabulary
- plausible future integration
- same datatype
- inferred compatibility

## Anti-collapse rules

Preserve:

\[
\text{datatype match}
\neq
\text{semantic match}
\]

\[
\text{semantic compatibility}
\neq
\text{authority compatibility}
\]

\[
M_A\leadsto M_B
\neq
M_B\leadsto M_A
\]

\[
M_A\leadsto M_B
\neq
M_B\circ M_A
\]

\[
\text{pairwise compatible edges}
\neq
\text{common interface}
\]

\[
\text{adjacent functions}
\neq
\text{demonstrated interface}
\]

Do not collapse these distinctions.

## No composition

L4 does not test whether compatible mechanisms work correctly when composed.

A demonstrated interface edge establishes only:

\[
M_A\leadsto M_B.
\]

It does not establish:

\[
M_B\circ M_A.
\]

Do not:

- execute compositions
- infer path behavior
- infer end-to-end correction
- infer invariant preservation across a chain
- infer cumulative performance gain

Those belong to later phases.

## No common handle

Multiple interface edges do not establish a universal interface.

For example:

\[
M_1\leadsto M_2
\]

and:

\[
M_3\leadsto M_4
\]

do not imply the existence of a shared interface \(\mathcal I\).

Do not synthesize a common socket, handle, protocol, schema, or substrate from pairwise similarities.

L4 discovers sockets that already exist.

It does not design the handle.

## Evidence discipline

Preserve all existing claim ceilings and dependency limits.

Do not transfer evidence between repositories.

Do not promote:

- proposed to implemented
- implemented to demonstrated
- formal to empirical
- local compatibility to general compatibility
- interface compatibility to composition

A missing mapping is evidence of an interface gap under the frozen corpus, not evidence that no mapping could ever exist.

## Directionality

Check directions independently.

\[
M_A\leadsto M_B
\]

does not imply:

\[
M_B\leadsto M_A.
\]

Do not infer transitivity.

\[
M_A\leadsto M_B
\quad\land\quad
M_B\leadsto M_C
\]

does not establish:

\[
M_A\leadsto M_C.
\]

Each edge must be directly supported.

## Null result

The following is a valid L4 result:

> Shared functions and invariants exist, but no existing mechanism output is demonstrated to satisfy another mechanism's required input.

If so:

\[
\boxed{
\text{L4 compatible edges}=0
}
\]

and L5 remains closed.

Do not manufacture compatibility to preserve the modular-tool hypothesis.

## Positive result

If one or more compatible edges are demonstrated, record only those exact edges.

A positive L4 result earns the statement:

> The frozen corpus contains specific complementary mechanisms with demonstrated interface compatibility.

It does not earn:

- a common architecture
- a universal interface
- valid composition
- cumulative gain
- minimization

## Governing sequence

\[
\text{existing frozen corpus}
\rightarrow
\text{output/input audit}
\rightarrow
\text{existing interface evidence}
\rightarrow
\text{compatibility judgment}
\rightarrow
\boxed{\text{STOP}}
\]

Never reverse this order.

## Final rule

**Audit the sockets. Do not invent the handle.**
