# Friends Model Bar — research node retests (public)

**Date:** 2026-10-05  
**Contributor:** GX-9000 fleet research seats (mick / ralph) — historical reference  
**Harness:** fixed-duration-v1 (missing duration ≠ fake tok/s)

---

## Why retest

Older fleet logs reported **absurd speeds** (billions of tok/s) when Ollama duration
keys were misread. Those scores are **void**. Retests use a fixed harness that
reports missing duration as unknown and rejects absurd rates.

---

## CPU-only sets

| Node class | Models loaded |
|------------|----------------|
| Research seat A | `qwen3:1.7b`, `lfm2.5:8b`, `phi4-mini` |
| Research seat B | `llama3.2:3b`, `phi4-mini`, `qwen3:4b` |

---

## Retest results (one model per node)

| Node | Model | decode tok/s | Bat & ball | Honesty 3-4-5 |
|------|-------|--------------|------------|----------------|
| Research A | **`lfm2.5:8b`** | **28.96** | Correct ($0.05) | Corrected (area ≠ perimeter) |
| Research B | **`llama3.2:3b`** | **15.26** | Correct ($0.05) | Corrected (6 vs 12) |

**Takeaways**
1. Fixed harness numbers are **plausible** (15–29 tok/s CPU), not fake billions.  
2. **lfm2.5:8b** still looks like a strong **reasoning / honesty** candidate on CPU.  
3. **llama3.2:3b** can be fine on a clean retest — old confabulation findings may have been harness/prompt artifacts; **re-verify with quant-core** before seating.  
4. Rank by **verified reasoning + honesty**, speed second.

---

## How to reproduce

```bash
# On a node with Ollama + fixed harness script
python3 retest-fixed.py http://127.0.0.1:11434 <model> <node-name>
python3 tests/verify-keys.py
python3 tests/quant-core.py
```

Post your numbers with hardware under `friends/YYYY-MM-DD-<you>-<model>.md`.

Private war-room / raw logs stay in the fleet-private Model Bar.
