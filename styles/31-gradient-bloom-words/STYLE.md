# 31 · Gradient Bloom Words

**Origin:** inspired by a colorful gradient text fade tutorial, rebuilt with this repo's palette and its own motion.
**Best for:** Word-by-word reveals: each word blooms in from blur in its own flowing gradient with a matching glow.
**Format:** 1080×1920 (9:16), 30 fps · demo length 6 s · footage: No (colour stage).

![preview](poster.jpg)  ·  [preview.mp4](preview.mp4)

## Look
One centred word at a time on a deep plum stage, each with its own three-colour gradient and glow.

## Motion language
Letters bloom in from blur, scale and drop in a soft wave while the gradient flows through them; the word dissolves to the right as the next one blooms.

## Scene recipe
| Scene file | What it does |
| --- | --- |
| `compositions/s38.html` | Word-by-word reveals. |

## What to swap
Words: the `.wd` blocks (`data-g` = gradient colours).

## Build / render
```bash
cd styles/31-gradient-bloom-words/template
python3 ../../../tools/build_index.py .
npx hyperframes check
npx hyperframes render -o out.mp4
```
