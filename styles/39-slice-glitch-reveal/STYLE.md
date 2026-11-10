# 39 · Slice Glitch Reveal

**Origin:** inspired by a minimal line text tutorial, rebuilt with this repo's palette and its own motion.
**Best for:** Title cards: the words are cut into thin slices that drop into place with streaks and a red ghost.
**Format:** 1080×1920 (9:16), 30 fps · demo length 6 s · footage: No (colour stage).

![preview](poster.jpg)  ·  [preview.mp4](preview.mp4)

## Look
Heavy navy type on cream with a red multiply ghost copy and thin black streaks.

## Motion language
Each of 22 slices per line drops or rises into place at its own moment, trailing a streak and a red ghost that catches up; the exit slices everything out upward.

## Scene recipe
| Scene file | What it does |
| --- | --- |
| `compositions/s39.html` | Title cards. |

## What to swap
Lines: the `.ln` blocks. Slices: `N`.

## Build / render
```bash
cd styles/39-slice-glitch-reveal/template
python3 ../../../tools/build_index.py .
npx hyperframes check
npx hyperframes render -o out.mp4
```
