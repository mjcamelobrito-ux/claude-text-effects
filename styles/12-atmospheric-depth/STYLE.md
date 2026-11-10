# 12 · Atmospheric Depth

**Reference:** "Marca la diferencia con un estilo único de edición" (Spanish motion reel)
**Best for:** Premium studio/brand intros, cinematic personal-brand reels, Spanish-language content (template copy is in Spanish).
**Format:** 1080×1920 (9:16), 30 fps · demo length 9.8 s · footage: No: pure motion graphics.

![preview](poster.jpg)  ·  [preview.mp4](preview.mp4)

## Look
- Cream wall `#ece6db` with soft window-light shadows; alternates with dark atmospheric scenes (light shafts, gothic arch window).
- Deep focus play: foreground words out of focus sliding past the lens, mid-ground sharp, background soft.
- Thin grey + heavy black Inter, Didone accent (Abril Fatface), outlined serif.
- Organic accents: ink branch with red blossoms, falling petals, audio waveform line; logo framed by corner brackets.

## Motion language
- Rack-focus reveals (blur 20 → 0).
- Dissolve through blur between scenes.
- Branch draws itself (stroke-dash), blossoms pop along it.
- Light shafts slowly rotate; lens flare sweeps across the logo.

## Edit rhythm
Slow, cinematic: 2.4–2.6 s per scene.

## Scene recipe
All on-screen copy is lorem-ipsum placeholder sized like the reference; quotes below describe what each slot held in the reference reel. Replace it with lines from your script or the footage transcript, keeping roughly the same word count per slot.

| Scene file | What it does |
| --- | --- |
| `compositions/ad1.html` | 'de un mercado' + waveform, foreground blur drift. |
| `compositions/ad2.html` | Dark arch window, light shafts, petals: 'experiencias VISUALES'. |
| `compositions/ad3.html` | Ink branch + 'pero no todo'. |
| `compositions/ad4.html` | Logo in bracket frame + flare. |

## What to swap
- Logo SVG in `ad4.html`.
- Colours: `cream`, `blossom`.
- Copy is Spanish; swap freely.
- Editable variables (HyperFrames Variables panel): `cream`, `blossom`.

## Build / render
```bash
cd styles/12-atmospheric-depth/template
python3 ../../../tools/build_index.py .   # after reordering/retiming scenes.json
npx hyperframes preview                    # live preview / edit
npx hyperframes check                      # lint + layout audit
npx hyperframes render -o out.mp4          # final render
```
