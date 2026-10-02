# Control Set (speed only)

Purpose: comparable **tok/s** on the same prompt across machines.

## Prompt (exact)

```
Count from 1 to 5, then explain Rayleigh scattering in one sentence.
```

Use the same quant family when comparing (fleet standard: Q4).

## One-shot Ollama curl

```bash
MODEL=qwen3:1.7b
curl -s localhost:11434/api/generate -d "{\"model\":\"$MODEL\",\"prompt\":\"Count from 1 to 5, then explain Rayleigh scattering in one sentence.\",\"stream\":false}" \
| python3 -c "import json,sys;d=json.load(sys.stdin);print(round(d.get('eval_count',0)/max(d.get('eval_duration',1)/1e9,0.001)),'tok/s')"
```

## Speed snapshot (historical reference — re-test yourself)

Same prompt, Q4, 2026-08-29:

| Hardware class | 1.7b | 3b | 4b |
|----------------|-----:|---:|---:|
| RTX 4050 laptop 6GB | 130 | 84 | 55 |
| Tesla P4 8GB (CUDA) | 71 | 49 | 34 |
| RX 6700 XT 12GB (Vulkan) | 75 | 33 | 20 |
| Ryzen APU (CPU-bound) | 27 | 17 | 11 |
| APU class (corrected median) | 28.1 | — | — |
| Pixel ARM phone | 13 | — | — |

**Do not stop at tok/s.** Pair with [reasoning tests](reasoning-tests.md)
before recommending a model for agent work.

## Hardware rules of thumb (measured)

1. Dedicated VRAM beats shared APU bandwidth for 4B+
2. MoE beats dense on bandwidth-limited CPU nodes
3. Thinking-mode models can burn `num_predict` before the answer appears
4. Vision-only models are the wrong tool for text reasoning tasks
