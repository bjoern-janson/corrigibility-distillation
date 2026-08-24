# RD-001 — Terminal Lesson

**Status:** `TERMINAL INTERPRETATION / AVAILABLE_LEVERAGE_DEMONSTRATED / LEARNER_TARGET_CLASS_MISMATCH / TRAINING NOT OPENED / SUCCESSOR NOT OPENED`

**Experiment:** `RD-001`  
**Parent state:** `dadf0686477641737e10b25cfae9ed239b4c0409`  
**Preregistration:** `bb0a85182a59a498568fa2905a49802af35b56b4`  
**Frozen calibration result:** `d2df78ada3642cd33a543360cb5218bda7892e30`  
**Learner-target compatibility audit:** `dadf0686477641737e10b25cfae9ed239b4c0409`  
**RIL-003:** `UNTOUCHED / FROZEN PRE-REVEAL`

This artifact freezes the interpretation of RD-001 after the successful oracle calibration and the subsequent pre-training learner-target compatibility audit.

It opens no successor experiment, defines no new generator, designs no learner, consumes no training beacon, materializes no `Q_train`, and generates no held-out test data.

---

## 1. The three distinctions RD-001 must not collapse

RD-001 separates three scientific objects:

\[
\boxed{
\text{oracle leverage}
\neq
\text{reusable representation}
\neq
\text{learnable representation}.
}
\]

They answer different questions.

### Oracle leverage

Does there exist an admissible representation for a realized instance that reduces solving cost while preserving the required future behavior?

### Reusable representation

Does one representation or representation rule remain valid across the family of fresh instances over which reuse is claimed?

### Learnable representation

Does the frozen learner hypothesis class contain such a reusable representation, and can the acquisition procedure identify it from admissible training information?

No implication among these three is granted without separate evidence.

---

## 2. What RD-001 positively demonstrated

The frozen 24-instance calibration established:

```text
R_STAR exact native correctness          = 24 / 24
R_STAR designated trap preservation      = 24 / 24
fresh-cost wins R_STAR < R0              = 24 / 24
sum C_fresh(R0)                           = 2,093,094
sum C_fresh(R_STAR)                       = 1,134,901
aggregate fresh leverage                  = 1.844296550976693
```

The structural diagnostic also showed:

```text
sum exact native structural states        = 44,352
sum exact R_STAR structural states        = 9,912
sum C_search(R0)                           = 2,090,739
sum C_search(R_STAR)                       = 1,132,382
```

Therefore the calibration earned the bounded positive result:

\[
\boxed{
\textbf{
Under the frozen RD-001 calibration, an evaluator-supplied future-preserving
structural representation produced structural compression and lower exhaustive
fresh-instance search cost on all 24 realized calibration instances.
}
}
\]

Equivalently, for every calibration instance `i`:

\[
\boxed{
P(R_\star^{(i)})=1
\quad\land\quad
C_{fresh}(R_\star^{(i)})<C_{fresh}(R_0^{(i)}).
}
\]

This remains a positive empirical result.

The later learner-target audit does not revoke or rewrite it.

---

## 3. What the oracle actually was

The implemented generator chooses a hidden relevant descriptor subset separately for each realized instance:

\[
J_i\subseteq\{0,1,2,3\},
\qquad |J_i|\in\{1,2\}.
\]

The evaluator-side oracle receives that instance-specific value and constructs:

\[
\boxed{
R_\star(X_i)=R_{J_i}(X_i).
}
\]

The frozen calibration confirms that `J_i` genuinely varies across instances. Examples include:

```text
instance 0: J = {0,1}
instance 1: J = {0,3}
instance 2: J = {3}
instance 4: J = {1,2}
```

Thus the observed oracle leverage is leverage from a **family of instance-conditioned representations**.

The correct interpretation is therefore:

\[
\boxed{
\textbf{RD-001 demonstrated instance-specific representational leverage.}
}
\]

It did not demonstrate one family-wide reusable coordinate system.

---

## 4. What the preregistered learner was allowed to be

The frozen `R_L` output language permits one prospectively frozen token-classification / canonicalization schema applied to future instances.

Its artifact may contain:

- one global partition of the 16 four-bit descriptor values;
- identity-retention choices within learned classes;
- deterministic class labels;
- deterministic state-key canonicalization based on those learned classes.

It may not contain post-test repair, test-specific tables, target IDs, action recommendations, test-state heuristics, or arbitrary executable search logic.

For the proposed minimal coordinate learner, this would have reduced to a fixed descriptor projection:

\[
\boxed{
R_L(X)=R_K(X)
}
\]

for one frozen:

\[
K\subseteq\{0,1,2,3\}.
\]

That is not the same adaptation class as:

\[
R_\star(X_i)=R_{J_i}(X_i)
\]

when `J_i` changes with the instance.

Hence:

\[
\boxed{
R_\star\text{ works}
\not\Rightarrow
R_L\text{ can express what }R_\star\text{ does}.
}
\]

---

## 5. The failure localized before learning

The intended sequence was:

\[
\text{available geometry}
\rightarrow
\text{learner target}
\rightarrow
\text{learner acquisition}
\rightarrow
\text{held-out evaluation}.
\]

RD-001 stopped at the second transition:

\[
\boxed{
\text{available geometry}
\rightarrow
\textbf{target-class mismatch}
\rightarrow
\text{learner not opened}.
}
\]

The frozen audit verdict is:

```text
LEARNER_TARGET_CLASS_MISMATCH / TRAINING_NOT_OPENED
```

No learner failure occurred because no learner was designed or run.

No representation-acquisition claim was tested.

No `Q_train` beacon was consumed.

No `Q_train` suite was materialized.

No test seed exists.

No held-out test lane was opened.

The negative result is therefore at the **experiment-object constitution layer**, not at the learner-performance layer.

---

## 6. Why a fixed learner cannot simply be declared to recover the oracle

Under the frozen generator support, any descriptor coordinate may become consequential on a future instance.

If a global learner permanently omits coordinate `j`, there exist admissible future family realizations in which native transitions depend on `j`.

Therefore:

\[
\boxed{
\text{safe to forget on one realized instance}
\not\Rightarrow
\text{safe to forget across the family}.
}
\]

A globally conservative descriptor projection may retain all four bits, but that no longer reproduces the instance-specific irrelevant-bit deletion used by `R_STAR`.

Whether any residual globally reusable compression exists in the already frozen RD-001 learner language is unmeasured and is not inferred from the oracle calibration.

---

## 7. The methodological lesson

The strongest lesson is:

\[
\boxed{
\textbf{
Before asking whether a system can learn a representation, make sure the
representation to be learned is actually the same object across the worlds in
which learning and transfer are claimed.
}
}
\]

A shorter compression is:

\[
\boxed{
\textbf{A demonstrated oracle advantage is not automatically a learnable target.}
}
\]

And the structural non-equivalence is:

\[
\boxed{
\text{instance-conditioned useful coordinates}
\neq
\text{reusable coordinates}
\neq
\text{coordinates inside the learner hypothesis class}.
}
\]

This is another instance of the program's standing rule:

\[
\boxed{
\textbf{Do not cross an unearned transition merely because the objects on both sides look related.}
}
\]

---

## 8. Why RD-001 must not be repaired post hoc

RD-001 must not be rewritten so that the generator uses one family-wide latent `J` merely because the mismatch became visible after the positive calibration.

Such a change would transform a post-result observation into a purported preregistered property.

Therefore the following are forbidden inside RD-001:

- changing per-instance `J_i` into one family-wide `J*`;
- redefining `R_STAR` to make it match the desired learner class;
- widening `R_L` after seeing the calibration result;
- materializing training data and then choosing the learner hypothesis class;
- treating the 1.844296550976693 oracle leverage as the ceiling recoverable by the frozen global learner;
- relabeling the positive calibration as reusable or learned leverage.

RD-001 remains historically intact.

---

## 9. Current state freeze

```text
RD-001 PREREGISTRATION                 = FROZEN
V1 IMPLEMENTATION                      = PRESERVED / PRE-CALIBRATION AUDIT FAIL / RETIRED
V2 IMPLEMENTATION                      = FROZEN
V2 SEMANTIC AUDIT                      = PASS
CALIBRATION BEACON / SEED / MANIFEST   = FROZEN
R0 vs R_STAR CALIBRATION               = RUN
AVAILABLE_LEVERAGE                     = DEMONSTRATED
CALIBRATION INTERPRETATION             = INSTANCE-SPECIFIC ORACLE LEVERAGE
PUBLICATION-ORDER DEVIATION             = DISCLOSED
LEARNER TARGET COMPATIBILITY           = FAIL
R_L LEARNER SPECIFICATION              = NOT FROZEN
Q_TRAIN BEACON                         = NOT CONSUMED
Q_TRAIN                                = NOT MATERIALIZED
R_L ACQUISITION                        = NOT RUN
TEST SEED                              = UNAVAILABLE BY DESIGN
TEST INSTANCES                         = NOT GENERATED
SUCCESSOR EXPERIMENT                   = NOT OPENED
```

The two RD-001 verdicts must coexist:

```text
AVAILABLE_LEVERAGE_DEMONSTRATED
LEARNER_TARGET_CLASS_MISMATCH / TRAINING_NOT_OPENED
```

The second narrows the scope of the first; it does not erase it.

---

## 10. Possible future scientific ladder — not opened

A clean future program could separate the following questions:

\[
\boxed{
\begin{aligned}
RD\text{-}001 &: \text{instance-specific useful coordinates exist},\\
RD\text{-}002 &: \text{a reusable coordinate system exists},\\
RD\text{-}003 &: \text{a learner discovers it prospectively},\\
RD\text{-}004 &: \text{the acquired representation pays back its acquisition cost},\\
RD\text{-}005 &: \text{the learned coordinate system transfers to a new family}.
\end{aligned}
}
\]

This ladder is recorded only as a **possible decomposition of future questions**.

No identifier after RD-001 is opened, preregistered, implemented, or authorized by this artifact.

In particular:

```text
RD-002 = NOT OPENED
RD-003 = NOT OPENED
RD-004 = NOT OPENED
RD-005 = NOT OPENED
```

Any successor requires a fresh scientific object, fresh preregistration, and fresh prospective boundary.

---

## 11. Terminal RD-001 interpretation

RD-001 began by asking whether a finite planning family contained useful representation-induced discovery leverage before asking a learner to discover it.

The calibration answered a narrower but genuine existence question positively:

\[
\boxed{
\textbf{Useful future-preserving coordinates existed for each realized calibration instance.}
}
\]

The learner-target audit then showed that those oracle coordinates were not one reusable object inside the preregistered learner's global hypothesis class.

Therefore the correct final compression is:

\[
\boxed{
\textbf{
RD-001 found useful geometry, then stopped before pretending that
instance-specific geometry was a reusable learnable representation.
}
}
\]

That stop is part of the result.
