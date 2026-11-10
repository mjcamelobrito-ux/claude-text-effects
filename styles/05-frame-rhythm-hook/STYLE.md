# 05 · Frame-Rhythm Hook

**Reference:** "Try out this sequence in your next video to really hook people — 8, 3, 3, 4, 5 and then one…"
**Best for:** Educational talking-head reels for editors/creators; any hook that needs a jolt in the first 3 seconds.
**Format:** 1080×1920 (9:16), 30 fps · demo length 9.2 s · footage: Yes: a talking-head video plays under every scene (`footageSrc`).

![preview](poster.jpg)  ·  [preview.mp4](preview.mp4)

## Look
- Dark moody talking head, low-key light, desaturated.
- One word on screen at a time, centre-low, white bold sans; emotional words switch to italic serif.
- Key noun flashes as a giant glowing condensed title (Bebas Neue) above the head.
- Inserts: white card with a small B&W photo and one-word label; editor-timeline UI with coloured clips and a big timecode.

## Motion language
- Captions hard on / hard off with a 0.1 s scale pop.
- B-roll burst cut to exact frame counts: 8, 3, 3, 4, 5 frames (30 fps), then a ~1 s held card.
- Micro push-ins on each insert so even 3-frame shots move.
- Timeline panel drops from top; clips snap on with `back.out(3)`; playhead runs linear.
- Ending: vignette closes in (reads as a punch-in) + italic serif last word.

## Edit rhythm
Words every 0.2–0.4 s; burst of 23 frames; then calmer 0.7–1 s caption groups.

## Scene recipe
All on-screen copy is lorem-ipsum placeholder sized like the reference; quotes below describe what each slot held in the reference reel. Replace it with lines from your script or the footage transcript, keeping roughly the same word count per slot.

| Scene file | What it does |
| --- | --- |
| `compositions/fr1.html` | Word-per-beat captions + HOOK flash. |
| `compositions/fr2.html` | Frame-exact burst 8-3-3-4-5 + card hold. |
| `compositions/fr3.html` | Timeline UI explainer with captions. |
| `compositions/fr4.html` | Vignette punch + closing word. |

## What to swap
- Footage: `footageSrc`.
- Burst inserts: replace the `.fr2-cut` contents with your B-roll stills/clips; edit the `cuts` frame list.
- Timeline colours: `clipA`, `clipB`.
- Editable variables (HyperFrames Variables panel): `clipA`, `clipB`.

## Build / render
```bash
cd styles/05-frame-rhythm-hook/template
python3 ../../../tools/build_index.py .   # after reordering/retiming scenes.json
npx hyperframes preview                    # live preview / edit
npx hyperframes check                      # lint + layout audit
npx hyperframes render -o out.mp4          # final render
```
