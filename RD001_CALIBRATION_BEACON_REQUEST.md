# RD-001 Calibration Beacon Request

**Status:** `ROUND SELECTED FROM FROZEN RULE / BEACON BYTES NOT YET CAPTURED / CALIBRATION NOT RUN`

Implementation-freeze commit:

`4ffa3f7810baa8c3cc62e37de44b265114acd5d6`

Frozen implementation-freeze committer timestamp:

`2026-08-24T20:41:11Z`

Frozen drand default-mainnet parameters:

```text
chain_hash = 8990e7a9aaed2ffed73dbd7092123d6f289930540d7651336225dc172e51b2ce
genesis    = 1595431050
period     = 30 seconds
T(r)       = genesis + period*(r-1)
```

The unique first round satisfying `T(r) > freeze_timestamp` is:

```text
round          = 6405769
scheduled_time = 2026-08-24T20:41:30Z
```

Primary frozen retrieval URL:

https://api.drand.sh/8990e7a9aaed2ffed73dbd7092123d6f289930540d7651336225dc172e51b2ce/public/6405769

Secondary relay-agreement URL:

https://drand.cloudflare.com/8990e7a9aaed2ffed73dbd7092123d6f289930540d7651336225dc172e51b2ce/public/6405769

No later round may be substituted because of availability, convenience, or observed value.
