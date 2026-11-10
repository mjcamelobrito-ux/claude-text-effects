# 07 · Cube Roll Words

**Origin:** an original kinetic 3D text effect for this repo (not based on a reference reel).
**Best for:** Lower-third keywords and lists: four words on the faces of a solid 3D bar that tumbles in and rolls one face per beat.
**Format:** 1080×1920 (9:16), 30 fps · demo length 4.5 s · footage: Yes: a talking-head video plays underneath (`footageSrc`).

![preview](poster.jpg)  ·  [preview.mp4](preview.mp4)

## Look
- A long solid bar (cube) in the lower third, seen slightly from the side; one word per face.
- Each face is a solid colour block with heavy tight sans (Inter 900): lime, cobalt, pink, cream.
- Soft contact shadow under the bar.

## Motion language
- **Tumble in:** drops from above the frame spinning 200° on its long axis and lands.
- **Roll:** rolls forward 90° per word with a springy overshoot (back.out), so the next face comes to the front.
- **Drift:** the camera slowly swings around the bar (rotationY −16° → 14°) to keep the 3D alive.
- **Tumble out:** falls out of frame spinning.

## Edit rhythm
A word every ~0.85 s; 4 words per bar.

## Scene recipe
| Scene file | What it does |
| --- | --- |
| `compositions/cr1.html` | Bar tumbles in, rolls through 4 words, tumbles out. |

## What to swap
- Words: `cr1-f0` … `cr1-f3` (roll order).
- Face colours: `c1`, `c2`, `c3` (4th face cream in CSS).
- Bar size/position: `#cr1-cube` (faces are `translateZ(height / 2)`).
- Roll timing: the three `rotationX: 90 * k` tweens.

## Build / render
```bash
cd styles/07-cube-roll-words/template
python3 ../../../tools/build_index.py .
npx hyperframes preview
npx hyperframes check
npx hyperframes render -o out.mp4
```
