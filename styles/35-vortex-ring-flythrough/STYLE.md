# 35 · Vortex Ring Fly-Through

**Origin:** inspired by a cinematic camera text tutorial, rebuilt with this repo's palette and its own motion.
**Best for:** Openers: a vortex of spinning text rings, the camera flies through to the title.
**Format:** 1080×1920 (9:16), 30 fps · demo length 6 s · footage: No (colour stage).

![preview](poster.jpg)  ·  [preview.mp4](preview.mp4)

## Look
Navy text on rings tilted in 3D on a light grey stage; title in navy and cobalt.

## Motion language
Rings spin in alternate directions; the camera flies forward through them (each ring swells past the lens and fades) and the title appears in the calm centre.

## Scene recipe
| Scene file | What it does |
| --- | --- |
| `compositions/s43.html` | Openers. |

## What to swap
Rings: `#s43-copy` (`data-r` radius, `data-s` size). Title: `.title`.

## Build / render
```bash
cd styles/35-vortex-ring-flythrough/template
python3 ../../../tools/build_index.py .
npx hyperframes check
npx hyperframes render -o out.mp4
```
