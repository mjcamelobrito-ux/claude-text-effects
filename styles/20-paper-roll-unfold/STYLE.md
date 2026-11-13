# 20 · Paper Roll Unfold

**Origin:** an original kinetic text effect for this repo.
**Best for:** Lists, steps and punchlines with a tactile, playful feel: the words themselves roll up like a paper roll and unroll from top to bottom. No paper, no roll graphic: only the type.
**Format:** 1080×1920 (9:16), 30 fps · demo length 5.4 s · footage: No (colour stage).

![preview](poster.jpg)  ·  [preview.mp4](preview.mp4)

## Look
- A column of four big words: cobalt block letters (Archivo Black) alternating with pink italic serif (Instrument Serif) on a lilac stage.
- While rolled, the words wind round a horizontal axis like a roll of paper: a see-through cylinder made of letters, its far side dimmed and mirrored.

## Motion language
- **Appear:** the tightly rolled words fade in at the top with a small drop.
- **Unroll:** the curl line travels down the column; above it the words lie flat and readable, below it they are still wound up. The roll thins as the words come off it, exactly like paper coming off the back of a roll.
- **Roll back up:** after a hold, the words roll back up from the bottom in one quick motion and vanish.

## Edit rhythm
0.4 s appear, 3 s unroll (≈0.75 s per word), ~0.9 s hold, 0.8 s roll-up.

## Scene recipe
| Scene file | What it does |
| --- | --- |
| `compositions/pr1.html` | Rolled words unroll down the screen into a flat column, hold, roll back up. |

## What to swap
- Words: `SHEETS` in `generator.py` (word + `sans`/`serif`), then `python3 generator.py && python3 ../../tools/build_index.py template`. The column is cut into 100 thin slices, each carrying a copy of the words, so editing by hand means editing all of them.
- Smoothness: `H` (slice height) in `generator.py`. Sheet spacing: `SH`.
- Roll size: `r` in the timeline (120 → 40 as it unrolls). Speed: the UNROLL tween duration.
- Colours: `c1`, `c2`, `stageLight`, `stageDeep`.

## How it works
Each slice sits at strip length `s`. Slices before the curl line `C` are flat. A slice past it, `u = s − C` along the strip, is wrapped round a roll of radius `r`: angle `φ = u / r`, `y = C + r sin φ`, `z = r cos φ − r`, turned by `φ`. Only the outer turn is shown. Animating `C` from 0 to the column length unrolls the words.

## Build / render
```bash
cd styles/20-paper-roll-unfold/template
python3 ../../../tools/build_index.py .
npx hyperframes preview
npx hyperframes check
npx hyperframes render -o out.mp4
```
