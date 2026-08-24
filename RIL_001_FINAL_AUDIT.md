# RIL-001 — Final Audit

Terminal verdict: **`REPRESENTATION_INDUCED_LEVERAGE`**

## Audit ordering

The scientific order was preserved:

```text
preregistration
-> implementation freeze
-> pre-execution source/A_fixed/instrumentation audit
-> primary resource records generated without inspection
-> P1-P9 preservation inspected and passed
-> opcode/memory records opened
-> dynamic A_fixed equality checked
-> terminal verdict assigned
-> confirmatory wall timing
-> STOP
```

No primary R0/R1 cost comparison was observed before implementation freeze. No implementation, counter boundary, representation construction, source pin, dataset, candidate order, scoring rule, or authority rule was modified after the first primary record was generated.

## Preservation audit

All P1-P9 passed. There were zero semantic mismatches and zero per-candidate scoring mismatches. Candidate counts were 94 and 127; candidate identities/order were shared. Both arms selected the same canonical M1 candidate and produced identical held-out predictions.

## Fixed-algorithm audit

Static audit passed before execution. Dynamic shared regions were:

```text
c_search^op(R0) = c_search^op(R1) = 3,274,609
c_update^op(R0) = c_update^op(R1) = 67
```

Thus the cost difference is not credited to pruning, changed candidate order, early stopping, changed adoption logic, or changed update logic.

## Cost audit

```text
C_op(R0_AST)  = 9,825,003
C_op(R1_SEM8) = 4,094,613
Lambda_F^op   = 2.399494897320
peak memory R0 = 206,757
peak memory R1 = 206,757
```

Both preregistered positive cost gates pass.

## Epistemic status

The result earns only the bounded RIL-001 existence claim. It does not retroactively alter the frozen corpus, CGP-001, or the RIL roadmap. `RIL-2` remains a future question requiring an explicit new preregistration.
