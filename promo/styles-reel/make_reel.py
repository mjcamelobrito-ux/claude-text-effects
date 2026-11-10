"""Generate compositions/reel.html: the whole promo as one scene, timed to Maria's VO (assets/maria.mp4).

Timeline (from `npx hyperframes transcribe assets/maria.mp4`):
  0 – NAMES_IN       hook, full-frame speaker + title + numbered list
  NAMES_IN – END     speaker shrinks to a face circle under the list; the style being named plays full-screen behind
  END – CTA          speaker full-frame again, "single repo" captions
  CTA – TOTAL        moving grid of all templates behind, face circle again, comment STYLES
  The style plays in a hand-held phone; a blurred copy fills the background.
Edit the times below and re-run: python3 make_reel.py && python3 ../../tools/build_index.py .
"""
NAMES = ["The Recipe", "The Magazine", "The Demo Drop", "The Billboard", "8-3-3-4-5", "The Blueprint", "The Stamp",
         "Glasshouse", "Word Orbit", "Object Lesson", "The Gallery", "Golden Fog", "The Tearjerker"]
STARTS = [2.63, 3.65, 4.75, 6.06, 6.80, 8.83, 9.98, 10.88, 12.02, 13.32, 15.24, 16.20, 17.13]
END = 18.60          # names finished
CTA = 24.35          # "Comment styles…"
TOTAL = 27.46
# captions between END and CTA: (text, in, out, emphasis?)
CAPS = [("i turned every one of them", 18.80, 20.50, False),
        ("into a single", 20.50, 21.90, False), ("repo.", 21.39, 21.90, True),
        ("you pick the style,", 21.90, 23.10, False),
        ("claude edits", 23.10, 24.30, False), ("the video.", 23.70, 24.30, True)]
# face circle: source face centre and where it goes
FACE_X, FACE_Y = 530, 670     # face centre in the source frame
R0 = 300                      # crop radius in source pixels
SCALE = 0.7                   # circle size (0.7 = 30% smaller than the 300 px circle)
PIP = (860, 1640)             # face-circle centre while the phone plays (bottom-right, over the phone corner)
CTA_POS = (540, 1250)         # face-circle centre during the CTA
PH_X, PH_Y, PH_W, PH_H = 255, 790, 540, 960   # phone card (bigger than before)
LEFT = 7
N = len(NAMES)

def item(i, n):
    return f'<div id="rl-i{i:02d}" class="rl-item"><span class="rl-n">{i:02d}</span>{n}</div>'

left = "\n        ".join(item(i + 1, n) for i, n in enumerate(NAMES[:LEFT]))
right = "\n        ".join(item(i + 1 + LEFT, n) for i, n in enumerate(NAMES[LEFT:]))
bgs = "\n    ".join(
    f'<video id="rl-bg{i+1:02d}" class="clip rl-bg" src="assets/bgblur/{i+1:02d}.mp4" muted playsinline '
    f'data-start="{STARTS[i]:.2f}" data-duration="{(STARTS[i+1] if i < N-1 else END) - STARTS[i] + 0.1:.2f}" data-track-index="{2+i}"></video>'
    for i in range(N))

phones = "\n      ".join(
    f'<video id="rl-p{i+1:02d}" class="clip rl-pv" src="assets/clips/{i+1:02d}.mp4" muted playsinline '
    f'data-start="{STARTS[i]:.2f}" data-duration="{(STARTS[i+1] if i < N-1 else END) - STARTS[i] + 0.1:.2f}" data-track-index="{40+i}"></video>'
    for i in range(N))
RR = int(R0 * SCALE)

# CTA grid (same layout as before)
COLS, ROWS, TW, TH, GAP = 4, 5, 290, 516, 16
gdur = round(TOTAL - CTA, 2)
cols = []
for c in range(COLS):
    tiles = "".join(
        f'<div class="rl-tile"><video id="rl-g{c}{r}" class="clip rl-gv" src="assets/grid/{(c + COLS*r) % N + 1:02d}.mp4" muted playsinline '
        f'data-start="{CTA}" data-duration="{gdur}" data-track-index="{20 + c*ROWS + r}"></video></div>' for r in range(ROWS))
    cols.append(f'<div id="rl-col{c}" class="rl-col" style="left:{c*(TW+GAP)}px">{tiles}</div>')
grid_w = COLS * TW + (COLS - 1) * GAP

# ---- sound: music bed under the voice + one effect per visible action (peak lands 1 frame after the picture)
MUSIC_VOL, SFX_VOL, VOICE_VOL = 0.175, 0.56, 1.25
PEAK = {"whoosh": 0.162, "whoosh-b": 0.141, "pop": 0.119, "pop-b": 0.147, "impact-bass-2": 0.795}
LEN = {"whoosh": 0.57, "whoosh-b": 0.5, "pop": 0.72, "pop-b": 0.89, "impact-bass-2": 2.59}
F = 1 / 30
TAKES = ["whoosh", "pop", "whoosh-b", "pop-b"]                          # rotate takes so repeats don't read as a template
cues = [(TAKES[i % 4], t) for i, t in enumerate(STARTS)]                  # each style lands in the phone (first one = phone rising in)
cues += [("whoosh", END + 0.0), ("pop", 21.39), ("impact-bass-2", CTA + 0.05)]  # phone out, "repo.", grid reveal
sfx_html = "\n    ".join(
    f'<audio id="rl-sfx{k:02d}" class="clip" src="assets/sfx/{n}.mp3" data-start="{max(0, t + F - PEAK[n]):.3f}" '
    f'data-duration="{LEN[n]:.2f}" data-volume="{(0.75 if n == "impact-bass-2" else SFX_VOL)}" data-track-index="{70 + k}"></audio>'
    for k, (n, t) in enumerate(cues))
music_html = (f'<audio id="rl-music" class="clip" src="assets/bgm/track.mp3" data-start="0" data-duration="{TOTAL}" '
              f'data-volume="{MUSIC_VOL}" data-fade-out="1.2" data-timeline-role="music" data-track-index="69"></audio>')

caps_html = "\n    ".join(
    f'<div id="rl-c{k}" class="rl-cap {"rl-emph" if e else "rl-line"}">{t}</div>' for k, (t, a, b, e) in enumerate(CAPS))

html = f"""<template>
  <style>
    #reel {{ position: absolute; inset: 0; overflow: hidden; background: #0b0b0b; font-family: Inter, sans-serif; }}
    .rl-bg {{ position: absolute; left: 0; top: 0; width: 1080px; height: 1920px; object-fit: cover; z-index: 1; }}
    #rl-grid {{ position: absolute; left: {(1080 - grid_w)//2}px; top: -380px; width: {grid_w}px; height: 2700px; z-index: 2; opacity: 0; }}
    .rl-col {{ position: absolute; top: 0; width: {TW}px; display: flex; flex-direction: column; gap: {GAP}px; }}
    .rl-tile {{ position: relative; width: {TW}px; height: {TH}px; border-radius: 22px; overflow: hidden; background: #1a1a1a; box-shadow: 0 16px 40px rgba(0,0,0,.45); }}
    .rl-gv {{ position: absolute; left: 0; top: 0; width: {TW}px; height: {TH}px; object-fit: cover; }}
    #rl-dim {{ position: absolute; inset: 0; z-index: 3; background: linear-gradient(rgba(0,0,0,.55), rgba(0,0,0,.15) 45%, rgba(0,0,0,.35)); opacity: 0; }}
    /* speaker layer: full frame, clipped down to a face circle when the styles play */
    #rl-face {{ position: absolute; left: 0; top: 0; width: 1080px; height: 1920px; z-index: 5; clip-path: circle(1400px at {FACE_X}px {FACE_Y}px); }}
    #rl-vid {{ position: absolute; left: 0; top: 0; width: 1080px; height: 1920px; object-fit: cover; }}
    #rl-phone {{ position: absolute; left: {PH_X}px; top: {PH_Y}px; width: {PH_W}px; height: {PH_H}px; z-index: 4; border-radius: 40px; border: 6px solid rgba(255,255,255,.94); overflow: hidden; background: #000; box-shadow: 0 34px 80px rgba(0,0,0,.6); opacity: 0; }}
    .rl-pv {{ position: absolute; left: 0; top: 0; width: {PH_W - 12}px; height: {PH_H - 12}px; object-fit: cover; }}
    #rl-pbadge {{ position: absolute; left: 24px; top: 24px; z-index: 60; padding: 6px 16px; border-radius: 20px; background: rgba(0,0,0,.6); color: #fff; font-weight: 700; font-size: 28px; }}
    #rl-pbadge .rl-cnt {{ left: 16px; top: 6px; }}
    #rl-sizer {{ visibility: hidden; }}
    #rl-ring {{ position: absolute; left: {-RR - 7}px; top: {-RR - 7}px; width: {2*RR + 14}px; height: {2*RR + 14}px; border-radius: 50%; border: 7px solid var(--hi, #f5e04a); box-shadow: 0 20px 60px rgba(0,0,0,.5); z-index: 6; opacity: 0; }}
    #rl-shade {{ position: absolute; left: 0; right: 0; top: 0; height: 1000px; z-index: 3; background: linear-gradient(rgba(0,0,0,.72), rgba(0,0,0,.45) 60%, rgba(0,0,0,0)); }}
    #rl-title {{ position: absolute; left: 0; right: 0; top: 230px; z-index: 7; text-align: center; font-weight: 900; font-size: 84px; line-height: .98; letter-spacing: -0.055em; color: #fff; text-shadow: 0 4px 24px rgba(0,0,0,.45); }}
    #rl-title b {{ display: inline-block; color: var(--hi, #f5e04a); font-weight: 900; }}
    .rl-colist {{ position: absolute; top: 450px; z-index: 7; padding: 18px 26px 18px 20px; border-radius: 22px; background: rgba(12,12,12,.78); backdrop-filter: blur(8px); }}
    #rl-left {{ left: 40px; }} #rl-right {{ right: 40px; }}
    .rl-item {{ font-weight: 700; font-size: 34px; line-height: 1.32; letter-spacing: -0.03em; color: rgba(255,255,255,.66); white-space: nowrap; transform-origin: 0 50%; }}
    .rl-n {{ display: inline-block; width: 46px; font-size: 24px; font-weight: 700; color: rgba(255,255,255,.7); letter-spacing: 0; }}
    .rl-cnt {{ position: absolute; opacity: 0; }}
    .rl-cap {{ position: absolute; left: 0; right: 0; z-index: 8; text-align: center; font-weight: 900; letter-spacing: -0.055em; opacity: 0; text-shadow: 0 4px 22px rgba(0,0,0,.5); }}
    .rl-line {{ top: 1000px; font-size: 76px; color: #fff; }}
    .rl-emph {{ top: 1080px; font-size: 118px; color: var(--hi, #f5e04a); }}
    #rl-cmt {{ position: absolute; left: 0; right: 0; top: 560px; z-index: 8; text-align: center; font-weight: 900; font-size: 120px; letter-spacing: -0.055em; color: #fff; opacity: 0; text-shadow: 0 6px 30px rgba(0,0,0,.6); }}
    #rl-cmt b {{ color: var(--hi, #f5e04a); font-weight: 900; }}
    #rl-sub {{ position: absolute; left: 0; right: 0; top: 715px; z-index: 8; text-align: center; font-weight: 700; font-size: 50px; letter-spacing: -0.04em; color: #fff; opacity: 0; text-shadow: 0 3px 16px rgba(0,0,0,.7); }}
  </style>
  <div id="reel" data-composition-id="reel" data-width="1080" data-height="1920">
    {bgs}
    <div id="rl-grid" data-layout-allow-overflow data-layout-ignore>
      {"".join(cols)}
    </div>
    <div id="rl-dim"></div>
    <div id="rl-face" data-layout-ignore>
      <video id="rl-vid" class="clip" src="assets/maria.mp4" data-has-audio="true" data-volume="{VOICE_VOL}" playsinline data-start="0" data-duration="{TOTAL}" data-track-index="1"></video>
    </div>
    <div id="rl-ring"></div>
    <div id="rl-shade"></div>
    <div id="rl-title"><b>13</b> video styles<br/>Claude can create</div>
    <div id="rl-left" class="rl-colist">
        {left}
    </div>
    <div id="rl-right" class="rl-colist">
        {right}
    </div>
    <div id="rl-phone">
      {phones}
      <div id="rl-pbadge"><span id="rl-sizer">00/{N}</span>{''.join(f'<span id="rl-k{i+1:02d}" class="rl-cnt">{i+1:02d}/{N}</span>' for i in range(N))}</div>
    </div>
    {caps_html}
    {music_html}
    {sfx_html}
    <div id="rl-cmt">comment <b>STYLES</b></div>
    <div id="rl-sub">and i'll send you the link.</div>
  </div>
  <script>
    const tl = gsap.timeline({{ paused: true }});
    const STARTS = {STARTS}, END = {END}, CTA = {CTA}, N = {N};
    const FULL = "circle(1400px at {FACE_X}px {FACE_Y}px)", SMALL = "circle({R0}px at {FACE_X}px {FACE_Y}px)";
    gsap.set("#rl-face", {{ transformOrigin: "{FACE_X}px {FACE_Y}px" }});
    const shrink = (t, cx, cy) => {{
      tl.fromTo("#rl-face", {{ clipPath: FULL, x: 0, y: 0, scale: 1 }}, {{ clipPath: SMALL, x: cx - {FACE_X}, y: cy - {FACE_Y}, scale: {SCALE}, duration: 0.45, ease: "expo.inOut" }}, t);
      tl.set("#rl-ring", {{ x: cx, y: cy }}, t);
      tl.fromTo("#rl-ring", {{ opacity: 0, scale: 1.3 }}, {{ opacity: 1, scale: 1, duration: 0.3, ease: "back.out(2)" }}, t + 0.3);
    }};
    const grow = (t, cx, cy) => {{
      tl.to("#rl-ring", {{ opacity: 0, duration: 0.15 }}, t);
      tl.fromTo("#rl-face", {{ clipPath: SMALL, x: cx - {FACE_X}, y: cy - {FACE_Y}, scale: {SCALE} }}, {{ clipPath: FULL, x: 0, y: 0, scale: 1, duration: 0.45, ease: "expo.inOut" }}, t);
    }};
    // hook: the number pops as it is said
    tl.fromTo("#rl-title b", {{ scale: 1.5 }}, {{ scale: 1, duration: 0.3, ease: "back.out(3)" }}, 0.1);
    // names: face circle under the list, style plays full-screen behind
    shrink(STARTS[0] - 0.35, {PIP[0]}, {PIP[1]});
    tl.fromTo("#rl-shade", {{ opacity: 0.6 }}, {{ opacity: 1, duration: 0.3 }}, STARTS[0] - 0.35);
    // the phone rises (from below, behind the face circle) and keeps a hand-held wobble
    tl.fromTo("#rl-phone", {{ opacity: 1, y: 1100, rotation: -6 }}, {{ opacity: 1, y: 0, rotation: -2, duration: 0.5, ease: "expo.out" }}, STARTS[0] - 0.4);
    for (let k = 0; k < 15; k++) tl.to("#rl-phone", {{ y: (k % 2 ? -8 : 8), rotation: (k % 2 ? -1 : -3), duration: 1, ease: "sine.inOut" }}, STARTS[0] + 0.1 + k);
    for (let i = 1; i <= N; i++) {{
      const id = "#rl-i" + String(i).padStart(2, "0"), k = "#rl-k" + String(i).padStart(2, "0");
      const a = STARTS[i - 1], b = i < N ? STARTS[i] : END;
      tl.set(id, {{ color: "#f5e04a", scale: 1.08 }}, a);
      tl.set(id, {{ color: "rgba(255,255,255,.66)", scale: 1 }}, b);
      tl.set(k, {{ opacity: 1 }}, a); tl.set(k, {{ opacity: 0 }}, b);
      // tiny punch-in on the phone for every new style
      tl.fromTo("#rl-phone", {{ scale: 1.04 }}, {{ scale: 1, duration: 0.2, ease: "power2.out" }}, a);
    }}
    // after the names: list clears, speaker returns full-frame for the captions
    tl.to(["#rl-title", ".rl-colist"], {{ opacity: 0, y: -40, filter: "blur(10px)", duration: 0.3, ease: "power2.in" }}, END - 0.1);
    tl.to("#rl-phone", {{ y: 1400, rotation: 8, duration: 0.35, ease: "power3.in" }}, END - 0.15);
    tl.to("#rl-shade", {{ opacity: 0, duration: 0.3 }}, END - 0.1);
    grow(END - 0.1, {PIP[0]}, {PIP[1]});
    {chr(10).join(f'    tl.fromTo("#rl-c{k}", {{ opacity: 0, scale: 1.15, filter: "blur(10px)" }}, {{ opacity: 1, scale: 1, filter: "blur(0px)", duration: 0.18, ease: "power3.out" }}, {a}); tl.set("#rl-c{k}", {{ opacity: 0 }}, {b});' for k, (t, a, b, e) in enumerate(CAPS)).strip()}
    // CTA: template grid fades in behind, face circle again, comment STYLES
    tl.fromTo("#rl-grid", {{ opacity: 0, scale: 1.6, rotation: -14 }}, {{ opacity: 1, scale: 1, rotation: -8, duration: 0.5, ease: "expo.out" }}, CTA);
    for (let c = 0; c < {COLS}; c++) {{ const d = c % 2 ? -1 : 1; tl.fromTo("#rl-col" + c, {{ y: d * -120 }}, {{ y: d * 120, duration: {gdur}, ease: "none" }}, CTA); }}
    tl.fromTo("#rl-dim", {{ opacity: 0 }}, {{ opacity: 1, duration: 0.3 }}, CTA);
    shrink(CTA - 0.05, {CTA_POS[0]}, {CTA_POS[1]});
    tl.fromTo("#rl-cmt", {{ opacity: 0, scale: 1.3, filter: "blur(14px)" }}, {{ opacity: 1, scale: 1, filter: "blur(0px)", duration: 0.25, ease: "power3.out" }}, CTA + 0.05);
    tl.fromTo("#rl-sub", {{ opacity: 0, y: 20 }}, {{ opacity: 1, y: 0, duration: 0.2, ease: "power3.out" }}, {CTA + 0.8:.2f});
    window.__timelines["reel"] = tl;
  </script>
</template>
"""
open("compositions/reel.html", "w").write(html)
print("ok", TOTAL)
