# RIL-001 — Pre-Execution Audit

Status: **PASS; frozen before any primary R0/R1 cost result was inspected or compared.**

Preregistration anchor: `204fe919159145ac9c29f1becfb92b0c511af02b`  
Implementation freeze: `a0f8f795a805e8f579fd608fbcaa83dcfa6ef60f`

This audit authorizes the one-shot primary RIL-001 execution. It is prerequisite evidence only. It is not evidence of representation-induced leverage.

## 1. Implementation freeze integrity

The implementation commit is a single child of repository state `51f81862bed87e0e770e89b0024ccf867662c319` and adds exactly eight files under `experiments/ril_001/`:

| Path | Git blob |
|---|---|
| `contract.py` | `2f4b18721cddaabfb0ea118adada2ea0161659de` |
| `algorithm.py` | `e64d5b08e69330cdc08dd0cc8ea85f238ae04593` |
| `audit.py` | `eddf91309839c4bc38cec3f6c1b48528a4ab5a02` |
| `instrument.py` | `ac8bf7b728bc3ad25847e597770fbc97dbc0c613` |
| `ril_001.py` | `0d003b24891e6607809ad2937d52ba25bf073047` |
| `test_ril_001.py` | `fcc9a415173e482345f18824614ce0f9874b4200` |
| `execution_config.json` | `4020bc7edc9a417df0161fffcdde5b8541c1cc55` |
| `README.md` | `d97ca741c1b20a4b84638492e249fec7273340a1` |

No frozen preregistration, corpus, necessity, CGP, status, or roadmap artifact changed in the implementation commit.

## 2. Frozen parent source integrity

Parent: `bjoern-janson/future-sufficiency@2f4ca824e02b89df0c23d64de312c4f93a4c8a41`.

Verified Git blobs:

- `experiments/meta_language_repair.py`: `f74d85f5f9d0c7842dc50e34ae2718699108fff6`
- `experiments/meta_language_repair.md`: `9ac2883c797e99af27fd092b262f5cb6ce8ece70`

Runtime source audit reproduced exactly:

```text
READ_ONCE_PROGRAMS = 94
FANOUT_PROGRAMS    = 127
M0 majority ceiling = 0.875
M1 majority ceiling = 1.0
frozen constants/order = PASS
```

## 3. Parent positive control

The native FS007 low-cost `NEEDS_FANOUT` condition reproduced before RIL execution:

```text
base empirical accuracy    = 0.89
fanout empirical accuracy  = 1.0
estimated repair value     = 10.999999999999998
repair cost                = 5.0
repaired                   = true
construction rule after    = fanout_allowed
held-out transfer          = 1.0
goal_rule_mutated          = false
authority_expanded         = false
```

This is a source/reproduction gate, not a RIL result.

## 4. `A_fixed` static audit

PASS on all frozen static checks:

```text
shared_algorithm_has_no_representation_branch = true
single_shared_search_path_present              = true
representation_difference_isolated_in_predictors = true
```

The shared algorithm performs candidate enumeration, exact empirical scoring, tie-breaking, gain/value computation, persistence, and held-out evaluation. The scientific representation difference is isolated to:

```text
R0_AST  : program.evaluate_local((x,y,z))
R1_SEM8 : semantic_tuple[4*x + 2*y + z]
```

and to whether the candidate view payload references the parent AST value or existing semantic-tuple key.

## 5. Pre-cost semantic/mechanical tests

Before implementation freeze, and without running the frozen primary condition through both costed arms, the apparatus passed:

- exact candidate counts;
- all `221 x 8` candidate/pattern R0↔R1 semantic identity checks;
- fail-closed unknown-representation handling;
- Python compilation;
- instruction-counting mechanics on a deliberately tiny non-primary one-candidate fixture.

These checks are implementation validation only. Full P1–P9 preservation remains a post-primary gate exactly as preregistered.

## 6. Opcode instrumentation audit

The frozen interpreter is CPython `3.13.5`. Primary deterministic work is counted with `sys.monitoring` `INSTRUCTION` events.

This is accepted as the preregistered CPython opcode/instruction-event unit because each monitored `INSTRUCTION` event corresponds to execution of a CPython bytecode instruction in the frozen interpreter. The harness assigns events to the four frozen regions:

```text
translation
eval
search
update
```

The monitoring callbacks themselves are outside those root regions and are not charged as scientific work. Instrumentation mechanics were verified on a non-primary fixture before freeze.

If the primary run produces unequal `c_search^op` or unequal `c_update^op`, `A_fixed` fails post-execution and the terminal status is `NOT_EVALUABLE` regardless of total cost.

## 7. Frozen execution environment

See `experiments/ril_001/execution_manifest.json` for the exact runtime manifest. Key values:

```text
Python implementation = CPython
Python version        = 3.13.5
platform              = Linux 6.18.35 x86_64
visible CPUs          = 5
affinity              = [0,1,2,3,4]
timing repetitions    = 15
timing warmup         = none; every arm run in a fresh process
timing order          = alternating by repetition
```

Wall time remains confirmatory only.

## 8. Pre-execution verdict

```text
source integrity = PASS
parent positive control = PASS
A_fixed static isolation = PASS
opcode instrumentation admissibility = PASS
PRIMARY EXECUTION = AUTHORIZED
```

No leverage claim is made. The next legal sequence is:

```text
primary cost files -> preservation P -> A_fixed dynamic equality -> cost verdict -> STOP
```
