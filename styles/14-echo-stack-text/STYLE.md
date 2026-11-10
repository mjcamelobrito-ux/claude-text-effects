# 14 · Echo Stack Text

**Origin:** an original kinetic 3D text effect for this repo (not based on a reference reel).
**Best for:** Big brand words and launches: a word with a deep trail of outline echoes that collapse into one solid word.
**Format:** 1080×1920 (9:16), 30 fps · demo length 3.7 s · footage: No (colour stage).

![preview](poster.jpg)  ·  [preview.mp4](preview.mp4)

## Look
- A solid lime word (Archivo Black) in front of 11 outline echoes stepping back and down-right, fading pink → cobalt.
- Dark indigo stage; a small tracked-out line underneath.

## Motion language
- **Stack in:** the echoes fly out of the distance one after another, back of the stack first.
- **Orbit:** the camera swings around the stack (rotationY 30° → −30°) so its depth reads.
- **Collapse:** every echo snaps into the front word with a punch (scale 1.12 → 1).
- **Burst:** the echoes blow back out toward the camera and the word goes with them.

## Edit rhythm
0.7 s build, 1.6 s orbit, collapse + hold ~0.8 s, 0.35 s burst.

## Scene recipe
| Scene file | What it does |
| --- | --- |
| `compositions/es1.html` | Echo stack builds, orbits, collapses into one word, bursts out. |

## What to swap
- Word: same text in all 12 `es1-e*` copies (`es1-e0` is the solid front).
- Small line: `#es1-sub`.
- Colours: `c1`, `echo` (the ramp ends at cobalt in the script), `stageLight`, `stageDeep`. Depth: the `i * 46` / `i * 9` / `i * 7` offsets.

## Build / render
```bash
cd styles/14-echo-stack-text/template
python3 ../../../tools/build_index.py .
npx hyperframes preview
npx hyperframes check
npx hyperframes render -o out.mp4
```
