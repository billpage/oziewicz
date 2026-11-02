"""Build the plain slides page of a narrated talk (the input to voiceover.py).

The page holds one <section class="slide"> per slide position, each showing a
page of the talk's PDF as a vector (SVG) image, and a `const NOTES = [...]`
array with the speaker notes. Its form is the one voiceover.py from
billpage/wpmw (src/narration/voiceover.py) reads.

A talk directory holds:
  slide_to_pdfpage.json   position -> PDF page (a list; positions may repeat pages)
  notes/slide_NN.md       the notes for position NN (absent: no notes, no audio)

The PDF itself is not in the repository (see the talk's NOTICE.md); pass its
path. Needs pdftocairo (poppler-utils).

Run (writes <name>.html through ozlib.utils.output_path, i.e. into $OZ_OUTPUT):
  OZ_OUTPUT=talks/npa2009 PYTHONPATH=src python3 src/narration/build_slides.py \
      --pdf /path/to/NPA2009-Beamer.pdf --talk talks/npa2009 --name npa2009 \
      --title "What is Special Relativity Theory?"
"""

from __future__ import annotations

import argparse
import base64
import json
import subprocess
import tempfile
from pathlib import Path

from ozlib.utils import output_path


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--pdf", required=True, help="the talk's slides as PDF")
    ap.add_argument("--talk", required=True, help="talk directory (order map and notes/)")
    ap.add_argument("--name", required=True, help="base name of the page written")
    ap.add_argument("--title", required=True, help="page title")
    ap.add_argument("--width", type=int, default=1920)
    ap.add_argument("--height", type=int, default=1484, help="default: US-letter landscape at width 1920")
    args = ap.parse_args()

    talk = Path(args.talk)
    order = json.loads((talk / "slide_to_pdfpage.json").read_text())
    with tempfile.TemporaryDirectory() as tmp:
        uri = {}
        for p in sorted(set(order)):
            svg = Path(tmp) / f"p{p}.svg"
            subprocess.run(["pdftocairo", "-svg", "-f", str(p), "-l", str(p), args.pdf, str(svg)],
                           check=True, timeout=120)
            uri[p] = "data:image/svg+xml;base64," + base64.b64encode(svg.read_bytes()).decode()
    notes = []
    for k in range(1, len(order) + 1):
        f = talk / "notes" / f"slide_{k:02d}.md"
        notes.append(f.read_text().strip() if f.exists() else "")

    W, H = args.width, args.height
    # Each page image is stored once, as a CSS background, and reused when a page is shown again.
    css = "\n".join(f".slide[data-page=\"{p}\"] {{ background-image: url('{uri[p]}'); }}" for p in sorted(uri))
    sections = "\n".join(f'<section class="slide" data-n="{k}" data-page="{p}" '
                         f'aria-label="Slide {k} (PDF page {p} of {max(order)})"></section>'
                         for k, p in enumerate(order, 1))
    page = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{args.title}</title>
<style>
html, body {{ margin: 0; height: 100%; background: #1d232c; overflow: hidden; }}
#stage {{ position: absolute; left: 0; top: 0; width: {W}px; height: {H}px; transform-origin: 0 0; }}
.slide {{ position: absolute; left: 0; top: 0; width: {W}px; height: {H}px; display: block;
         background: #fff no-repeat center / contain; }}
@media screen {{ .slide:not(.current) {{ display: none !important; }} }}
{css}
</style>
</head>
<body>
<div id="stage">
{sections}
</div>
<div id="notes"></div>
<script>
const NOTES = {json.dumps(notes, ensure_ascii=False).replace("</", "<\\/")};
</script>
</body>
</html>
"""
    out = output_path(f"{args.name}.html")
    Path(out).write_text(page)
    print(f"{out}: {len(order)} slides, {sum(bool(n) for n in notes)} with notes, {len(page) / 1e6:.1f} MB")


if __name__ == "__main__":
    main()
