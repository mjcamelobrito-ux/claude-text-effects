# 19 · Bend Text 3D

**Origin:** an original kinetic 3D text effect for this repo.
**Best for:** Title cards and hooks that should feel physical and playful: a headline printed on a flexible sheet that bows, curves, rolls into a tube and springs flat again. Good for product names, launches, "new" announcements.
**Format:** 1080×1920 (9:16), 30 fps · demo length 5 s · footage: No (colour stage).

![preview](poster.jpg)  ·  [preview.mp4](preview.mp4)

## Look
- A three-line block: big lime and white heavy sans (Inter 900) plus a small pink italic serif line (Instrument Serif).
- The block behaves like a flexible sheet: it curves smoothly in 3D, with shading that follows the bend (surfaces turned toward the light are brighter).
- When it rolls into a tube, the back of the sheet shows through, dim and mirrored, like a clear cylinder.
- Cobalt stage with a soft floor shadow.

## Motion language
- **Reveal:** the flat block opens from the centre outward with a small pop.
- **Bow:** it bends toward the camera (centre nearest, edges curving away) with a slight tilt.
- **Flex:** it flexes the other way into a concave curve, like a curved screen, while turning.
- **Roll:** it rolls up into a complete tube and spins once.
- **Spring flat:** it unrolls back to flat with an overshoot (back.out), holds, then rolls up again and shrinks away.

## Edit rhythm
~0.5 s reveal, ~0.8 s per bend, 1 s roll, 0.75 s spring-back, ~1 s hold, 0.6 s exit.

## Scene recipe
| Scene file | What it does |
| --- | --- |
| `compositions/bt1.html` | Block reveals, bows, flexes, rolls into a spinning tube, springs flat, rolls away. |

## What to swap
- Words: edit `LINES` in `generator.py`, then run `python3 generator.py && python3 ../../tools/build_index.py template` (the block is cut into 60 strips, each carrying a copy of the text, so editing by hand means changing all 60).
- Smoothness: `N` in `generator.py` (more strips = smoother curve, heavier page).
- Colours: `c1`, `c2`, `c3`, `stageLight`, `stageDeep`.
- The bends: `CONVEX`, `CONCAVE` (1 / radius in px) and `TUBE` in the script, and the `R({...})` steps that animate between them.

## How it works
The text block is sliced into thin vertical strips. Each strip is placed on a circle of curvature `k`: at arc position `s` it sits at angle `θ = s·k`, `x = sin θ / k`, `z = (cos θ − 1) / k`, turned by `θ`. Animating `k` from 0 (flat) through positive (bow), negative (concave) to `2π / width` (closed tube) bends the whole block.

## Build / render
```bash
cd styles/19-bend-text-3d/template
python3 ../../../tools/build_index.py .
npx hyperframes preview
npx hyperframes check
npx hyperframes render -o out.mp4
```
