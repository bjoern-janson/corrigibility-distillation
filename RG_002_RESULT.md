# RG-002 — Terminal Result

Status: **COST_ROBUSTNESS_TRADEOFF — CLOSED**

## Frozen anchors

```text
RG-001 terminal null    ce4aac5f2deb9f8ce37fb7298019f936a373e055
RG-002 preregistration  378158466309b391b5b79e0e2c5c691ae991e786
RG-002 implementation   985b65be7db964a8959d3b276080aacb8864da90
pre-execution audit     e712e2b572af47d5fe99462dd1253514a6a0e10a
RG-001 realizer blob    9a074faf9579e57060de7f1df10093c2a080b8a3
```

RG-002 is an instrumentation-repair assay, not an independent replication. The scientific function, realizers, substrate, and fault model were selected/frozen in RG-001 before its primary cost attempt. RG-002 changes only the tracer activation needed to count the already-preregistered construction region.

## Validity V

Both realizers matched the independent 12-bit parity reference on the complete finite domain:

```text
R0_LOOP12  4096/4096 exact, mismatch_count=0
R1_LUT6    4096/4096 exact, mismatch_count=0
```

Therefore:

\[
\boxed{V_0=V_1=1}.
\]

## Cost C

Primary deterministic CPython 3.13.5 opcode counts:

| Region | R0 LOOP12 | R1 LUT6 |
|---|---:|---:|
| construction | 6 | 5,837 |
| 4,096 predictions | 634,880 | 98,304 |
| total | **634,886** | **104,141** |

\[
\boxed{\Lambda_C=\frac{634886}{104141}=6.0964077548708}.
\]

Total counted work fell by approximately **83.5969%** despite the LUT realizer paying a much larger one-time construction cost.

## Robustness B

The perturbation universe was all 512 single-bit flips in the shared 64-byte auxiliary-memory region, with complete 4,096-input validity checked after every fault.

```text
|B0| = 512
|B1| = 448
B1 subset B0 = true
B1 proper subset B0 = true
```

R0 ignores the reserved region, so all 512 faults preserve F. R1 masks each table read with `& 1`: the seven high-bit flips per byte are harmless, while the low-bit flip in each of 64 parity cells breaks full-domain validity. Thus:

\[
\boxed{B_1\subsetneq B_0}.
\]

Exact robustness-vector SHA-256 digests:

```text
R0 dabdd72895a4cb287ddfadff4412cb3a9c3ef61f0fdae70939b5a0eba4863c2a
R1 0dbeacead75c64b6283beb6cba1bfee261ae63f4703109982e14c2697f90dd7e
```

The complete 512-bit vectors are preserved in `RG_002_RESULT.json`.

## Terminal adjudication

The preregistered condition is satisfied:

\[
\boxed{V_0=V_1=1,\qquad C_1<C_0,\qquad B_1\subsetneq B_0}.
\]

Therefore:

```text
RG-002 = COST_ROBUSTNESS_TRADEOFF, CLOSED
```

## Earned claim

> Under the exact frozen 12-bit parity function, CPython 3.13.5 opcode-cost contract, two frozen realizers, and one-bit auxiliary-memory fault model, RG-002 demonstrates a bounded cost/robustness separation between two valid realizations of the same function.

This is a constructed bounded existence witness. It does **not** establish realization geometry as a general theory, biological affordance migration, natural evolutionary tradeoffs, hardware-independent cost relations, environmental autonomy, representation-induced generality, or any RIL-003 result.
