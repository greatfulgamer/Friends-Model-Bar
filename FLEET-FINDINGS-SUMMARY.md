# Fleet findings summary (public)

**Updated:** 2026-10-05  
**Audience:** brothers, friends, other fleets — no RobCo framework required.  
**Private war-room / raw node logs** live in the fleet-private Model Bar — not here.

This page is the **public findings digest**. Numbers are **historical fleet
references** — re-test on your own hardware.

---

## Ground rules (repeat)

1. **No secrets** — passwords, API keys, private keys stay out of git.
2. Post **measured** numbers + hardware you used.
3. Rank by **task quality first** (reasoning / honesty), **speed second**.
4. Failures are data — confabulating / not terminating is a valid finding.
5. **Merge never overwrite** — add your file under `friends/`; don’t delete others’ posts.

---

## Why reasoning kits matter

Independent fleet testing found that on identical hardware the **fastest models
were often the worst reasoners** when scored with **machine-checked answer keys**.

| Model (historical fleet) | Speed vibe | quant-core | Honesty probes |
|--------------------------|------------|------------|----------------|
| **`lfm2.5:8b`** | mid | **9/9** on two nodes | **2/2 PASS** — refused false premises |
| `phi4-mini-reasoning` | very fast | low / often `CUT_OFF` | Do not trust “refusal” without full completion |
| `llama3.2:3b` | ok | 1/9 (older harness) | Retest with fixed harness before judging |
| `qwen3.5:4b` | ok | low on early runs | Confabulated details — retest with thinking budget |

**Takeaway for your box:** do **not** pick a model from a speed table alone for
agent / tool-call / war-room style work.

Filled example (historical): [`friends/EXAMPLE-2026-10-02-raul-lfm25.md`](friends/EXAMPLE-2026-10-02-raul-lfm25.md)

### Research-node retests (2026-10-05) — fixed harness

Full post: [`friends/2026-10-05-fleet-research-retests.md`](friends/2026-10-05-fleet-research-retests.md)

| Node class | Model | decode tok/s | Reasoning | Honesty |
|------------|-------|--------------|-----------|---------|
| Research A | `lfm2.5:8b` | **28.96** | correct | corrected |
| Research B | `llama3.2:3b` | **15.26** | correct | corrected |

**Harness lesson:** old “billions of tok/s” scores were duration-key bugs. Retest with fixed harness only.

---

## How to run the portable suite

```bash
# from repo root
python3 tests/verify-keys.py    # must pass BEFORE scoring
python3 tests/quant-core.py     # machine-scored reasoning + honesty
```

| Kit | Path | Measures |
|-----|------|----------|
| Reasoning + honesty | [`kits/reasoning-tests.md`](kits/reasoning-tests.md) | Multi-step math, ratio, unanswerable premise, false authority |
| Control-set speed | [`kits/control-set.md`](kits/control-set.md) | tok/s on a fixed prompt |
| Visual | [`kits/visual-tests.md`](kits/visual-tests.md) | Screenshot understanding |
| Quant harness | [`tests/quant-core.py`](tests/quant-core.py) | Score `__ / 9` + honesty |

**Harness honesty rule:** if `verify-keys.py` fails, **do not invent a score**.
A score produced by an unverified checker is not evidence.

---

## Hardware lessons that travel

| Lesson | Why it matters |
|--------|----------------|
| **MoE beats dense** on bandwidth-limited nodes | Active parameters drive cost, not total size |
| **iGPU “GPU” logs ≠ acceleration** | Some runtimes *detect* an iGPU then drop it — check measured tok/s |
| **Dense 8B on weak APU can crawl** | ~4 tok/s class on 680M-class hardware in our tests |
| **MoE can fit less RAM than you fear** | Some 13–14GB MoE ran in ~11GB free on a constrained node |
| **Thinking models starve at tiny budgets** | Empty answer ≠ model failure — raise token budget before FAIL |
| **LaTeX / reasoning wrappers break naive scorers** | `\boxed{5:8}` is correct even if a dumb matcher says FAIL |

---

## What to post when you finish a run

Copy [`friends/_TEMPLATE.md`](friends/_TEMPLATE.md) →  
`friends/YYYY-MM-DD-<you>-<model>.md`

Include:

- Hardware (CPU / GPU / RAM / quant / runtime)
- Control-set tok/s (optional but useful)
- Full quant-core table + honesty probes
- Honest verdict: **PASS / PASS-WITH-CAVEATS / STOP** (not just a number)
- What broke (if anything) — harness bugs count as findings

---

## Related public surface

| Repo | Purpose |
|------|---------|
| **Friends-Model-Bar** (this repo) | Group notebook + portable kits |
| Fleet Field Manual (public educational) | How a home AI fleet is organized at a high level |
| Private Model-Bar | War-room, doctrine, raw logs — not for public clone |

---

*Non Impediti Ratione Cogitationis.*
