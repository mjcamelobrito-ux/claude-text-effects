# claude-text-effects

40 vertical (9:16) kinetic text effects, inspired by reference reels and tutorials and rebuilt as editable [HyperFrames](https://hyperframes.heygen.com) templates (HTML + GSAP → MP4). Packaged as a Claude Code plugin: apply a style with `/video-style <style> <brief>`. Each style's shortcut is in the table below; the number works too (`/video-style 21`).

![overview](overview.jpg)

| # | Style | Shortcut | Best for | Footage |
|---|---|---|---|---|
| 01 | [Fisheye Sphere Text](styles/01-fisheye-sphere-text/STYLE.md) | `/video-style fisheye-sphere-text` | Hook titles on a fisheye sphere that snap-rolls line by line; gliding fisheye lens | — |
| 02 | [Paper Cut-out Text](styles/02-paper-cutout-text/STYLE.md) | `/video-style paper-cutout-text` | Bubble letters on torn paper: flutter / tear / stamp in, 12 fps stop motion | ✔ |
| 03 | [Depth & Orbit Text](styles/03-depth-orbit-text/STYLE.md) | `/video-style depth-orbit-text` | Words peek from behind the subject, helix climb, rising giant letters, depth tunnel | ✔ |
| 04 | [Word-Pop Captions](styles/04-word-pop-captions/STYLE.md) | `/video-style word-pop-captions` | Rolling one-word captions, marker underlines, cursor select, circle-reveal cards | ✔ |
| 05 | [Cube Roll Words](styles/05-cube-roll-words/STYLE.md) | `/video-style cube-roll-words` | Words on the faces of a 3D bar that tumbles in and rolls one face per beat | ✔ |
| 06 | [Blinds Unfold Text](styles/06-blinds-unfold-text/STYLE.md) | `/video-style blinds-unfold-text` | Giant words cut into slats that swing open like venetian blinds | — |
| 07 | [Domino Letters](styles/07-domino-letters/STYLE.md) | `/video-style domino-letters` | Thick extruded letters stand up like dominoes, then topple | — |
| 08 | [Split-Flap Board](styles/08-split-flap-board/STYLE.md) | `/video-style split-flap-board` | Departure-board tiles flip through letters into place | ✔ |
| 09 | [Extruded Title Orbit](styles/09-extruded-title-orbit/STYLE.md) | `/video-style extruded-title-orbit` | Thick 3D block title; camera orbits, snaps face-on with a glare | — |
| 10 | [Page Flip Words](styles/10-page-flip-words/STYLE.md) | `/video-style page-flip-words` | One word per page of an open book; pages turn on the spine | — |
| 11 | [Flag Wave Letters](styles/11-flag-wave-letters/STYLE.md) | `/video-style flag-wave-letters` | Letters ripple like a flag, then a gust blows them away | ✔ |
| 12 | [Cube Unfold Text](styles/12-cube-unfold-text/STYLE.md) | `/video-style cube-unfold-text` | A word on every face of a cube that unfolds flat into a cross | — |
| 13 | [Horizon Crawl](styles/13-horizon-crawl/STYLE.md) | `/video-style horizon-crawl` | Lines glide away over a neon grid floor; the hero word stands up | — |
| 14 | [Infinite Spiral Text](styles/14-infinite-spiral-text/STYLE.md) | `/video-style infinite-spiral-text` | A phrase streaming endlessly out of a spiral that fills the background | ✔ |
| 15 | [Wall Perspective Text](styles/15-wall-perspective-text/STYLE.md) | `/video-style wall-perspective-text` | Words painted on the side walls of a room, following their perspective | ✔ |
| 16 | [Bend Text 3D](styles/16-bend-text-3d/STYLE.md) | `/video-style bend-text-3d` | A headline on a flexible sheet that bends, rolls into a tube and springs flat | — |
| 17 | [Horizontal Orbit Text](styles/17-horizontal-orbit-text/STYLE.md) | `/video-style horizontal-orbit-text` | Upright letters on a horizontal ring orbiting the speaker like a carousel | ✔ |
| 18 | [3D Pop Letters](styles/18-3d-pop-letters/STYLE.md) | `/video-style 3d-pop-letters` | A flat word pops up into candy-coloured 3D blocks, spin-waves, sinks flat | — |
| 19 | [Tag Pile Drop](styles/19-tag-pile-drop/STYLE.md) | `/video-style tag-pile-drop` | Pill tags drop onto a table one by one into a heap, then fly back up | — |
| 20 | [Paper Roll Unfold](styles/20-paper-roll-unfold/STYLE.md) | `/video-style paper-roll-unfold` | The words themselves roll up like a paper roll and unroll top to bottom | — |
| 21 | [Snake Text](styles/21-snake-text/STYLE.md) | `/video-style snake-text` | A sentence slithering diagonally in the shape of a snake, last word as the head | — |
| 22 | [Contour Rings Text](styles/22-contour-rings-text/STYLE.md) | `/video-style contour-rings-text` | Lines of text nesting round the speaker's head like contour lines | ✔ |
| 23 | [Camera Lockup Type](styles/23-camera-lockup-type/STYLE.md) | `/video-style camera-lockup-type` | Words flip in to build a justified block while the camera frames each one | — |
| 24 | [Turning Camera Type](styles/24-turning-camera-type/STYLE.md) | `/video-style turning-camera-type` | A flush word puzzle with sideways words; the camera turns 90° to read each one | — |
| 25 | [Neon Outline Depth](styles/25-neon-outline-depth/STYLE.md) | `/video-style neon-outline-depth` | Neon outline type that extrudes into depth | — |
| 26 | [Wall Projection Words](styles/26-wall-projection-words/STYLE.md) | `/video-style wall-projection-words` | Words slam onto a tilted wall one beat at a time | — |
| 27 | [Ball Burst Letters](styles/27-ball-burst-letters/STYLE.md) | `/video-style ball-burst-letters` | A bouncing ball bursts into the word, then swallows it again | — |
| 28 | [Boxed Dot Stop](styles/28-boxed-dot-stop/STYLE.md) | `/video-style boxed-dot-stop` | A glowing dot draws the frame, then becomes the full stop the word slides out of | — |
| 29 | [Glow Search Bar](styles/29-glow-search-bar/STYLE.md) | `/video-style glow-search-bar` | A glowing pill grows into a search bar and the query types itself | — |
| 30 | [Rail Shot Letters](styles/30-rail-shot-letters/STYLE.md) | `/video-style rail-shot-letters` | Letters shoot along vertical rails into line, leaving coloured speed bars | — |
| 31 | [Gradient Bloom Words](styles/31-gradient-bloom-words/STYLE.md) | `/video-style gradient-bloom-words` | Each word blooms in from blur in its own flowing gradient with a matching glow | — |
| 32 | [Neon Capsule Word](styles/32-neon-capsule-word/STYLE.md) | `/video-style neon-capsule-word` | A red neon capsule tumbles in and becomes one letter, the rest of the word shoves out of it | — |
| 33 | [Sticker Lyric Beats](styles/33-sticker-lyric-beats/STYLE.md) | `/video-style sticker-lyric-beats` | One word per beat with a new colour and a big graphic shape | — |
| 34 | [Tumble Flip Letters](styles/34-tumble-flip-letters/STYLE.md) | `/video-style tumble-flip-letters` | Letters tumble in 3D space and flip into line to spell each word | — |
| 35 | [Vortex Ring Fly-Through](styles/35-vortex-ring-flythrough/STYLE.md) | `/video-style vortex-ring-flythrough` | A vortex of spinning text rings, the camera flies through to the title | — |
| 36 | [Golden Signature](styles/36-golden-signature/STYLE.md) | `/video-style golden-signature` | Gold script writes itself behind a glowing spark | — |
| 37 | [Horizon Arc Glow](styles/37-horizon-arc-glow/STYLE.md) | `/video-style horizon-arc-glow` | A glowing gradient horizon rises and the name fades up under it | — |
| 38 | [Grunge Poster Beats](styles/38-grunge-poster-beats/STYLE.md) | `/video-style grunge-poster-beats` | Distressed condensed words slam in at a tilt over a red globe grid | — |
| 39 | [Ribbon Ride Words](styles/39-ribbon-ride-words/STYLE.md) | `/video-style ribbon-ride-words` | Fat ribbons sweep across on an S-curve and each word rides its ribbon | — |
| 40 | [Shard Punch Zoom](styles/40-shard-punch-zoom/STYLE.md) | `/video-style shard-punch-zoom` | A white shard slices across and the camera punches into an extreme close-up | — |

Each style folder has `STYLE.md` (the spec), `template/` (the HyperFrames project), `preview.mp4` and `poster.jpg`.

## Use it

**As a plugin (Claude Code):**
```bash
/plugin marketplace add mjcamelobrito-ux/claude-text-effects   # or install from a local path
/video-style contour-rings-text "my clip: assets/talk.mp4"
```

**By hand:**
```bash
npm i -g hyperframes            # needs Node 18+, ffmpeg
cp -r styles/22-contour-rings-text/template my-clip
cp ~/footage/ep12.mp4 my-clip/assets/            # then set footageSrc in scenes.json
# edit copy in my-clip/compositions/*.html, timing in scenes.json
python3 tools/build_index.py my-clip
cd my-clip && npx hyperframes preview            # live editor
npx hyperframes check && npx hyperframes render -o ep12.mp4
```

## How a template is built

- `scenes.json` — scene order, durations, editable variables (brand colours), optional talking-head footage layer. `tools/build_index.py` turns it into `index.html`.
- `compositions/<scene>.html` — one scene per file, everything on a paused GSAP timeline (deterministic, frame-accurate). Captions and hard cuts use `tl.set` so seeking is exact.
- `assets/` — neutral placeholders (silhouette footage and subject cut-out) and the OFL Google fonts each style needs (e.g. Instrument Serif, Luckiest Guy, Lora, Inter Tight).

## Notes

- All on-screen text is **lorem ipsum** placeholder, sized like the original copy. `/video-style` replaces it with lines from your script or the transcript of the footage you give it.

- Reference videos are **not** included (they belong to their creators); each STYLE.md names its source.
- Placeholder art is intentionally plain; the style comes from type, colour, layout and timing. Swap in real cut-outs, footage and logos you have rights to.
- "Text behind the person" styles (03, 14, 17, 22) have a subject cut-out layer wired in (`cutoutSrc`); swap in a cut-out of your own speaker.
