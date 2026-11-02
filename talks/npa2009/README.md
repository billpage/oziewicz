# *What is Special Relativity Theory?* (Oziewicz, NPA 2009): narrated slides

Zbigniew Oziewicz gave this talk online to the relativity discussion group of
the Natural Philosophy Alliance (NPA). Its slides are a Beamer PDF dated 29
December 2009. The argument is that of *Ternary relative velocity* (2007), read
in [`supplement/bodies_first.md`](../../supplement/bodies_first.md#6-the-astonishing-conflict)
§6. The slides, the words of the talk and the recording are Oziewicz's and are
not under this repository's licences: see [`NOTICE.md`](NOTICE.md).

**Play the talk** (each page is one self-contained file, about 30 MB, which also
plays offline when saved):

- [In Oziewicz's own voice](https://billpage.github.io/oziewicz/narrated/npa2009_oziewicz_narrated.html):
  the recording of the talk, one clip per slide, with the transcript beside it.
- [Read by a synthetic voice](https://billpage.github.io/oziewicz/narrated/npa2009_andrew_narrated.html)
  (Microsoft Edge `en-US-AndrewNeural`): the same transcript, read aloud
  without the chat asides; about 60 minutes against 90 for the recording.

Keys: left and right arrows change slide, Space plays and pauses, T shows or
hides the transcript, C turns on continuous play.

*Status.* Notes for positions 1-17 are Bill Page's corrected transcript of
2021; positions 18-55, and the checking of all of them, were drafted with
Claude (Anthropic) on 1 November 2026 from Whisper transcripts. Bill Page
listened to both narrated pages on 2 November 2026. The points below were
checked against transcripts and sources, not settled by ear.

## Files

| Where | File | What it is |
|---|---|---|
| here | `npa2009.html` | The slides page: 55 positions, each a page of the PDF as an SVG image, with the notes in `const NOTES`. It is the input to `voiceover.py` and shows nothing by itself |
| here | `notes/slide_NN.md` | The notes, one file per position; positions 52 and 54 have none (shown without comment) |
| here | `slide_to_pdfpage.json` | Position → PDF page (1-39) |
| here | `pronunciations.json` | For the synthetic voice: drops the bracketed stage directions and respells names |
| `src/narration/` | `build_slides.py` | Builds `npa2009.html` from the PDF, the order and the notes |
| `talks/` | `narrated.sha256` | SHA-256 of each narrated page that may be published (see below) |
| `output` branch | `narrated/npa2009_oziewicz_narrated.html` | Oziewicz's voice, audio embedded (32 kbit/s mono) |
| `output` branch | `narrated/npa2009_andrew_narrated.html` | Synthetic voice, audio embedded |

## Deck order and audio

The order is the one Bill Page reconstructed in 2021. Oziewicz moves through
the 39 PDF pages and returns to some of them, which gives 55 positions:

```
position: 1 … 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 …
PDF page: 1 … 9  7  9 10 11 10 11 10 11 12 13 14 10 14 15 16 17 18 16 19 …
position: 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55
PDF page: 20 21 22 23 24 23 24 25 26 27 28 29 30 29 11 30 31 30 32 33 34 35 36 37 38 39 35
```

The audio of each position is a clip that Bill Page cut in 2021 from the
recording (91 min 40 s), following an Audacity label track. The recording's
first 82.8 s, before the talk begins, are left out. The clips run end to end
with no gaps up to "Thank you very much. I have no more."

## How the notes were made

1. Every clip was transcribed with Whisper `medium.en` (faster-whisper, int8,
   beam 5, voice-activity filter on, with a prompt naming the people and
   terms). Clips 18-55 were transcribed again with `small.en`, without the
   filter and without conditioning on earlier text, because Whisper drops
   disfluent speech. A word-level comparison of the two passes found three
   dropped passages (positions 33, 41, 44), which are in the notes.
2. **Positions 1-17** start from Bill Page's corrected notes of May 2021, made
   by listening. Whisper was used only to check names and wording.
3. **Positions 18-55** are new, from the two Whisper passes read against the
   slide each passage refers to.
4. Editing rules: keep Oziewicz's words and order; correct grammar only where
   the meaning is unambiguous; drop false starts, repetitions and room
   business. When he reads or answers the online chat, the text is marked
   `[Reading the chat]` or `[Answering the chat]`. `[…]` marks a passage that
   could not be made out. Nothing is added that he did not say.

## Points not settled by the transcripts

| Position | Text | Basis | Note |
|---|---|---|---|
| 1, 20, 23, 41, 51 | Robert **Kiehn** | Whisper: "Ken", "King", "Kim", "Kien"; 2021 notes: Kiehn | R. M. Kiehn took part in the NPA discussions |
| 8 | **Yuval Ne'eman** in Israel | 2021 notes: "Ezra Newman"; Whisper: "Yuval Newman" | Ne'eman worked in Israel; Ezra T. Newman in Pittsburgh |
| 17 | John **Huang** | 2021 notes: "John Wang"; Whisper: "John Huang" (twice) | PDF page 3 lists John Huang |
| 35 | "[…] Bergmann also starts from this definition" | Whisper: "And the world conference on special relativity, Bergman also start…" | Possibly "the well-known book on special relativity" |
| 35 | Minkowski's paper "written in 1908" | Whisper: "1905" | PDF page 24 has Minkowski 1908 |
| 51 | **Hehl** in Germany | Whisper: "Herr" | Hehl and Obukhov, *Foundations of Classical Electrodynamics: Charge, Flux, and Metric* (2003) |
| 51 | "v over c to the fourth power" | `medium.en`: "V over C 2.4"; `small.en`: "V over C to power 4" | PDF page 36: `(v_AB + v_BA)^2 = -2(gamma-1)(1-1/gamma^2) = -beta^4 - O(beta^6)`, checked in SymPy (`src/verify_relative_velocity.py`, Part E) |
| 53 | **Dingle** | Whisper: "Dingell" | Herbert Dingle |
| 55 | "hyperbolic geometry and **Euclidean** geometry are the same" | `medium.en`: "real"; `small.en`: "crion" | |
| 35, 41, 53 | "Alfred" | a participant in the chat | not identified |

## Statements in the talk that are his, not established

The notes keep what he said. These should not be repeated without checking:

- Position 26: he calls Grassmann "a priest"; Grassmann was a gymnasium
  teacher who had studied theology. The King of Sweden's prize (Oscar II) was
  awarded in 1889, not "around 1895", and the editor of *Acta Mathematica* was
  Mittag-Leffler, not Möbius. The withdrawn printing and Poincaré's error are
  historical.
- Positions 35 and 48: he says Minkowski's paper defining the monad "has never
  been translated into English". Meghnad Saha translated *Die Grundgleichungen
  für die elektromagnetischen Vorgänge in bewegten Körpern* (1908) in Saha and
  Bose, *The Principle of Relativity* (Calcutta 1920;
  [Project Gutenberg 66944](https://www.gutenberg.org/ebooks/66944)). Unless he
  meant another paper, the statement is wrong.
- Position 35: he says the posthumous "Minkowski" papers were written by Max
  Born. Born edited and completed Minkowski's posthumous 1910 paper in
  *Mathematische Annalen*; whether it differs from Minkowski in substance is
  his judgement.
- The argument itself (positions 36-53, the "astonishing conflict"):
  [`supplement/bodies_first.md`](../../supplement/bodies_first.md#6-the-astonishing-conflict) §6.

## Rebuilding and publishing

`voiceover.py` is in billpage/wpmw (`src/narration/voiceover.py`); its `main`
includes the guard that keeps the page quiet in sandboxed previews. The PDF and
the clips are not in the repository.

```bash
# notes -> slides page (needs pdftocairo)
OZ_OUTPUT=talks/npa2009 PYTHONPATH=src python3 src/narration/build_slides.py \
    --pdf /path/to/NPA2009-Beamer.pdf --talk talks/npa2009 --name npa2009 \
    --title "What is Special Relativity Theory?"

# Oziewicz's voice: put clip-N.mp3 as <outdir>/audio/slide_NN.mp3, then
python3 ~/wpmw/src/narration/voiceover.py talks/npa2009/npa2009.html \
    --name npa2009_oziewicz -d ~/npa2009-oziewicz --reuse-audio --reencode 32

# Synthetic voice (Edge, needs internet; python3 -m venv .venv && pip install edge-tts)
python3 -u ~/wpmw/src/narration/voiceover.py talks/npa2009/npa2009.html \
    --name npa2009_andrew -d ~/npa2009-andrew --pronunciations talks/npa2009/pronunciations.json \
    --tts edge --voice en-US-AndrewNeural --reencode 32
```

A narrated page is published by committing it to `narrated/` on the `output`
branch and adding its SHA-256 to [`talks/narrated.sha256`](../narrated.sha256)
on `main`, through a pull request. The Pages workflow publishes only the files
whose hash is listed, so a page is served only after its hash has been reviewed
on `main` (see [`AI-USE.md`](../../AI-USE.md)). The two pages listed now are
the ones Bill Page listened to on 2 November 2026:
`npa2009_andrew_narrated.html` is his local render byte for byte, and
`npa2009_oziewicz_narrated.html` is the single-file build of 1 November, made
from the same `npa2009.html` and clips as the copy he played.

## References

- Z. Oziewicz, "Ternary relative velocity; astonishing conflict of the Lorentz
  group with relativity", in V. Gladyshev (ed.), *Physical Interpretations of
  Relativity Theory*, Moscow 2007, pp. 292-303;
  [arXiv:1104.0682](https://arxiv.org/abs/1104.0682).
- Z. Oziewicz, "Relativity groupoid, instead of relativity group",
  [arXiv:math/0608770](https://arxiv.org/abs/math/0608770).
- Z. Oziewicz and W. S. Page, "Concepts of relative velocity",
  [arXiv:1104.0684](https://arxiv.org/abs/1104.0684).
- Further references (Urbantke, Ungar, Mocanu, Bargmann-Michel-Telegdi):
  [`references/bibliography.md`](../../references/bibliography.md).
