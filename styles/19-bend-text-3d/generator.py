import pathlib, json
# Regenerates template/compositions/bt1.html and scenes.json. Edit LINES (and N for smoother bends), then run:
#   python3 generator.py && python3 ../../tools/build_index.py template
LINES = ("LOREM", "IPSUM", "dolor sit amet")
R = pathlib.Path(__file__).resolve().parent / "template"
(R / "compositions").mkdir(parents=True, exist_ok=True); (R / "assets").mkdir(exist_ok=True)
N, W, H = 60, 1000, 560
SW = W / N
slices = "\n".join(
    f'      <div id="bt1-s{i}" class="sl" data-layout-allow-overflow data-layout-allow-overlap style="left:{-SW/2:.2f}px"><div class="sheet" data-layout-ignore style="left:{-i*SW:.2f}px">'
    f'<div class="l1">{LINES[0]}</div><div class="l2">{LINES[1]}</div><div class="l3">{LINES[2]}</div></div></div>'
    for i in range(N))
html = """<template>
  <style>
    @font-face { font-family: "Instrument Serif"; font-style: italic; src: url("assets/fonts/instrument-serif-italic.woff2") format("woff2"); }
    #bt1 { position: absolute; inset: 0; overflow: hidden; perspective: 1500px;
      background: radial-gradient(ellipse 80% 60% at 50% 46%, var(--stageLight, #3a2cf0) 0%, var(--stageDeep, #0b0828) 100%); }
    /* the text block is cut into thin vertical strips; each strip is placed on a curve in 3D, so the whole block bends */
    #bt1-rig { position: absolute; left: 540px; top: """ + str(960 - H // 2) + """px; width: 0; height: """ + str(H) + """px; transform-style: preserve-3d; }
    #bt1 .sl { position: absolute; top: 0; width: """ + f"{SW + 1.2:.2f}" + """px; height: """ + str(H) + """px; overflow: hidden; }
    #bt1 .sheet { position: absolute; top: 0; width: """ + str(W) + """px; height: """ + str(H) + """px; text-align: center; }
    #bt1 .l1 { font: 900 250px/240px Inter, sans-serif; letter-spacing: -0.06em; color: var(--c1, #c8ff3c); }
    #bt1 .l2 { font: 900 250px/220px Inter, sans-serif; letter-spacing: -0.06em; color: var(--c2, #ffffff); }
    #bt1 .l3 { font: italic 400 96px/96px "Instrument Serif", serif; color: var(--c3, #ff5fc8); }
    #bt1-shadow { position: absolute; left: 190px; top: 1330px; width: 700px; height: 80px; border-radius: 50%; background: radial-gradient(ellipse at center, rgba(0,0,0,.5), transparent 70%); }
    #bt1-copy { display: none; }
  </style>
  <div id="bt1" data-composition-id="bt1" data-width="1080" data-height="1920">
    <div id="bt1-shadow"></div>
    <!-- Every strip shows the same block (three lines). To change the words, edit .l1/.l2/.l3 in ALL strips
         (or regenerate with the generator in STYLE.md). -->
    <div id="bt1-rig">
""" + slices + """
    </div>
  </div>
  <script>
    const tl = gsap.timeline({ paused: true });
    // ---- bend model ----
    // Strip i sits at arc position s (px from the block's centre). With curvature k (1/radius), it lands at
    // angle θ = s·k on a circle: x = sin θ / k, z = (cos θ − 1)/k. k > 0 bows toward camera (centre nearest), k < 0 curves
    // away (concave), k = 2π / width rolls the block into a complete tube. Strips facing away show dimmed (the back of the sheet).
    const N = """ + str(N) + """, W = """ + str(W) + """, SW = W / N;
    const S = [...Array(N).keys()].map(i => document.getElementById("bt1-s" + i));
    const st = { k: 0, spin: 0, tilt: 0, show: 0 };
    function render() {
      for (let i = 0; i < N; i++) {
        const s = (i + 0.5) * SW - W / 2, th = s * st.k;
        const x = Math.abs(st.k) < 1e-6 ? s : Math.sin(th) / st.k, z = Math.abs(st.k) < 1e-6 ? 0 : (Math.cos(th) - 1) / st.k;
        // the strip turns with the surface: its normal points outward from the curve (CSS rotateY + turns +x away from camera)
        const a = th * 180 / Math.PI;
        S[i].style.transform = `translate3d(${x.toFixed(2)}px, 0, ${z.toFixed(2)}px) rotateY(${a.toFixed(3)}deg)`;
        // light from the front-left: strips turned toward it are brighter
        // light from the front-left; a strip whose back faces the camera shows the sheet's dim mirrored reverse (see-through tube)
        const face = (a + st.spin) * Math.PI / 180, c = Math.cos(face), lit = c >= 0 ? 0.62 + 0.38 * Math.cos(face + 0.35) : 0.32;
        const vis = Math.max(0, Math.min(1, st.show * N * 0.5 - Math.abs(i - N / 2) + 1));  // reveal from the centre outward
        S[i].style.filter = `brightness(${lit.toFixed(3)})`;
        S[i].style.opacity = Math.min(1, vis) * (c >= 0 ? 1 : 0.55);
      }
      document.getElementById("bt1-rig").style.transform = `rotateX(${st.tilt}deg) rotateY(${st.spin}deg)`;
    }
    const CONVEX = 1 / 520, CONCAVE = -1 / 520, TUBE = 2 * Math.PI / W * 0.985;
    const R = (vars, d, e, t) => tl.to(st, { ...vars, duration: d, ease: e, onUpdate: render }, t);
    tl.fromTo(st, { k: 0, spin: 0, tilt: 0, show: 0 }, { show: 1, duration: 0.45, ease: "power2.out", onUpdate: render }, 0);
    tl.fromTo("#bt1-rig", { scale: 0.85 }, { scale: 1, duration: 0.5, ease: "back.out(2)" }, 0);
    R({ k: CONVEX, tilt: 12 }, 0.75, "power2.inOut", 0.5);              // bows toward the camera
    R({ k: CONCAVE, spin: -24, tilt: -8 }, 0.8, "power2.inOut", 1.3);   // flexes the other way, like a curved screen
    R({ k: TUBE, spin: -384, tilt: 10 }, 1.05, "power2.inOut", 2.15);   // rolls up into a tube and spins once
    R({ k: 0, spin: -360, tilt: 0 }, 0.75, "back.out(1.6)", 3.2);       // springs back flat
    R({ k: TUBE, spin: -540, tilt: 25 }, 0.6, "power3.in", 4.4);        // rolls up again and leaves
    tl.to("#bt1-rig", { scale: 0.2, opacity: 0, duration: 0.45, ease: "power3.in" }, 4.55);
    tl.fromTo("#bt1-shadow", { opacity: 0 }, { opacity: 1, duration: 0.5 }, 0.1);
    tl.to("#bt1-shadow", { opacity: 0, duration: 0.3 }, 4.6);
    render();
    window.__timelines["bt1"] = tl;
  </script>
</template>
"""
(R / "compositions/bt1.html").write_text(html)
(R / "scenes.json").write_text(json.dumps({
  "id": "bend-text-3d", "title": "19 Bend Text 3D", "background": "#0b0828",
  "variables": [
    {"id": "c1", "type": "color", "label": "Line 1 (lime)", "default": "#c8ff3c"},
    {"id": "c2", "type": "color", "label": "Line 2 (white)", "default": "#ffffff"},
    {"id": "c3", "type": "color", "label": "Line 3 serif (pink)", "default": "#ff5fc8"},
    {"id": "stageLight", "type": "color", "label": "Stage centre", "default": "#3a2cf0"},
    {"id": "stageDeep", "type": "color", "label": "Stage edge", "default": "#0b0828"}],
  "scenes": [{"id": "bt1", "duration": 5.0}]}, indent=2) + "\n")
print("wrote", R / "compositions/bt1.html")
