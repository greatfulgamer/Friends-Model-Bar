# Friends Model Bar

A **public** group notebook for people running local models at home —
brothers, friends, other fleets. No RobCo framework required.

> Fleet-internal Model Bar (war-room, doctrine, deployment, raw node logs)
> lives in a **private** repo. This repo is the shareable watering hole.

## Add your findings

1. Copy [`friends/_TEMPLATE.md`](friends/_TEMPLATE.md) →
   `friends/YYYY-MM-DD-<you>-<model>.md`
2. Run at least one kit:
   - [Reasoning + honesty](kits/reasoning-tests.md) ← most important
   - [Visual tests](kits/visual-tests.md)
   - [Control-set speed](kits/control-set.md)
3. Open a PR, or send the markdown to whoever maintains this repo

## Example

See [`friends/EXAMPLE-2026-10-02-raul-lfm25.md`](friends/EXAMPLE-2026-10-02-raul-lfm25.md)
for a filled-in post (historical reference — re-test on your hardware).

## Layout

| Path | What |
|------|------|
| `friends/` | Group results — **you add files here** |
| `kits/` | How to run the three portable tests |
| `tests/` | Machine-checked reasoning suite (quant-core) |
| `Visual Tests/` | Stock images for vision prompts |

## Ground rules

- **No secrets** — no passwords, API keys, private keys
- Post **measured** numbers; say what hardware you used
- Rank by **task quality first** (reasoning/honesty), speed second
- Failures are data — confabulating / not terminating is a valid finding
- Be kind; different boxes will get different tok/s

## Why reasoning tests?

Independent testing found the **fastest models were often the worst reasoners**
when checked with verified answer keys. Speed alone is a trap for agent work.
The quant-core suite is small, portable, and machine-scored.
