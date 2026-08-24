# RG-001 — Final Audit

Status: **CLOSED / NOT EVALUABLE**

## Sequence integrity

```text
preregistration before implementation   PASS
implementation freeze before results    PASS
pre-execution audit                     PASS
validity run                            PASS
cost run                                ATTEMPTED
cost instrumentation contract           FAIL
robustness run                          NOT REACHED
```

## Failure classification

Shallowest supported locus:

```text
measurement / instrumentation
```

The scientific realizers themselves were both exactly valid on all 4096 inputs. The failure is that the frozen CPython opcode tracer did not count `build_r0` construction opcodes, despite construction being explicitly included in the preregistered cost object.

## No salvage under identifier

The invalid cost record is provenance only. No corrected cost value, robustness result, or realization-geometry inference is admitted under RG-001.

Any corrected tracer requires a new prospective assay identifier.

## RIL-003 separation

No RIL-003 scientific or apparatus file was modified. No Beacon, target, target manifest, or RIL-003 primary result was read or generated.

Terminal:

```text
RG-001    CLOSED / NOT_EVALUABLE
RIL-003   UNCHANGED / PRE-REVEAL
```
