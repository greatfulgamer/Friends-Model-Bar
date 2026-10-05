# Fleet findings summary (public)

**Updated:** 2026-10-04 · **Source:** GX-9000 Model Bar measurements (portable kits)  
**Private war-room / node logs** stay in the fleet-private Model Bar repo.

This page is for **friends/brothers** running local models. Numbers are
**historical fleet references** — re-test on your own hardware.

---

## 1. Rank by reasoning, not tok/s

Independent, machine-checked runs found:

| Model (tag) | Speed vibe | quant-core | Honesty probes |
|-------------|------------|------------|----------------|
| **`lfm2.5:8b`** | mid (not fastest) | **9/9** on two nodes | **2/2 PASS** (refuses false premises) |
| `phi4-mini-reasoning` | **very fast** | 2/9 | `CUT_OFF` / incomplete (budget vs ability — verify) |
| `llama3.2:3b` | ok | 1/9 | **NO_REFUSAL** — answered questions with no factual answer |
| `qwen3.5:4b` | ok | low on early runs | confabulated details — retest with thinking budget if needed |

**Rule:** the fastest model was the **worst reasoner** on identical hardware.
Any selection by tok/s alone will pick confabulators for agent/war-room work.

---

## 2. Portable test kits (run these)

| Kit | Path | What it proves |
|-----|------|----------------|
| Reasoning + honesty | [`kits/reasoning-tests.md`](kits/reasoning-tests.md) | Multi-step math + refusal behaviour |
| Control-set speed | [`kits/control-set.md`](kits/control-set.md) | tok/s baseline |
| Visual | [`kits/visual-tests.md`](kits/visual-tests.md) | Screenshot understanding |
| Machine scorer | [`tests/quant-core.py`](tests/quant-core.py) + [`tests/verify-keys.py`](tests/verify-keys.py) | **Refuses to score** if answer keys missing |

```bash
python3 tests/verify-keys.py
python3 tests/quant-core.py
```

**Harness honesty:** if `verify-keys.py` fails, **do not invent a score**.
Missing keys = no result. A score you did not verify is not evidence.

---

## 3. Hardware lessons (portable)

| Lesson | Why it matters |
|--------|----------------|
| **MoE beats dense** on bandwidth-limited nodes (APU/CPU) | Active params drive cost, not total size |
| **iGPU “GPU acceleration” is often fake** | Ollama may *detect* iGPU then drop it — check `/api/ps`, not just logs |
| **Dense 8B on weak APU ≈ unusable** | ~4 tok/s class |
| **MoE 20B-class can fit less RAM than feared** | e.g. some 13–14GB MoE run in ~11GB free |
| **Thinking models can starve at small budgets** | Empty answer ≠ model failure — raise `num_predict` |
| **Harness bugs invert scores** | Strip `</think><tool_call><function=write><parameter=content># Fleet findings summary (public)

**Updated:** 2026-10-04  
**Audience:** brothers, friends, other fleets  
**Private war-room / raw node logs** live in the fleet-private Model Bar — not here.

Numbers below are **historical fleet measurements**. Re-test on **your** hardware before trusting them.

---

## Why this notebook exists

Local models behave differently per GPU, quant, driver, and RAM. Leaderboards
rarely match a home box. Post **measured** results — pass or fail.

**Ground rule already proven in our fleet:**  
> The **fastest** model was often the **worst reasoner** when checked with
> machine-verified answer keys. Rank by **task quality first**, speed second.

---

## Portable kits

| Kit | Path | What it measures |
|-----|------|------------------|
| **Reasoning + honesty** (most important) | [`kits/reasoning-tests.md`](kits/reasoning-tests.md) | quant-core cases + refusal probes |
| Control-set speed | [`kits/control-set.md`](kits/control-set.md) | tok/s on a fixed prompt |
| Visual | [`kits/visual-tests.md`](kits/visual-tests.md) | Screenshot / HUD understanding |
| Machine scorer | [`tests/quant-core.py`](tests/quant-core.py) + [`tests/verify-keys.py`](tests/verify-keys.py) | Deterministic scores — **refuses to run if keys missing** |

```bash
python3 tests/verify-keys.py
python3 tests/quant-core.py
```

**If `verify-keys.py` fails, do not invent a score.**  
A score produced by a tool you have not verified is not evidence.

---

## Findings worth carrying into your own tests

### 1) Speed ≠ reasoning
On identical hardware, a mid-speed MoE (`lfm2.5:8b`) scored **9/9** on quant-core
(both arithmetic and honesty probes), while faster small dense models scored
poorly and **confabulated** on questions whose correct answer is “no such rule.”

See [`friends/EXAMPLE-2026-10-02-raul-lfm25.md`](friends/EXAMPLE-2026-10-02-raul-lfm25.md)
(historical example — re-test yourself).

### 2) Thinking models can look “broken” when starved
A model that returns empty may have burned the whole token budget *thinking*.
Distinguish **harness starvation** from **model inability** before scoring FAIL.

### 3) Harness bugs invert results
Stripping reasoning markers (`</think><tool_call><function=write><parameter=content># Friends Model Bar — Fleet findings summary (public)

**Updated:** 2026-10-04  
**Audience:** brothers, friends, other fleets — no RobCo framework required.  
**Private war-room / raw node logs** stay in the fleet-private Model Bar repo.

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
| `llama3.2:3b` | ok | 1/9 | **NO_REFUSAL** — answered questions with no factual answer |
| `qwen3.5:4b` | ok | low on early runs | Confabulated details — retest with thinking budget |

**Takeaway for your box:** do **not** pick a model from a speed table alone for
agent / tool-call / war-room style work.

Filled example (historical): [`friends/EXAMPLE-2026-10-02-raul-lfm25.md`](friends/EXAMPLE-2026-10-02-raul-lfm25.md)

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
| **LaTeX / reasoning wrappers break naive scorers** | `\boxed{...}` and `</think><tool_call><function=write><parameter=content># Friends Model Bar — Fleet findings summary (public)

**Updated:** 2026-10-04  
**Audience:** brothers, friends, other fleets — no RobCo framework required.  
**Private war-room / raw node logs** stay in the fleet-private Model Bar repo.

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
| `llama3.2:3b` | ok | 1/9 | **NO_REFUSAL** — answered questions with no factual answer |
| `qwen3.5:4b` | ok | low on early runs | Confabulated details — retest with thinking budget |

**Takeaway for your box:** do **not** pick a model from a speed table alone for
agent / tool-call / war-room style work.

Filled example (historical): [`friends/EXAMPLE-2026-10-02-raul-lfm25.md`](friends/EXAMPLE-2026-10-02-raul-lfm25.md)

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
