"""Build a self-contained slides page from a source deck with TeX formulas.

The source is an HTML page of the kind voiceover.py (billpage/wpmw,
src/narration/voiceover.py) narrates: a `<div id="stage">` with one
`<section class="slide">` per slide, a `<div id="notes">`, and a script that
contains `const NOTES = [];`. In the source:

  \\( ... \\)        inline TeX, typeset as an inline SVG
  \\[ ... \\]        display TeX, typeset as a centred SVG block
  src="asset:F"    an image, embedded as a data URI from --assets/F
  data-nofoot      on a section: no footer line

Every other section gets a footer `<p class="foot">FOOT · k / N</p>`.
The notes come from <talk>/notes/slide_NN.md (one per slide; NN from 01) and
fill the NOTES array. Formulas are typeset by tex_svg.mjs (MathJax, needs
`npm install katex mathjax-full` at the repository root), so the page needs
no script, font or stylesheet from elsewhere for its mathematics.

Run (writes <name>.html through ozlib.utils.output_path, i.e. into $OZ_OUTPUT):
  OZ_OUTPUT=talks/grassmann_to_clifford PYTHONPATH=src python3 src/narration/build_deck.py \\
      --talk talks/grassmann_to_clifford --name grassmann_to_clifford \\
      --assets ~/oziewicz-output/figures --foot "Oziewicz project · From Grassmann to Clifford"
"""

# SPDX-License-Identifier: AGPL-3.0-or-later

from __future__ import annotations

import argparse
import base64
import json
import mimetypes
import re
import subprocess
from pathlib import Path

from ozlib.utils import output_path

MATH = re.compile(r"\\\((.+?)\\\)|\\\[(.+?)\\\]", re.S)


def typeset(stage: str) -> str:
    """Replace every \\( \\) and \\[ \\] in the stage by MathJax SVG."""
    found = list(MATH.finditer(stage))
    items = [{"tex": (m.group(1) or m.group(2)).strip(), "display": m.group(2) is not None}
             for m in found]
    if not items:
        return stage
    mjs = Path(__file__).with_name("tex_svg.mjs")
    res = subprocess.run(["node", str(mjs)], input=json.dumps(items), capture_output=True,
                         text=True, check=False, timeout=300,
                         cwd=Path(__file__).resolve().parents[2])
    if res.returncode != 0:
        raise SystemExit(res.stderr)
    svgs = json.loads(res.stdout)
    out, last = [], 0
    for m, it, svg in zip(found, items, svgs):
        out.append(stage[last:m.start()])
        out.append(f'<div class="mathd">{svg}</div>' if it["display"]
                   else f'<span class="math">{svg}</span>')
        last = m.end()
    out.append(stage[last:])
    return "".join(out)


def embed_assets(stage: str, assets: Path | None) -> str:
    def repl(m: re.Match) -> str:
        if assets is None:
            raise SystemExit(f"asset {m.group(1)} used but --assets not given")
        f = assets / m.group(1)
        mime = mimetypes.guess_type(f.name)[0] or "application/octet-stream"
        return f'src="data:{mime};base64,{base64.b64encode(f.read_bytes()).decode()}"'
    return re.sub(r'src="asset:([^"]+)"', repl, stage)


def add_footers(stage: str, foot: str) -> str:
    n = stage.count('<section class="slide"')
    k = 0

    def repl(m: re.Match) -> str:
        nonlocal k
        k += 1
        if "data-nofoot" in m.group(1):
            return m.group(0)
        return f'{m.group(1)}{m.group(2)}<p class="foot">{foot} · {k} / {n}</p>\n</section>'
    return re.sub(r'(<section class="slide"[^>]*>)(.*?)</section>', repl, stage, flags=re.S)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--talk", required=True, help="talk directory (slides.html and notes/)")
    ap.add_argument("--name", required=True, help="base name of the page written")
    ap.add_argument("--assets", type=Path, help="directory of the images named asset:...")
    ap.add_argument("--foot", default="", help="footer text before the slide number")
    args = ap.parse_args()

    talk = Path(args.talk)
    src = (talk / "slides.html").read_text(encoding="utf-8")
    a = src.index('<div id="stage">')
    b = src.index('<div id="notes"', a)
    stage = add_footers(src[a:b], args.foot)
    stage = embed_assets(typeset(stage), args.assets.expanduser() if args.assets else None)

    n = stage.count('<section class="slide"')
    notes = []
    for k in range(1, n + 1):
        f = talk / "notes" / f"slide_{k:02d}.md"
        notes.append(f.read_text(encoding="utf-8").strip() if f.exists() else "")
    if "const NOTES = [];" not in src:
        raise SystemExit("slides.html must contain `const NOTES = [];`")
    rest = src[b:].replace("const NOTES = [];",
                           "const NOTES = " + json.dumps(notes, ensure_ascii=False)
                           .replace("</", "<\\/") + ";", 1)
    page = src[:a] + stage + rest
    out = output_path(f"{args.name}.html")
    Path(out).write_text(page, encoding="utf-8")
    words = sum(len(t.split()) for t in notes)
    print(f"{out}: {n} slides, {sum(bool(t) for t in notes)} with notes, "
          f"{words} words (about {words / 140:.0f} min at 140 words a minute), "
          f"{len(page) / 1e6:.1f} MB")


if __name__ == "__main__":
    main()
