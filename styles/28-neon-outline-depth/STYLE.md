# 28 · Neon Outline Depth

**Origin:** inspired by a 3D glow outline text tutorial, rebuilt with this repo's palette and its own motion.
**Best for:** Logo reveals and channel names: neon outline type that extrudes into depth.
**Format:** 1080×1920 (9:16), 30 fps · demo length 6 s · footage: No (colour stage).

![preview](poster.jpg)  ·  [preview.mp4](preview.mp4)

## Look
Two lines of hollow neon tubes (heavy italic Montserrat): a clean gradient outline (pink → cobalt → sky) with a white-hot core and a soft glow. Eight thinner outlines stepped back in space form the 3D depth, hidden inside the front letters so the tubes stay readable.

## Motion language
The neon switches on with a few stutters, then the depth outlines fan out behind it while the extrusion direction swings left to right like a slow 3D turn. The gradient drifts through the tubes, with one small flicker mid-hold; finally the depth collapses and the sign fades.

## Scene recipe
| Scene file | What it does |
| --- | --- |
| `compositions/s28.html` | Logo reveals and channel names. |

## What to swap
Lines: `LINES` in the script. Depth: `N`. Tube thickness: the `dilate` radii in the `#s28-front` filter. Switch-on stutters: `FLICK`. Colours: `c1`–`c3` (gradient), `c4` (stage).

## Build / render
```bash
cd styles/28-neon-outline-depth/template
python3 ../../../tools/build_index.py .
npx hyperframes check
npx hyperframes render -o out.mp4
```

## How it works
The outline is not a stroke (strokes show the font's overlapping contours inside letters). Instead an SVG filter grows the filled glyphs with `feMorphology` and cuts the original glyphs out, giving one clean ring per letter, then adds blur glows and a thin white core. The depth layers use a thinner version of the same filter and sit under a mask that hides them inside the front letters.
