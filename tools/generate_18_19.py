import pathlib, json, colorsys, random
# Regenerates styles 18 (edit WORD / FS / PAL) and 19 (edit TAGS / STY / seed). Run from anywhere:
#   python3 tools/generate_18_19.py && python3 tools/build_index.py styles/18-3d-pop-letters/template && python3 tools/build_index.py styles/19-tag-pile-drop/template
ROOT = pathlib.Path(__file__).resolve().parent.parent / "styles"
def hexrgb(h): h = h.lstrip("#"); return tuple(int(h[i:i+2], 16) / 255 for i in (0, 2, 4))
def darker(h, k):
    r, g, b = hexrgb(h); hh, l, s = colorsys.rgb_to_hls(r, g, b); l = max(0, l * k)
    r, g, b = colorsys.hls_to_rgb(hh, l, s); return "#%02x%02x%02x" % (int(r * 255), int(g * 255), int(b * 255))

# ======================= 34 3D POP LETTERS =======================
T = ROOT / "18-3d-pop-letters/template"; (T / "compositions").mkdir(parents=True, exist_ok=True); (T / "assets").mkdir(exist_ok=True)
WORD = "LOREM"; FS = 225; DEP = 14
GLYPH = {"L": .64, "O": .84, "R": .76, "E": .66, "M": .98, "I": .36, "P": .74, "S": .72, "U": .78, "D": .80, "T": .68, "A": .80, "N": .80}
PAL = ["#c8ff3c", "#ff5fc8", "#6a86ff", "#ff7a59", "#9fe0ff", "#ffe24a"]
widths = [round(FS * GLYPH.get(c, .74)) for c in WORD]; GAP = 8
total = sum(widths) + GAP * (len(WORD) - 1); x = -total / 2
letters = []
for i, (c, w) in enumerate(zip(WORD, widths)):
    col = PAL[i % len(PAL)]
    lays = "".join(f'<span class="lay" data-layout-ignore style="color:{darker(col, 0.62 - k * 0.025)}">{c}</span>' for k in range(DEP))
    letters.append(f'''      <div id="pl1-L{i}" class="L" style="left:{x:.0f}px;width:{w}px" data-layout-allow-overlap>{lays}<span class="face" style="color:{col}">{c}</span></div>
      <div id="pl1-sh{i}" class="sh" style="left:{x + w/2 - w*0.6:.0f}px;width:{w*1.2:.0f}px"></div>
      <div id="pl1-rg{i}" class="rg" style="left:{x + w/2 - 120:.0f}px"></div>''')
    x += w + GAP
html34 = """<template>
  <style>
    #pl1 { position: absolute; inset: 0; overflow: hidden; perspective: 1100px; perspective-origin: 540px 640px;
      background: radial-gradient(ellipse 90% 55% at 50% 58%, var(--stageLight, #2c2a8a) 0%, var(--stageDeep, #0a0820) 100%); }
    /* the stage: a floor at y = 0; the camera looks down at it a little */
    #pl1-stage { position: absolute; left: 540px; top: 1120px; width: 0; height: 0; transform-style: preserve-3d; }
    #pl1 .L { position: absolute; bottom: 0; height: """ + str(FS) + """px; transform-style: preserve-3d; transform-origin: 50% 100%; }
    #pl1 .L span { position: absolute; left: 0; bottom: 0; width: 100%; text-align: center; font: 400 """ + str(FS) + """px/""" + str(FS) + """px "Archivo Black", sans-serif; }
    /* contact shadow and a pop shockwave ring, both lying on the floor */
    #pl1 .sh { position: absolute; top: -30px; height: 60px; border-radius: 50%; background: radial-gradient(ellipse at center, rgba(0,0,0,.55), transparent 70%); transform: rotateX(90deg); }
    #pl1 .rg { position: absolute; top: -120px; width: 240px; height: 240px; border-radius: 50%; border: 6px solid rgba(255,255,255,.7); transform: rotateX(90deg) scale(0); opacity: 0; }
    #pl1-word { display: none; }
  </style>
  <div id="pl1" data-composition-id="pl1" data-width="1080" data-height="1920">
    <!-- Letters are generated (generator.py) so each slab hugs its glyph and gets its own colour + darker sides -->
    <div id="pl1-stage" data-layout-allow-overlap data-layout-allow-overflow>
""" + "\n".join(letters) + """
    </div>
  </div>
  <script>
    const tl = gsap.timeline({ paused: true });
    // Each letter is a face + """ + str(DEP) + """ stacked layers behind it. Per letter we animate:
    //   rx = how far it lies back on the floor (90° flat, face up → 0° standing), y = jump height,
    //   d = extrusion depth (0 = flat print, 1 = full block), ry = turn on its own axis.
    const N = """ + str(len(WORD)) + """, DEP = """ + str(DEP) + """, STEP = 5;
    const L = [...Array(N).keys()].map(i => document.getElementById("pl1-L" + i));
    const LAY = L.map(el => [...el.querySelectorAll(".lay")]);
    const SH = L.map((e, i) => document.getElementById("pl1-sh" + i));
    const P = L.map(() => ({ rx: 90, y: 0, d: 0, ry: 0 }));
    function render() {
      for (let i = 0; i < N; i++) {
        const p = P[i];
        L[i].style.transform = `translateY(${-p.y}px) rotateY(${p.ry}deg) rotateX(${p.rx}deg)`;
        LAY[i].forEach((e, k) => { e.style.transform = `translateZ(${-(k + 1) * STEP * p.d}px)`; });
        const stand = 1 - p.rx / 90;                     // shadow darkens as the letter stands, softens when it jumps
        SH[i].style.opacity = (0.25 + 0.75 * stand) * Math.max(0.3, 1 - p.y / 300);
      }
    }
    tl.set("#pl1-stage", { rotationX: -16 }, 0);
    tl.fromTo("#pl1-stage", { scale: 0.9 }, { scale: 1, duration: 1.0, ease: "power2.out" }, 0);
    // POP: left to right, each flat letter springs up, inflating into a block, with a little jump and a shockwave
    P.forEach((p, i) => {
      const t = 0.45 + i * 0.13;
      tl.to(p, { rx: 0, duration: 0.6, ease: "back.out(2.6)", onUpdate: render }, t);
      tl.to(p, { d: 1, duration: 0.5, ease: "power3.out", onUpdate: render }, t);
      tl.to(p, { keyframes: [{ y: 170, duration: 0.22, ease: "power2.out" }, { y: 0, duration: 0.3, ease: "bounce.out" }], onUpdate: render }, t);
      tl.fromTo(`#pl1-rg${i}`, { scale: 0.2, opacity: 0.9 }, { scale: 2.2, opacity: 0, duration: 0.6, ease: "power2.out" }, t + 0.05);
      // SWAY while held, alternating directions
      tl.to(p, { ry: i % 2 ? 9 : -9, duration: 0.7, ease: "sine.inOut", onUpdate: render, yoyo: true, repeat: 1 }, 1.4 + i * 0.05);
      // SPIN WAVE: one full turn each, rippling across the word
      tl.to(p, { ry: "+=360", duration: 0.65, ease: "power2.inOut", onUpdate: render }, 2.95 + i * 0.09);
      // SINK: right to left they lie back down and deflate into flat print again
      const s = 3.95 + (N - 1 - i) * 0.1;
      tl.to(p, { rx: 90, d: 0, duration: 0.45, ease: "power3.in", onUpdate: render }, s);
    });
    tl.to("#pl1-stage", { rotationY: 14, duration: 2.6, ease: "sine.inOut" }, 1.2);       // camera eases around the word
    tl.to("#pl1-stage", { rotationY: 0, duration: 0.6, ease: "power2.inOut" }, 3.9);
    tl.to("#pl1-stage", { opacity: 0, duration: 0.3 }, 4.75);
    render();
    window.__timelines["pl1"] = tl;
  </script>
</template>
"""
(T / "compositions/pl1.html").write_text(html34)
(T / "scenes.json").write_text(json.dumps({"id": "3d-pop-letters", "title": "18 3D Pop Letters", "background": "#0a0820",
  "variables": [{"id": "stageLight", "type": "color", "label": "Stage centre", "default": "#2c2a8a"},
                {"id": "stageDeep", "type": "color", "label": "Stage edge", "default": "#0a0820"}],
  "scenes": [{"id": "pl1", "duration": 5.1}]}, indent=2) + "\n")

# ======================= 35 TAG PILE DROP =======================
T = ROOT / "19-tag-pile-drop/template"; (T / "compositions").mkdir(parents=True, exist_ok=True); (T / "assets").mkdir(exist_ok=True)
TAGS = ["lorem ipsum", "dolor sit amet", "✦", "consectetur", "sed do", "tempor", "magna aliqua", "ut enim", "✦", "quis nostrud",
        "ullamco", "laboris nisi", "aliquip", "ex ea commodo", "duis aute", "irure dolor"]
STY = [("#15122a", "#ffffff"), ("#2f55ff", "#ffffff"), ("#ffffff", "#15122a"), ("#c8ff3c", "#15122a"), ("#ff5fc8", "#15122a")]
rnd = random.Random(7)
pills = []
for i, t in enumerate(TAGS):
    bg, fg = STY[i % len(STY)]
    if t == "✦": bg, fg = ("#c8ff3c", "#15122a") if i < 8 else ("#ff5fc8", "#15122a")
    # settle zone: a loose heap in the middle of the frame, later tags landing toward the centre (on top)
    # rejection-sample a spot that keeps some distance from earlier tags, so most text stays readable in the heap
    k = i / (len(TAGS) - 1)
    for _ in range(400):
        cx = 540 + rnd.uniform(-300, 300) * (1 - 0.25 * k); cy = 1000 + rnd.uniform(-560, 560) * (1 - 0.2 * k)
        if all((cx - p[3]) ** 2 + ((cy - p[4]) * 1.6) ** 2 > 230 ** 2 for p in pills): break
    rot = rnd.choice([rnd.uniform(-24, 24), rnd.uniform(-24, 24), rnd.uniform(55, 80) * rnd.choice([-1, 1])])
    pills.append((t, bg, fg, cx, cy, rot))
items = []
for i, (t, bg, fg, cx, cy, rot) in enumerate(pills):
    cls = "badge" if t == "✦" else "pill"
    items.append(f'''      <div id="tp1-w{i}" class="wrap" data-layout-allow-occlusion data-layout-allow-overlap style="left:{cx:.0f}px;top:{cy:.0f}px;z-index:{i + 1}" data-r="{rot:.1f}">
        <div class="shadow {cls}-s"></div>
        <div id="tp1-p{i}" class="{cls}" data-layout-allow-occlusion style="background:{bg};color:{fg}">{t}</div>
      </div>''')
html35 = """<template>
  <style>
    #tp1 { position: absolute; inset: 0; overflow: hidden;
      background: radial-gradient(ellipse 85% 60% at 50% 50%, #ffffff 0%, var(--table, #ecebf2) 65%, #d9d7e3 100%); }
    /* top-down view onto a table. Each tag: a wrapper at its resting spot, a soft shadow, the tag itself */
    #tp1 .wrap { position: absolute; width: 0; height: 0; }
    #tp1 .pill, #tp1 .badge { position: absolute; left: 0; top: 0; transform: translate(-50%, -50%); white-space: nowrap;
      font: 800 52px/116px Inter, sans-serif; letter-spacing: -0.02em; height: 116px; padding: 0 50px; border-radius: 58px; }
    #tp1 .badge { width: 170px; height: 170px; padding: 0; border-radius: 50%; font-size: 82px; line-height: 170px; text-align: center; }
    #tp1 .shadow { position: absolute; left: 0; top: 0; border-radius: 60px; background: rgba(30,20,60,.22); filter: blur(12px); }
    #tp1 .pill-s { width: 360px; height: 96px; margin: -48px 0 0 -180px; }
    #tp1 .badge-s { width: 140px; height: 140px; margin: -70px 0 0 -70px; border-radius: 50%; }
  </style>
  <div id="tp1" data-composition-id="tp1" data-width="1080" data-height="1920">
    <!-- Tags drop in order (later ones land on top). Edit the text; positions/rotations are in each wrapper (left/top/data-r).
         Regenerate a new heap with generator.py. -->
    <div id="tp1-table" data-layout-allow-overlap data-layout-allow-overflow>
""" + "\n".join(items) + """
    </div>
  </div>
  <script>
    const tl = gsap.timeline({ paused: true });
    const W = gsap.utils.toArray("#tp1 .wrap");
    // fit each shadow to its tag once fonts are in (pills are as wide as their text)
    window.__hf = window.__hf || {}; window.__hf.buildReady = window.__hf.buildReady || {};
    window.__hf.buildReady["tp1"] = document.fonts.load("800 52px Inter").then(() => {
      W.forEach(w => { const p = w.querySelector(".pill"), s = w.querySelector(".pill-s"); if (p && s) { s.style.width = (p.offsetWidth - 20) + "px"; s.style.marginLeft = -(p.offsetWidth - 20) / 2 + "px"; } });
    });
    function rng(s) { return () => { s = (s * 16807) % 2147483647; return s / 2147483647; }; }
    const r = rng(11);
    // DROP: each tag falls from above the camera onto the table: it starts huge, blurred, with a far, faint shadow,
    // and lands at rest size with a squash, its shadow tightening under it. The heap jolts on every landing.
    W.forEach((w, i) => {
      const tag = w.querySelector(".pill, .badge"), sh = w.querySelector(".shadow"), rot = +w.dataset.r, t = 0.15 + i * 0.17;
      const spin = (r() - 0.5) * 90, dx = (r() - 0.5) * 160, dy = (r() - 0.5) * 160;
      tl.set(w, { opacity: 0 }, 0); tl.set(w, { opacity: 1 }, t);
      tl.fromTo(tag, { scale: 2.8, rotation: rot + spin, x: dx, y: dy, filter: "blur(16px)" },
                     { scale: 1, rotation: rot, x: 0, y: 0, filter: "blur(0px)", duration: 0.34, ease: "power2.in" }, t);
      tl.to(tag, { keyframes: [{ scale: 0.93, duration: 0.06 }, { scale: 1.02, duration: 0.08 }, { scale: 1, duration: 0.1 }] }, t + 0.34);
      tl.fromTo(sh, { x: 70, y: 110, scale: 1.8, opacity: 0, rotation: rot }, { x: 5, y: 10, scale: 1, opacity: 1, rotation: rot, duration: 0.34, ease: "power2.in" }, t);
      if (i) tl.to("#tp1-table", { keyframes: [{ scale: 0.994, duration: 0.05 }, { scale: 1, duration: 0.12 }] }, t + 0.34);
    });
    // UN-STACK: the camera lifts and the tags fly back up past the lens, top of the heap first
    const end = 0.15 + W.length * 0.17 + 0.9;
    W.slice().reverse().forEach((w, k) => {
      const tag = w.querySelector(".pill, .badge"), sh = w.querySelector(".shadow"), t = end + k * 0.05;
      tl.to(tag, { scale: 3, rotation: "+=" + ((k % 2 ? 1 : -1) * 40), filter: "blur(18px)", opacity: 0, duration: 0.4, ease: "power2.in" }, t);
      tl.to(sh, { opacity: 0, scale: 1.8, duration: 0.3 }, t);
    });
    window.__timelines["tp1"] = tl;
  </script>
</template>
"""
(T / "compositions/tp1.html").write_text(html35)
dur35 = round(0.15 + len(TAGS) * 0.17 + 0.9 + len(TAGS) * 0.05 + 0.5, 2)
(T / "scenes.json").write_text(json.dumps({"id": "tag-pile-drop", "title": "19 Tag Pile Drop", "background": "#ecebf2",
  "variables": [{"id": "table", "type": "color", "label": "Table colour", "default": "#ecebf2"}],
  "scenes": [{"id": "tp1", "duration": dur35}]}, indent=2) + "\n")
print("ok", dur35)
