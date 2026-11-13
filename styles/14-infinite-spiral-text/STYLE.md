# 14 · Infinite Spiral Text

**Origin:** an original kinetic 3D-feel text effect for this repo (not based on a reference reel).
**Best for:** Hypnotic backgrounds behind a talking head: a slogan, brand line or keyword list streaming out of a spiral that never ends. Works as a hook or as a full-length background loop.
**Format:** 1080×1920 (9:16), 30 fps · demo length 6 s (loops seamlessly for any length) · footage: Yes (`footageSrc`) **plus a subject cut-out** (`cutoutSrc`) so the person stays in front of the spiral.

![preview](poster.jpg)  ·  [preview.mp4](preview.mp4)

## Look
- One phrase repeated along a **logarithmic spiral** centred behind the head and filling the whole frame.
- Letter size grows with distance from the centre, so every turn is the same picture scaled up (self-similar): tiny letters near the centre, huge letters bleeding off the frame edges.
- Heavy sans (Inter 900); words take three colours in turn (white, lime, pink). The footage is dimmed 55 % under the spiral, and a soft dark well hides the noisy centre.

## Motion language
- **Endless outflow:** the phrase slides along the spiral, so words are born tiny in the middle, swirl outward and grow until they leave the frame. Because the spiral is self-similar there is no loop point: it can run for any length.
- **Counter-turn:** the whole spiral turns slowly the other way (−0.6 rad over 6 s) for a hypnotic feel.
- **Pour in:** at the start it fades up while scaling out of the centre (35 % → 100 %). **Zoom out:** at the end it rushes past the camera.

## Edit rhythm
Continuous; at the default speed a word travels one full turn in ~3.7 s.

## Scene recipe
| Scene file | What it does |
| --- | --- |
| `compositions/is1.html` | Infinite spiral behind the subject: pour in, endless flow, zoom out. |

## What to swap
- Phrase: `#is1-copy` (it repeats endlessly; end it with a separator like ` · `).
- Colours: `c1`, `c2`, `c3` (words cycle through them).
- Shape and speed: `GROW` (how much bigger each turn is; 1.2 = tight, 1.6 = loose), `SPEED` (flow, radians/s; negative = flow inward), `CX`/`CY` (spiral centre: put it behind the head).
- Length: change the scene duration and the `t`/`spin` tween to match; the flow never repeats visibly.
- Footage `footageSrc`, cut-out `cutoutSrc` (must line up with the footage; for a moving subject use an alpha video, see style 03's notes). Remove `#is1-cut` to put the spiral in front of everything.

## Build / render
```bash
cd styles/14-infinite-spiral-text/template
python3 ../../../tools/build_index.py .
npx hyperframes preview
npx hyperframes check
npx hyperframes render -o out.mp4
```
