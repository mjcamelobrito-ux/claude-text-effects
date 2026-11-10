# 42 · Tumble Flip Letters

**Origin:** inspired by a 3D text flip tutorial, rebuilt with this repo's palette and its own motion.
**Best for:** Word sequences: letters tumble in 3D space and flip into line to spell each word.
**Format:** 1080×1920 (9:16), 30 fps · demo length 6 s · footage: No (colour stage).

![preview](poster.jpg)  ·  [preview.mp4](preview.mp4)

## Look
White heavy letters (first letter lime) on a deep navy stage.

## Motion language
Letters float scattered in 3D, tumbling on their own axes; on each beat they flip and fly into line, hold, then burst back to the scatter and re-form the next word.

## Scene recipe
| Scene file | What it does |
| --- | --- |
| `compositions/s42.html` | Word sequences. |

## What to swap
Words: `#s42-copy`. Timing: `STEP`, `FORM`, `HOLD`.

## Build / render
```bash
cd styles/42-tumble-flip-letters/template
python3 ../../../tools/build_index.py .
npx hyperframes check
npx hyperframes render -o out.mp4
```
