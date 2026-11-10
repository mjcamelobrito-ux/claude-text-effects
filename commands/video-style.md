---
description: Apply one of the 27 video editing styles to a brief, script or footage (vertical 9:16, HyperFrames)
argument-hint: <style slug or name> [brief / script / footage path]
---

Apply the video editing style **$ARGUMENTS**.

1. Load the `video-style-templates` skill and follow it.
2. Resolve the style from `styles/index.json` (match slug, number or name loosely, e.g. "podcast", "05", "poster pink"). If nothing matches or no style was given, list the 27 styles with their "best for" line and ask which one.
3. Copy `styles/<slug>/template/` to a new project folder named after the brief (never edit the template in place).
4. Read `styles/<slug>/STYLE.md`. All text in the template is lorem ipsum: if footage was given, transcribe it and time captions/emphasis words to the speech; otherwise take lines from the brief. Rewrite the copy, timing and assets in the scene files to fit the user's brief/script, keeping the style's look, motion language and rhythm. Swap footage/images the user supplied into `assets/`.
5. `python3 tools/build_index.py <project>` after any change to `scenes.json`, then `npx hyperframes check`, fix errors, snapshot and review, render with `npx hyperframes render`.
6. Deliver the MP4 and say in one line what was swapped and what still uses placeholders.
