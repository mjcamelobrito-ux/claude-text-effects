# 19 · Halo Orbit Text

**Origin:** the orbit scene from style 16's first version, kept on its own as a single text effect (the ring of words was itself inspired by the word spiral in "How to do the 3D text effect… straight sauce ep 1").
**Best for:** A one-line hook or question that circles the speaker's head like a halo; quick, punchy intros.
**Format:** 1080×1920 (9:16), 30 fps · demo length 2.8 s · footage: Yes (`footageSrc`) **plus a subject cut-out** (`cutoutSrc`) so the back of the ring passes behind the person.

![preview](poster.jpg)  ·  [preview.mp4](preview.mp4)

## Look
- Nine words evenly spaced on a circle around the head, each baseline following the curve.
- The ring is tilted back 62° in 3D, so it reads as a flat halo: the front half crosses in front of the face/neck, the back half goes behind the head (dimmed to 85 %).
- Medium tight sans (Inter 700), white, soft shadow.

## Motion language
- **Pop in:** the ring scales up from 45 % and fades in (0.6 s, expo out).
- **Orbit:** it spins 190° around the head (power1 in-out) while slowly growing to 115 %.
- **Fly out:** it scales past the camera to 220 % and fades (0.35 s, power3 in).

## Edit rhythm
One ring per line of speech, ~2.8 s. Chain several rings for a list (new words each time).

## Scene recipe
| Scene file | What it does |
| --- | --- |
| `compositions/ho1.html` | Ring of 9 words pops in, orbits the head, flies out past the camera. |

## What to swap
- Words: the `ho1-b*` (back) and `ho1-f*` (front) lists; keep both identical. More or fewer words: change both lists and `N`.
- Shape: `R` (ring radius, px), `TILT` (degrees); centre: `.ring` `left/top` (sit it on the head).
- Speed/amount of spin: the `spin` tween (`-40 → 150`).
- Footage `footageSrc`, cut-out `cutoutSrc` (must line up with the footage; for a moving subject use an alpha video, see style 16's notes). Colour: `ink`.

## Build / render
```bash
cd styles/19-halo-orbit-text/template
python3 ../../../tools/build_index.py .
npx hyperframes preview
npx hyperframes check
npx hyperframes render -o out.mp4
```
