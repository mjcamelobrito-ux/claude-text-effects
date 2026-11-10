# 09 · AI-World Kinetic Type

**Reference:** "Comment invideo and I'll send you the free access…" (invideo launch reel)
**Best for:** Launch/announcement reels with a presenter in AI-generated or surreal environments; high-energy creator promos.
**Format:** 1080×1920 (9:16), 30 fps · demo length 10.2 s · footage: Yes: a talking-head video plays under every scene (`footageSrc`).

![preview](poster.jpg)  ·  [preview.mp4](preview.mp4)

## Look
- Presenter footage composited into AI-generated worlds (race track, floating island, giant timeline).
- Every word is its own object: own font (bold sans, Didone, Instrument Serif, Yellowtail script, Anton), own colour (yellow, cyan, red, violet, white) and own 3D angle.
- Words orbit the subject: stacked in a staggered column, rotated 90°, even upside-down.
- Extruded serif headlines with stacked shadows ('JUST LAUNCHED').

## Motion language
- Words fly in from depth (z −1000) with big Y/X rotations, settling at a residual tilt.
- Whole stacks drift as if floating in the scene.
- Exits push toward camera (z +400–600) or whip off with blur.

## Edit rhythm
One word every 0.3 s; stacks of 4–6 words; scenes 2–3 s.

## Scene recipe
All on-screen copy is lorem-ipsum placeholder sized like the reference; quotes below describe what each slot held in the reference reel. Replace it with lines from your script or the footage transcript, keeping roughly the same word count per slot.

| Scene file | What it does |
| --- | --- |
| `compositions/ak1.html` | 'Editing isn't a race… but now Fast'. |
| `compositions/ak2.html` | Extruded 'JUST LAUNCHED'. |
| `compositions/ak3.html` | Six-word multicolour stack. |
| `compositions/ak4.html` | Rotated 'in plain words' + comment CTA. |

## What to swap
- Footage: `footageSrc` (generate the world with your AI video tool, keep the presenter centred).
- Colours: `c1`–`c4`.
- Keyword in `ak4.html`.
- Editable variables (HyperFrames Variables panel): `c1`, `c2`, `c3`, `c4`.

## Build / render
```bash
cd styles/09-ai-world-kinetic-type/template
python3 ../../../tools/build_index.py .   # after reordering/retiming scenes.json
npx hyperframes preview                    # live preview / edit
npx hyperframes check                      # lint + layout audit
npx hyperframes render -o out.mp4          # final render
```
