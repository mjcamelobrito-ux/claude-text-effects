#!/usr/bin/env python3
"""Rebuild a style template's index.html from its scenes.json.

Usage:  python3 tools/build_index.py styles/<style>/template

scenes.json shape:
{
  "id": "kinetic-collage",            # root composition id
  "title": "Kinetic Type Collage",
  "background": "#111",
  "footage": {"src": "assets/speaker-warm.mp4", "id": "footage", "hasAudio": false}   # optional talking-head layer; hasAudio keeps its sound
  "variables": [ {id,type,label,default}, ... ],                 # editable copy / colours / media
  "scenes": [ {"id": "s1", "start": 0, "duration": 2.4}, ... ]    # mounted from compositions/<id>.html
}
Scenes play back to back in the order given unless "start" is set. The root duration is the
end of the last scene. Re-run after reordering or retiming scenes; hand edits to index.html
are overwritten.
"""
import json, sys, pathlib

def build(tdir: pathlib.Path):
    spec = json.loads((tdir / "scenes.json").read_text())
    t = 0.0
    hosts = []
    for i, s in enumerate(spec["scenes"]):
        start = s.get("start", t)
        dur = s["duration"]
        t = max(t, start + dur)
        hosts.append(
            f'      <div id="{s["id"]}" data-composition-id="{s["id"]}" data-composition-src="compositions/{s["id"]}.html"\n'
            f'        data-start="{start:g}" data-duration="{dur:g}" data-track-index="{i + 2}" data-track-kind="graphics"\n'
            f'        data-width="1080" data-height="1920" style="z-index:{10 + i}"></div>'
        )
    total = round(t, 3)
    footage = ""
    if spec.get("footage"):
        f = spec["footage"]
        footage = (
            f'      <video id="{f.get("id", "footage")}" class="clip" src="{f["src"]}" data-var-src="footageSrc" {'data-has-audio="true"' if f.get("hasAudio") else 'muted'} playsinline\n'
            f'        data-start="0" data-duration="{total:g}" data-track-index="1"\n'
            f'        style="position:absolute;left:0;top:0;width:1080px;height:1920px;object-fit:cover;z-index:1"></video>\n'
        )
    variables = spec.get("variables", [])
    if spec.get("footage") and not any(v["id"] == "footageSrc" for v in variables):
        variables = [{"id": "footageSrc", "type": "string", "label": "Talking-head footage (path in assets/)",
                      "default": spec["footage"]["src"]}] + variables
    vars_json = json.dumps(variables, ensure_ascii=False).replace("'", "&#39;")
    html = f"""<!doctype html>
<html lang="en" data-resolution="portrait" data-composition-variables='{vars_json}'>
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=1080, height=1920" />
    <title>{spec["title"]}</title>
    <script src="https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/gsap.min.js"></script>
    <style>
      * {{ margin: 0; padding: 0; box-sizing: border-box; }}
      html, body {{ width: 1080px; height: 1920px; overflow: hidden; background: {spec.get("background", "#000")}; }}
      #bg {{ position: absolute; inset: 0; background: {spec.get("background", "#000")}; z-index: 0; }}
    </style>
  </head>
  <body>
    <div id="main" data-composition-id="main" data-start="0" data-duration="{total:g}" data-width="1080" data-height="1920">
      <div id="bg"></div>
{footage}{chr(10).join(hosts)}
    </div>
    <script>
      window.__timelines = window.__timelines || {{}};
      window.__timelines["main"] = gsap.timeline({{ paused: true }});
    </script>
  </body>
</html>
"""
    (tdir / "index.html").write_text(html)
    print(f"{tdir}/index.html  {len(hosts)} scenes  {total:g}s")

if __name__ == "__main__":
    for a in sys.argv[1:]:
        build(pathlib.Path(a))
