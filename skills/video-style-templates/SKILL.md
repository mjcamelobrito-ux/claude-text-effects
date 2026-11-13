---
name: video-style-templates
description: Apply one of 40 vertical kinetic text-effect styles (fisheye sphere text, paper cut-out text, depth & orbit text, word-pop captions, cube roll words, blinds unfold text, domino letters, split-flap board, extruded title orbit, page flip words, flag wave letters, cube unfold text, horizon crawl, infinite spiral text, wall perspective text, bend text 3d, horizontal orbit text, 3d pop letters, tag pile drop, paper roll unfold, snake text, contour rings text, camera lockup type, turning camera type, neon outline depth, wall projection words, ball burst letters, boxed dot stop, glow search bar, rail shot letters, gradient bloom words, neon capsule word, sticker lyric beats, tumble flip letters, vortex ring fly-through, golden signature, horizon arc glow, grunge poster beats, ribbon ride words, shard punch zoom) to a brief, script or footage using HyperFrames templates.
---

# Video style templates

Each style lives in `styles/<NN-slug>/`:

- `STYLE.md` — the style spec: reference, look (palette, type), motion language, edit rhythm, scene recipe, swap points. Read it before changing anything.
- `template/` — a HyperFrames project (1080×1920, 30 fps): `scenes.json` (scene order + durations + variables), `compositions/<scene>.html` (one scene per file, GSAP timeline), `assets/` (placeholder media + OFL fonts), generated `index.html`.
- `preview.mp4` / `poster.jpg` — rendered demo with placeholder content.

`styles/index.json` is the catalog (slug, name, best-for, needs footage, duration, variables).

## Applying a style

1. Pick the style (catalog). Styles marked `footage: true` need a talking-head clip; the rest are pure motion graphics.
2. Copy the template folder to a new project; never edit `styles/*/template` in place.
3. All on-screen text ships as lorem-ipsum placeholders. Replace it from the input: if the user gave footage, transcribe it first (`npx hyperframes transcribe <file>` or whisper) and pull caption chunks, hook lines and emphasis words from the transcript with their timings; otherwise use the brief/script. Keep each slot's word count and casing close to the placeholder so layouts hold. Map the brief/script to the scene recipe in STYLE.md: one idea per scene, keep the style's rhythm (beat lengths, caption chunk sizes, transition type). Add scenes by duplicating a scene file (rename its id everywhere: host id = scene root id = `data-composition-id` = timeline key; prefix element ids with the scene id) and listing it in `scenes.json`.
4. Swap media: footage → `assets/` + `footageSrc` default in `scenes.json`; cut-outs replace the placeholder PNGs at similar size; brand colours via the variables listed in STYLE.md.
5. Rebuild and verify:
   ```bash
   python3 tools/build_index.py <project>
   cd <project> && npx hyperframes check --json      # fix every error
   npx hyperframes snapshot --frames 8                # look at the frames
   npx hyperframes render -o <name>.mp4
   ```

## Rules that keep templates working

- Every animation lives on the scene's paused GSAP timeline; use `fromTo`, `tl.set` for hard on/off states (captions, frame-exact cuts). No timers, no unseeded randomness.
- Never put a CSS `transform` on an element GSAP transforms; animate transforms, not `left/top/width`.
- Fonts not bundled by HyperFrames need `@font-face` pointing at `assets/fonts/*.woff2` in each scene that uses them.
- Keep text inside the 168–1330 px vertical band (platform UI), min 28 px type.
- Text-behind-subject (styles 03, 14, 17, 22): the scene stacks back text → cut-out (`cutoutSrc`) → front text. The cut-out must match the footage; for moving footage use an alpha video (see STYLE.md).
- Placeholders (`speaker-*.mp4`, `subject-cutout*.png`, `object-sphere*.png`, `shot-*.jpg`, `ui-screen.png`) are neutral stand-ins: tell the user which ones remain in the final render.
