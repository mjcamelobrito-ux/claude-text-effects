# 34 · 3D Pop Letters

**Inspired by:** the "3D Text Pop Up Animation" After Effects tutorial (flat text whose letters pop up into chunky 3D blocks). The idea is borrowed; the colours, shockwaves, spin wave and sink are this repo's own.
**Best for:** Punchy one-word titles, brand names, launches and "NEW" moments: playful, toy-like, high energy.
**Format:** 1080×1920 (9:16), 30 fps · demo length 5.1 s · footage: No (colour stage).

![preview](poster.jpg)  ·  [preview.mp4](preview.mp4)

## Look
- A word printed flat on the floor of a dark indigo stage, seen from slightly above.
- When it pops, every letter becomes a solid extruded block (Archivo Black, 14 layers deep), each in its own candy colour (lime, pink, periwinkle, coral, sky…) with darker sides of the same hue.
- Soft contact shadows; a white shockwave ring ripples out on the floor under each letter as it pops.

## Motion language
- **Pop:** left to right, each flat letter springs up (back.out) while its extrusion inflates from flat print to a full block, with a little jump and a bouncy landing.
- **Sway:** standing letters sway on their own axes in alternating directions while the camera eases around the word.
- **Spin wave:** every letter does one full turn, rippling across the word.
- **Sink:** right to left they lie back down and deflate into flat print.

## Edit rhythm
0.13 s between letters; ~1.5 s hold with sway; 0.65 s spin wave; 0.45 s sink.

## Scene recipe
| Scene file | What it does |
| --- | --- |
| `compositions/pl1.html` | Flat word pops up letter by letter into 3D blocks, sways, spin-waves, sinks flat. |

## What to swap
- Word, size, colours: `WORD`, `FS`, `PAL` in `tools/generate_34_35.py`, then run `python3 tools/generate_34_35.py && python3 tools/build_index.py styles/34-3d-pop-letters/template`. (Each letter is 15 stacked spans, so editing by hand is tedious.)
- Stage colours: `stageLight`, `stageDeep`. Depth: `DEP` (layers) and `STEP` (px per layer).
- Timing: the POP / SWAY / SPIN / SINK tweens in the script.

## Build / render
```bash
cd styles/34-3d-pop-letters/template
python3 ../../../tools/build_index.py .
npx hyperframes preview
npx hyperframes check
npx hyperframes render -o out.mp4
```
