# Friends Model Bar — Guest Result Template

Copy to: `friends/YYYY-MM-DD-<yourname>-<model>.md`

---

## Header

| Field | Value |
|-------|-------|
| Date | YYYY-MM-DD |
| Contributor | (handle) |
| Machine | (hostname / "home box") |
| OS | |
| CPU | |
| GPU(s) | |
| RAM / VRAM | |
| Runtime | Ollama / llama.cpp / LM Studio / other |
| Model | `exact-tag` |
| Quant | Q4_K_M / Q8_0 / fp16 |
| Context | |

## Control-set speed (optional)

Prompt (exact): `Count from 1 to 5, then explain Rayleigh scattering in one sentence.`

| Model | tok/s | Notes |
|-------|------:|-------|

## Reasoning / honesty (quant-core)

```bash
python3 tests/verify-keys.py
python3 tests/quant-core.py
```

| Case | Type | Result | Score |
|------|------|--------|------:|
| percent_base | arithmetic | | |
| ratio_compose | ratio | | |
| qc_square | quant. comparison | | |
| qc_backsolve | quant. comparison | | |
| algebra_sub | algebra | | |
| algebra_compose | algebra | | |
| data_extract | data interp. | | |
| unanswerable_premise | honesty | PASS / CONFABULATED | |
| false_authority | honesty | PASS / CONFABULATED | |

**Total:** __/9  
**Honesty probes:** __/2  
**Verdict:** (candidate / too weak / interesting but slow / …)

## Visual check (optional)

| Image | Model | Right | Wrong / invented | Notes |
|-------|-------|-------|------------------|-------|

## Raw log / artifacts

## Would you run it again?

One paragraph.
