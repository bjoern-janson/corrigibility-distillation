# RG-001 — Realization Geometry Cost/Robustness Preregistration

Status: **PROSPECTIVE; PARALLEL LANE; NO RELATION TO RIL-003 TARGET SELECTION OR EXECUTION**

Branch: `rg-001-realization-geometry`

Parent branch point: `fd30d9996db5b82652c208a0d29ab9fff0aca523`

## 1. Scientific purpose

RG-001 is a deliberately separate existence assay for the provisional realization-geometry coordinate system. It asks whether two distinct realizers of the same fixed function can occupy different positions on more than one coordinate while preserving function identity.

The provisional coordinate object is only:

\[
\Gamma_F(r)=(V_F,C_F,B_F,A_F).
\]

RG-001 measures only `V`, `C`, and `B`. `A` is not tested.

Nothing in RG-001 may alter, reinterpret, parameterize, select, reveal, or execute any part of RIL-003. No RIL-003 target, Beacon output, SEM8 modification, FS007 result, or RIL-003 apparatus output is admissible input to RG-001.

## 2. Fixed function F

The exact function is 12-bit parity:

\[
F(x)=\left(\sum_{k=0}^{11} ((x\gg k)\&1)\right)\bmod 2,
\qquad x\in\{0,\ldots,4095\}.
\]

Reference semantics are defined independently by Python integer popcount:

```text
F_ref(x) = x.bit_count() & 1
```

The reference is used only for validity/robustness adjudication, never inside either measured realizer.

The complete finite domain of 4096 inputs is mandatory for every validity or robustness claim.

## 3. Shared substrate

Both realizers receive the same substrate contract:

```text
input domain                 integers 0..4095
output domain                {0,1}
reserved auxiliary memory    exactly 64 bytes
memory type                  bytearray
precision                    exact integer / bit operations
parallelism                  none
vectorization                none
memoization across calls     none except frozen auxiliary payload below
JIT                          forbidden
external libraries           forbidden for operative realization
```

The 64-byte reserved region exists for both realizers. `r0` ignores it during prediction. `r1` uses it as its operative representation.

Memory allocation size is therefore held fixed; information content/use is allowed to differ because that difference is the realization intervention.

## 4. Frozen realizers

### r0 = LOOP12

Construction:

```text
allocate bytearray(64), initialized to zero
```

Prediction:

```python
p = 0
v = x
for _ in range(12):
    p ^= v & 1
    v >>= 1
return p
```

The reserved 64-byte region is not read during prediction.

### r1 = LUT6

Construction:

```text
allocate bytearray(64)
for i in 0..63:
    compute 6-bit parity using an explicit six-iteration bit loop
    store that parity bit in memory[i]
```

No `bit_count`, table literal, imported lookup, precomputed blob, generated code, or external library may construct the payload.

Prediction:

```python
lo = x & 0x3F
hi = (x >> 6) & 0x3F
return (memory[lo] & 1) ^ (memory[hi] & 1)
```

The `& 1` read mask is part of the frozen realizer and may not be removed after preregistration.

## 5. Validity coordinate V

For each realizer `r_i`,

\[
V_F(r_i)=1
\]

iff for every integer `x` in `0..4095`:

```text
predict_i(x) == F_ref(x)
```

Validity is noncompensatory:

```text
V_i = 0
=> no cost or robustness result may be interpreted as a successful realization of F.
```

## 6. Cost coordinate C

Primary cost is **executed Python bytecode instructions internal to the realizer**, counted with CPython opcode tracing (`sys.settrace` + `frame.f_trace_opcodes = True`).

Counted regions are exactly:

```text
construction code for the realizer
prediction function body for one exhaustive ordered sweep x=0..4095
```

The shared harness loop, reference function, tracer implementation, result serialization, assertions, and robustness execution are not counted in `C`.

Construction is included once. Prediction is included exactly once per input in ascending order.

No timing claim is primary.

Let:

\[
C_i=C_F(r_i).
\]

Primary cost contrast:

\[
\Lambda_C = C_0/C_1.
\]

Cost leverage is demonstrated only if:

```text
V0 = V1 = 1
and
C1 < C0
```

No minimum speedup magnitude is preregistered.

## 7. Robustness coordinate B

The shared perturbation universe is the same for both realizers:

\[
\Delta=\{(j,b):0\le j<64,\ 0\le b<8\},
\]

exactly 512 single-bit corruption events in the reserved auxiliary-memory region.

For perturbation `delta=(j,b)`:

1. build a clean realization;
2. flip exactly `memory[j] ^= (1 << b)`;
3. do not repair or rebuild;
4. evaluate the complete 4096-input domain;
5. record whether all outputs still equal `F_ref`.

Define:

\[
B_F(r_i)=\{\delta\in\Delta:\forall x,\ r_i^{\delta}(x)=F(x)\}.
\]

Report the exact set cardinality and the full 512-bit pass/fail vector in canonical perturbation order:

```text
(j=0,b=0..7), (j=1,b=0..7), ..., (j=63,b=0..7)
```

Robustness comparison is set-based. A strict loss is demonstrated only if:

\[
B_F(r_1)\subsetneq B_F(r_0).
\]

No stochastic fault model or probability interpretation is allowed.

## 8. Primary scientific object

The primary record is:

\[
\bigl(V_0,C_0,B_0;\ V_1,C_1,B_1\bigr)
\]

plus the exact perturbation vectors.

The most interesting preregistered pattern is:

\[
V_0=V_1=1,
\qquad
C_1<C_0,
\qquad
B_1\subsetneq B_0.
\]

This would be a bounded existence witness that realization coordinates can trade off: cheaper does not imply at-least-as-robust.

## 9. Outcome taxonomy

```text
NOT_EVALUABLE
    frozen implementation/cost/fault contract cannot be faithfully instantiated

INVALID_REALIZER
    V0=0 or V1=0

NO_COST_SEPARATION
    V0=V1=1 but C1>=C0

COST_ONLY
    V0=V1=1, C1<C0, but B1 is not a strict subset of B0

COST_ROBUSTNESS_TRADEOFF
    V0=V1=1, C1<C0, and B1 is a strict subset of B0
```

Unexpected robustness relations must be reported as observed; do not coerce them into the taxonomy narrative.

## 10. Claim ceiling

Maximum positive claim:

> **Under the exact frozen 12-bit parity function, CPython opcode-cost contract, two frozen realizers, and one-bit auxiliary-memory fault model, RG-001 demonstrates a bounded cost/robustness separation between two valid realizations of the same function.**

RG-001 cannot establish:

```text
realization geometry as a general theory
representation-induced generality
biological affordance migration
environmental autonomy
natural evolutionary tradeoffs
hardware-independent cost relations
robustness outside the frozen single-bit auxiliary-memory fault model
any result about RIL-003
```

## 11. Execution order

Mandatory order:

```text
preregistration freeze
-> implementation
-> implementation freeze
-> pre-execution audit
-> validity
-> cost
-> robustness
-> result
-> final audit
-> STOP
```

No primary result may be inspected before the implementation freeze.

## 12. Lane-separation firewall

RG-001 must remain on `rg-001-realization-geometry` unless explicitly merged later for archival reasons.

Forbidden RG-001 inputs:

```text
RIL-003 Beacon pulse
RIL-003 target IDs or truth tables
RIL-003 target manifest
RIL-003 preservation/cost results
any post-preregistration modification of SEM8 motivated by RG-001
```

Forbidden backward effects:

```text
no change to RIL_003_PREREGISTRATION.md
no change to RIL_003_GENERATOR_CONTRACT.json
no change to experiments/ril_003/*
no change to RIL-003 target selection
no change to RIL-003 interpretation criteria
```

RG-001 is independent evidence only.
