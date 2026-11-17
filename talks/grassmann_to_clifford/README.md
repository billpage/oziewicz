# *From Grassmann to Clifford* (Bill Page, 2026): slides with narration

A talk for the Seminar on Fundamental Problems in Physics. It introduces this
repository and uses its supplement
[`grassmann_to_clifford.md`](../../supplement/grassmann_to_clifford.md) as the
example: Oziewicz's 1986 paper, his 1997 sequel, Jadczyk (2021) and Sobczyk's
null-vector papers, and an invitation to review the repository. 22 slides; the
notes are about 7,100 words, some 48 minutes when read by a synthetic voice.

**[View the slides](https://billpage.github.io/oziewicz/talks/grassmann_to_clifford/grassmann_to_clifford.html)**
(arrow keys or click to move, N shows the notes). The page is one file, about
1.2 MB; the formulas are SVG inside it, so it needs no network apart from the
web fonts, which fall back to system fonts.

Unlike [`npa2009/`](../npa2009/README.md), everything here is this repository's
own and under CC-BY-SA-4.0 (code: AGPL-3.0-or-later). Short formulas from the
papers discussed are restated, with their equation numbers, as in the
supplement.

*Status.* Drafted with Claude (Anthropic) on 17 November 2026 from the
supplement at commit `f1b7e34`, at which its 90 checks pass. Every formula on
the slides is taken from the supplement; a formula marked *checked* is checked
there. The one number added for the talk, the eigenvalue multiplicities of
slide 16 (`binom(n,k) 2^n`), was computed numerically for `n <= 5` (eigenvalues
of integer matrices) and is labelled so. Not yet read or heard by Bill Page.

## Files

| File | What it is |
|---|---|
| `slides.html` | The source: the slides, with formulas as TeX between `\(` `\)` and `\[` `\]`, images as `asset:NAME` and an empty `NOTES` array. Not a page to open |
| `notes/slide_NN.md` | The narration, one file per slide, in the speaker's voice |
| `grassmann_to_clifford.html` | The built page: formulas typeset as SVG, the figure embedded, `NOTES` filled. Input to `voiceover.py`, and served by GitHub Pages |
| `pronunciations.json` | For the synthetic voice: names, and a few spoken forms of symbols |
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

`voiceover.py` is in billpage/wpmw (`src/narration/voiceover.py`). Check the
spoken text first (seconds, no audio), then render with the Edge voice (needs
internet):

```bash
python3 ~/wpmw/src/narration/voiceover.py talks/grassmann_to_clifford/grassmann_to_clifford.html \
    --pronunciations talks/grassmann_to_clifford/pronunciations.json --preview -d ~/g2c-narration
python3 -u ~/wpmw/src/narration/voiceover.py talks/grassmann_to_clifford/grassmann_to_clifford.html \
    --pronunciations talks/grassmann_to_clifford/pronunciations.json \
    --tts edge --voice en-CA-LiamNeural --pause 30 --reencode 32 -d ~/g2c-narration
```

or record the notes in your own voice as `audio/slide_NN.mp3` in the output
folder and build with `--reuse-audio`. A narrated page is published as the
NPA talk's are: committed to `narrated/` on the `output` branch, with its
SHA-256 added to [`../narrated.sha256`](../narrated.sha256) on `main` through a
pull request, once Bill Page has listened to it.

## Sources

The papers are those of the supplement, §17, and of
[`references/bibliography.md`](../../references/bibliography.md). The
navigation script and page frame follow the slide decks of billpage/wpmw
(`docs/interactive/worlds_and_particles.html`).
