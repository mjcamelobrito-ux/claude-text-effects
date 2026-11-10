# 35 · Tag Pile Drop

**Inspired by:** the "Stacking Animation" After Effects tutorial (pill tags dropping onto the screen and piling up). The idea is borrowed; the palette, star badges, landing jolts and un-stack exit are this repo's own.
**Best for:** Lists of benefits, features, keywords or hashtags, "everything you get" moments, and myth-busting reels where a pile of claims builds up.
**Format:** 1080×1920 (9:16), 30 fps · demo length ~5 s · footage: No (table surface).

![preview](poster.jpg)  ·  [preview.mp4](preview.mp4)

## Look
- Top-down view of a light table; pill-shaped tags with short phrases (Inter 800) in navy, cobalt, white, lime and pink, plus round star badges.
- Each tag casts a soft shadow; the finished heap overlaps naturally but most phrases stay readable.

## Motion language
- **Drop:** each tag falls from above the camera onto the table: it starts huge, blurred and spinning with a far, faint shadow, and lands at rest size with a squash while its shadow tightens underneath. Later tags land on top.
- **Jolt:** the whole heap gives a tiny jolt on every landing.
- **Un-stack:** the camera lifts and the tags fly back up past the lens, top of the heap first.

## Edit rhythm
A tag every 0.17 s (16 tags ≈ 2.7 s), ~0.9 s hold, ~1.3 s un-stack.

## Scene recipe
| Scene file | What it does |
| --- | --- |
| `compositions/tp1.html` | 16 tags drop one by one into a heap, hold, fly back up past the camera. |

## What to swap
- Phrases: edit the text inside each `.pill` (pills grow to fit; shadows refit automatically). `✦` tags are round badges.
- A new heap (count, positions, rotations): `TAGS` / `STY` and the random seed in `tools/generate_34_35.py`, then rerun it and `build_index.py`. Positions are spaced out by rejection sampling so text stays readable.
- Table colour: `table`. Drop speed: the `0.17` stagger and `0.34` fall time in the script.

## Build / render
```bash
cd styles/35-tag-pile-drop/template
python3 ../../../tools/build_index.py .
npx hyperframes preview
npx hyperframes check
npx hyperframes render -o out.mp4
```
