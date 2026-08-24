# RG-002 — Final Audit

Status: **PASS / CLOSED / COST_ROBUSTNESS_TRADEOFF**

## Sequence integrity

```text
RG-001 null preserved                         PASS
RG-002 preregistration before repair code     PASS
scientific object inherited unchanged          PASS
corrected tracer frozen before primary rerun   PASS
sentinel pre-execution audit                   PASS
validity before cost                           PASS
cost before robustness                         PASS
full 512-fault robustness execution            PASS
```

## Primary gates

```text
V0                                      1
V1                                      1
C0 total opcodes                        634886
C1 total opcodes                        104141
Lambda_C                                6.0964077548708
B0 preserved faults                     512/512
B1 preserved faults                     448/512
B1 proper subset B0                     PASS
terminal verdict                        COST_ROBUSTNESS_TRADEOFF
```

## Provenance qualification

RG-002 is **not an independent replication** because the failed RG-001 cost attempt revealed partial cost information before the tracer repair. The scientific object itself, however, was prospectively selected and frozen before that attempt; RG-002 changed only the measurement layer and explicitly preregistered the repair before rerunning primary measurements.

## Claim ceiling

The result supports only a bounded existence witness that two valid realizations of one fixed function can exhibit a cost/robustness tradeoff under one exact computational substrate and fault model.

No general realization-geometry law is earned. No autonomy axis was tested. No RIL-003 artifact or criterion changed.

## RIL-003 firewall

```text
RIL-003 Beacon/targets read         NO
RIL-003 files modified              NO
RIL-003 target selection changed    NO
RIL-003 interpretation changed      NO
```

Terminal:

```text
RG-001   CLOSED / NOT_EVALUABLE
RG-002   CLOSED / COST_ROBUSTNESS_TRADEOFF
RIL-003  UNCHANGED / PRE-REVEAL
```
