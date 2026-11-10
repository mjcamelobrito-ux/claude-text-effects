# 28 · Neon Outline Depth

**Origin:** inspired by a 3D glow outline text tutorial, rebuilt with this repo's palette and its own motion.
**Best for:** Logo reveals and channel names: neon outline type that extrudes into depth.
**Format:** 1080×1920 (9:16), 30 fps · demo length 6 s · footage: No (colour stage).

![preview](poster.jpg)  ·  [preview.mp4](preview.mp4)

## Look
Two lines of heavy italic outline type stroked with one flowing pink-cobalt-sky gradient and a neon glow; 11 outline copies stepped back in space form the 3D depth.

## Motion language
The outlines trace themselves on, then fan out into depth while the extrusion direction swings left to right like a slow 3D turn; the gradient drifts through the strokes; finally the copies collapse.

## Scene recipe
| Scene file | What it does |
| --- | --- |
| `compositions/s28.html` | Logo reveals and channel names. |

## What to swap
Lines: `LINES` in the script. Depth: `N`. Colours: `c1`–`c3` (gradient), `c4` (stage).

## Build / render
```bash
cd styles/28-neon-outline-depth/template
python3 ../../../tools/build_index.py .
npx hyperframes check
npx hyperframes render -o out.mp4
```
