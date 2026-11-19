// tex_svg.mjs - typeset TeX as self-contained SVG with MathJax (mathjax-full).
//
// Reads a JSON array of {"tex": "...", "display": true|false} on stdin and
// writes a JSON array of SVG strings, in the same order, on stdout. Each SVG
// carries its own glyph paths (fontCache "local"), so it can be pasted into a
// page with no script, font or stylesheet: this is how build_deck.py puts the
// formulas into a slides page that voiceover (billpage/narrate) can narrate and that works
// offline. Colours: \color[RGB]{47,93,138}{...} and the macros in MACROS below.
//
// Needs mathjax-full, installed by `npm install katex mathjax-full` at the
// repository root (the same install the markdown checks use).
//
// SPDX-License-Identifier: AGPL-3.0-or-later

import { mathjax } from 'mathjax-full/js/mathjax.js';
import { TeX } from 'mathjax-full/js/input/tex.js';
import { SVG } from 'mathjax-full/js/output/svg.js';
import { liteAdaptor } from 'mathjax-full/js/adaptors/liteAdaptor.js';
import { RegisterHTMLHandler } from 'mathjax-full/js/handlers/html.js';
import { AllPackages } from 'mathjax-full/js/input/tex/AllPackages.js';

// Vectors blue, covectors orange, as in the figures of the supplement.
const MACROS = {
  V: ['{\\color[RGB]{47,93,138}{#1}}', 1],
  C: ['{\\color[RGB]{181,84,28}{#1}}', 1],
  G: ['{\\color[RGB]{46,125,79}{#1}}', 1],
  cV: '\\mathcal V',
  End: '\\mathrm{End}\\,',
};

const adaptor = liteAdaptor();
RegisterHTMLHandler(adaptor);
const doc = mathjax.document('', {
  InputJax: new TeX({ packages: AllPackages.filter((p) => p !== 'colorv2'), macros: MACROS }),
  OutputJax: new SVG({ fontCache: 'local' }),
});

let raw = '';
process.stdin.setEncoding('utf8');
process.stdin.on('data', (c) => { raw += c; });
process.stdin.on('end', () => {
  const items = JSON.parse(raw);
  const out = items.map(({ tex, display }, k) => {
    const node = doc.convert(tex, { display: !!display });
    const svg = adaptor.firstChild(node);
    const err = adaptor.innerHTML(node).match(/data-mjx-error="([^"]*)"/);
    if (err) {
      throw new Error(`TeX error "${err[1]}" in: ${tex}`);
    }
    // Text colour comes from the slide; the SVG uses currentColor. Glyph ids
    // are made unique per formula, so that no <use> refers to a glyph defined
    // in another formula (perhaps on a hidden slide).
    return adaptor.outerHTML(svg)
      .replace(/id="MJX-/g, `id="F${k}-MJX-`)
      .replace(/href="#MJX-/g, `href="#F${k}-MJX-`);
  });
  process.stdout.write(JSON.stringify(out));
});
