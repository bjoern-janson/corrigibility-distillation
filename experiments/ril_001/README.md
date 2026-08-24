# RIL-001 apparatus

Authority: `RIL_001_PREREGISTRATION.md` at `204fe919159145ac9c29f1becfb92b0c511af02b`.

This directory contains apparatus only. Freeze implementation before observing any
primary R0/R1 cost comparison. Then audit source integrity and `A_fixed`; if they
pass, execute once, apply preservation `P` before interpreting cost, issue the
preregistered terminal verdict, and stop.

`R0_AST` and `R1_SEM8` share one search/update/held-out path. The only scientific
representation difference is the candidate payload and prediction primitive.
