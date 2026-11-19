# *From Grassmann to Clifford* (Bill Page, 2026): slides with narration

A talk for the Seminar on Fundamental Problems in Physics. It introduces this
repository and uses its supplement
[`grassmann_to_clifford.md`](../../supplement/grassmann_to_clifford.md) as the
example: Oziewicz's 1986 paper, his 1997 sequel, Jadczyk (2021) and Sobczyk's
null-vector papers, and an invitation to review the repository. 23 slides; the
notes are about 7,650 words, some 51 minutes when read by a synthetic voice.

**[View the slides](https://billpage.github.io/oziewicz/talks/grassmann_to_clifford/grassmann_to_clifford.html)**
(arrow keys or click to move; the notes are in a panel on the right, which N hides and shows). The page is one file, about
1.3 MB; the formulas are SVG inside it, so it needs no network apart from the
web fonts, which fall back to system fonts.

**[Play the narrated talk](https://billpage.github.io/oziewicz/narrated/grassmann_to_clifford_narrated.html)**
(Microsoft Edge voice `en-CA-LiamNeural`, about 52 minutes): the slides with
an audio player per slide and the transcript beside them. One file, about
16 MB, which also plays offline when saved.

Unlike [`npa2009/`](../npa2009/README.md), everything here is this repository's
own and under CC-BY-SA-4.0 (code: AGPL-3.0-or-later). Short formulas from the
papers discussed are restated, with their equation numbers, as in the
supplement.

*Status.* Drafted with Claude (Anthropic) on 17 November 2026 from the
supplement at commit `f1b7e34`, at which its 90 checks pass. Every formula on
the slides is taken from the supplement; a formula marked *checked* is checked
there. The one number added for the talk, the eigenvalue multiplicities of
slide 17 (`binom(n,k) 2^n`), was computed numerically for `n <= 5` (eigenvalues
of integer matrices) and is labelled so. Not yet read or heard by Bill Page.

## Files

| File | What it is |
|---|---|
| `slides.html` | The source: the slides, with formulas as TeX between `\(` `\)` and `\[` `\]`, images as `asset:NAME` and an empty `NOTES` array. Not a page to open |
| `notes/slide_NN.md` | The narration, one file per slide, in the speaker's voice |
| `grassmann_to_clifford.html` | The built page: formulas typeset as SVG, the figure embedded, `NOTES` filled. Input to `narrate render`, and served by GitHub Pages |
| `pronunciations.json` | For the synthetic voice: spoken forms used only in this talk. Names shared by the talks are in [`src/narration/oziewicz_terms.json`](../../src/narration/oziewicz_terms.json) |
| [`src/narration/build_deck.py`](../../src/narration/build_deck.py), [`tex_svg.mjs`](../../src/narration/tex_svg.mjs) | Build the page from the source (MathJax, from the `npm install` the markdown checks already need) |

The only image, `grassmann_dual_pair.png`, is the figure of the supplement, from
`figures/` on the `output` branch.

## Building

From the repository root, after `npm install katex mathjax-full` and with the
`output` worktree at `~/oziewicz-output`:

```bash
OZ_OUTPUT=talks/grassmann_to_clifford PYTHONPATH=src python3 src/narration/build_deck.py \
    --talk talks/grassmann_to_clifford --name grassmann_to_clifford \
    --assets ~/oziewicz-output/figures --foot "Oziewicz project · From Grassmann to Clifford"
```

Edit the slides in `slides.html` and the words in `notes/`, then build again.
The script prints the number of words and an estimate of the length.

## Narrating

The narrator is `narrate` from
[billpage/narrate](https://github.com/billpage/narrate)
(`pip install "narrate[pptx] @ git+https://github.com/billpage/narrate@v0.3.0"`), with this repository's settings in
[`narration.toml`](../../narration.toml): the Edge voice `en-CA-LiamNeural`,
renders in `~/oziewicz-narration/`, and pronunciations merged from narrate's
common terms, [`src/narration/oziewicz_terms.json`](../../src/narration/oziewicz_terms.json)
and this talk's `pronunciations.json`. Check the spoken text first (seconds, no
audio), then render (needs internet):

```bash
narrate render talks/grassmann_to_clifford/grassmann_to_clifford.html --preview
narrate render talks/grassmann_to_clifford/grassmann_to_clifford.html
```

or record the notes in your own voice as `audio/slide_NN.mp3` in the output
folder and build with `--reuse-audio`. Once Bill Page has listened to it, the
page is published with

```bash
narrate publish ~/oziewicz-narration/grassmann_to_clifford/grassmann_to_clifford_narrated.html
```

which commits it to `narrated/` on the `output` branch and writes its SHA-256
into [`../narrated.sha256`](../narrated.sha256) for a pull request to `main`;
the page is served once that is merged. The page listed now is the
render Bill Page made and pushed to `output` on 19 November 2026 (`2ba5383`),
from `main` after the correction of the book title on slide 23 (`e06d8b9`).

## Sources

The papers are those of the supplement, §17, and of
[`references/bibliography.md`](../../references/bibliography.md). The
navigation script and page frame follow the slide decks of billpage/wpmw
(`docs/interactive/worlds_and_particles.html`).
