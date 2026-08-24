# Revision Propagation Principle

**Status:** `PROGRAM-LEVEL METHODOLOGICAL PRINCIPLE / NOT A NEW MECHANISM / NOT A NEW EXPERIMENT`  
**Scope:** retrospective synthesis over the existing corrigibility / realization lineage  
**Parent program head:** `550a781a9ccc5d708eadb4a3907f182c31cf00b1`  
**RIL-003:** `UNTOUCHED / FROZEN PRE-REVEAL`

## 1. Core distinction

\[
\boxed{
\textbf{epistemic revision}
\not\Rightarrow
\textbf{operational revision}.
}
\]

A system may correctly revise what it believes, warrants, or endorses while continuing to execute behavior derived from an older state.

The compact formulation is:

\[
\boxed{
\textbf{A system can be corrigible in knowledge and stale in action.}
}
\]

This principle does not introduce a new architecture. It separates two questions that must not be conflated:

1. can evidence revise warrant?;
2. can that warranted revision propagate to the behavior that is still being executed?

## 2. Propagation path

A useful schematic path is:

\[
\boxed{
E
\rightarrow
W
\rightarrow
D_{source}
\rightarrow
D_{compiled}
\rightarrow
D_{deployed}
\rightarrow
Y
}
\]

where:

- \(E\) is admissible evidence;
- \(W\) is the current warranted state;
- \(D_{source}\) is the canonical decision representation or source artifact;
- \(D_{compiled}\) is a transformed executable representation;
- \(D_{deployed}\) is the operative deployed decision artifact;
- \(Y\) is observed behavior or consequence.

The labels are diagnostic only. They are not a proposed universal system architecture.

The key non-implication is:

\[
\boxed{
E\rightarrow W'
\not\Rightarrow
D_{deployed}\rightarrow D'_{deployed}.
}
\]

Thus the current authoritative state and current operative behavior may disagree:

\[
\boxed{
W_{current}=W'
\qquad\land\qquad
D_{operative}=D_{old}.
}
\]

## 3. Constitution axis and propagation axis

The existing failure-localization coordinate system is:

\[
\boxed{R\rightarrow S\rightarrow W\rightarrow C\rightarrow Y}
\]

with representation, semantic constitution, admissible warrant, causal control, and consequential change.

That is a **constitution axis**: does a valid path from represented distinction to consequence exist?

The present principle adds a distinct **propagation axis**:

\[
\boxed{
W_{t_1}
\rightarrow
D_{source}
\rightarrow
D_{compiled}
\rightarrow
D_{deployed}
\rightarrow
Y_{t_2}.
}
\]

This asks whether a later warranted revision actually traverses the already-constituted realization path far enough to alter current behavior.

Therefore:

\[
\boxed{
\text{constitution success}
\not\Rightarrow
\text{revision propagation success}.
}
\]

A system may have a valid route from warrant to action in principle yet fail to propagate an updated warrant through stale compiled, cached, replicated, distributed, or deployed descendants.

## 4. All-relevant-operative-descendants condition

Compression and deployment may replicate one warranted decision into many operative descendants:

\[
D\rightarrow\{D_1,\ldots,D_n\}.
\]

Updating the canonical source \(D\) is not sufficient if stale descendants remain behaviorally relevant.

When revision is warranted, each still-relevant operative descendant that depends on the superseded warrant must be placed into at least one of the following states:

\[
\boxed{
\text{updated},
\quad
\text{invalidated},
\quad
\text{or explicitly bounded as stale}.
}
\]

This is a coverage requirement over operative dependence, not a demand for one universal deployment mechanism.

The governing research question is:

\[
\boxed{
\textbf{
Can warranted change propagate through the actual realization graph
far enough to eliminate superseded behavior?
}
}
\]

## 5. Corrigibility refinement

The stronger formulation is:

\[
\boxed{
\textbf{
Corrigibility is not merely the capacity to revise a belief; it is preservation
of a causal path by which warranted revision can reach the behavior still being executed.
}
}
\]

The path need not be instantaneous and need not use a single mechanism. It may involve authorization, source revision, recompilation, rebuilding, artifact distribution, deployment, cache invalidation, model replacement, policy refresh, or other transformations appropriate to the realization.

What matters methodologically is that warranted revision is not trapped upstream of the operative decision surface.

## 6. Relation to compression and revocability

The previously frozen compression/revocability principle states:

\[
\boxed{
\textbf{Compression buys cheap execution. Corrigibility preserves the right to revoke what was compressed.}
}
\]

The present principle makes the third step explicit:

\[
\boxed{
\begin{aligned}
\text{Compression} &: \text{makes execution cheap},\\
\text{Revocability} &: \text{keeps invalidation possible},\\
\text{Propagation} &: \text{makes warranted revision reach execution}.
\end{aligned}
}
\]

These are separate questions.

A system may preserve the epistemic right to revoke a rule while failing to propagate that revocation to all relevant operative descendants.

Therefore:

\[
\boxed{
\text{revocation available in knowledge}
\not\Rightarrow
\text{superseded behavior removed in operation}.
}
\]

## 7. Relation to existing program evidence

This principle is a synthesis across already-separated results. It does not claim one shared mechanism.

### Cognitive Evolution Architecture

CEA provides a direct local witness of the gap:

\[
\text{better internal state}
\not\Rightarrow
\text{changed action}.
\]

The improved predictive/state signal did not enter the operative `choose_action()` path. This is an atomic example of revision failing to reach execution.

### OpenCore / SSI / Cerebro

These lines distinguish evidence, warrant, admission, authority, memory, and causal effect. They show why revising an upstream epistemic object cannot be assumed to alter downstream operative behavior without an independently constituted causal path.

### Admissibility Failure Atlas

The atlas localizes many failures before or at semantic, warrant, identifiability, and causal-path constitution.

The present principle concerns a later failure class:

> even after a path to behavior exists, a revised warrant may fail to propagate through transformed or deployed descendants of the old warrant.

### RIL

RIL demonstrates the positive side: once a function is constituted, representation can alter realization cost. The present principle adds that efficient realization can create additional transformed artifacts whose revision behavior must be considered if validity later changes.

No RIL result is reinterpreted as a propagation experiment.

## 8. Research question

The earned research question is:

> **When revision is warranted, does a causal path actually reach every relevant operative decision that still depends on the superseded warrant, and where does that path first break?**

This question may eventually support empirical tests over compiled code, cached policies, model copies, deployment pipelines, distributed agents, firmware, or other realized decision systems.

No such experiment is opened by this artifact.

## 9. What is deliberately not introduced

This artifact does **not** introduce:

- a scalar revocation-reachability metric;
- a propagation score;
- a new topology ontology;
- a universal deployment graph formalism;
- a dedicated revocation module;
- a claim that all systems require recompilation or redeployment;
- a claim that epistemic and operational revision always diverge;
- a new experiment or benchmark;
- any modification to RIL-003 or its frozen reveal boundary.

The words `constitution axis` and `propagation axis` are diagnostic distinctions only.

## 10. Claim ceiling

This artifact freezes only the following program-level methodological principle:

\[
\boxed{
\textbf{
When revision is warranted, evidence must retain an admissible causal route
through the transformations that separate current warrant from current execution.
}
}
\]

If a superseded warrant has produced multiple still-relevant operative descendants, revising the canonical belief or source artifact is insufficient unless those descendants are updated, invalidated, or explicitly bounded as stale.

The shortest formulation remains:

\[
\boxed{
\textbf{A system can be corrigible in knowledge and stale in action.}
}
\]
