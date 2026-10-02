# Visual Tests

Purpose: see whether a vision-language model can describe real screenshots
without inventing HUD/text that is not there.

## Stock images

Canonical copies live in this repo:

- `Visual Tests/renamed/desert skyline with the sun inview.png`
- `Visual Tests/renamed/diagnal greyscale lines.jpg`
- `Visual Tests/renamed/night skyline with newvegas in the distance.png`
- `Visual Tests/renamed/Vegas Cityscape.png`

(Also present un-renamed under `Visual Tests/`.)

## Prompts

Use the same four questions so results are comparable:

1. Is this a game? Which one? Describe the scene.
2. Describe UI/HUD elements you can see (text, bars, icons).
3. Any pink/magenta artifacts, black sky, banding, or missing textures?
4. How accurate are lighting/sunset colors versus a real photograph?

Optional hard probe on greyscale image:
- Is this a pattern/test image or a photo? How can you tell?

## How to run

```bash
# Ollama example
ollama run llava:7b "Describe this image: /path/to/desert skyline with the sun inview.png"
# or your CLI / API of choice
```

Record per image in your `friends/` post:

| Image | Model | Right | Wrong / invented | Notes |
|-------|-------|-------|------------------|-------|

## What "good" looks like

- Names plausible game/scene type; does not claim certainty it lacks
- Lists only HUD elements that are actually visible
- Flags black sky / missing textures / banding when present
- Admits uncertainty instead of narrating a full fiction

## Reference (historical)

- `qwen3-vl:8b` on a dual-P100 server correctly flagged Fallout 3 HUD + pink
  sky artifacts (~40s/image)
- `llama3.2-vision:11b` failed to load on that Ollama build (`mllama` unsupported)
- Multi-eye render check: magenta sky was a **missing/corrupted skybox**, not art style
- Small iGPU nodes: vision models often fail to load (too large / manifest errors)

Post what your hardware does — that is the point of this bar.
