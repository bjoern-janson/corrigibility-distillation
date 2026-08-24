# RD-001 Calibration Beacon Request v2

**Status:** `V2 ROUND SELECTED FROM FROZEN RULE / BEACON BYTES NOT YET CAPTURED / CALIBRATION NOT RUN`

V2 implementation-refreeze commit:

`7d5fb20d73f47dab4d6dae72ad3ad16ad6443ea7`

Frozen v2 committer timestamp:

`2026-08-24T20:51:01Z`

Frozen drand default-mainnet parameters:

```text
chain_hash = 8990e7a9aaed2ffed73dbd7092123d6f289930540d7651336225dc172e51b2ce
genesis    = 1595431050
period     = 30 seconds
T(r)       = genesis + period*(r-1)
```

The unique first round satisfying `T(r) > v2_freeze_timestamp` is:

```text
round          = 6405789
scheduled_time = 2026-08-24T20:51:30Z
```

Primary frozen retrieval URL:

https://api.drand.sh/8990e7a9aaed2ffed73dbd7092123d6f289930540d7651336225dc172e51b2ce/public/6405789

Secondary relay-agreement URL:

https://drand.cloudflare.com/8990e7a9aaed2ffed73dbd7092123d6f289930540d7651336225dc172e51b2ce/public/6405789

Retired v1 round:

```text
6405769 = NOT CONSUMED / INELIGIBLE FOR V2
```

No later round may be substituted because of availability, convenience, or observed value.
