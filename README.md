# oziewicz

A reading of the work of Zbigniew Oziewicz (died 2020) in mathematical physics:
the conceptual and mathematical foundations of relativity and quantum mechanics,
and related pure mathematics. The repository holds derivations and review notes
that check his claims against computation where they can be checked, plus the
small amount of code needed to do that checking and to draw figures.

This is a working set of research notes, not a polished library. Conventions may
change, and nothing here has had external peer review.

Oziewicz's own papers are **not** in this repository. They are cited by link in
[`references/bibliography.md`](references/bibliography.md).

## In memoriam

Zbigniew Oziewicz (22 August 1941 - 8 December 2020) argued in print and in
talks that science is subjective, that it should be based on dissent, that
everybody has a right to be right, and that a referee system which blocks
alternative ideas is a danger to it. He called his own group of relativity
critics dissidents, and he wrote against Karl Popper's demarcation of science
from pseudo-science. These notes are partly a memorial to that way of working.
[`supplement/oziewicz_on_science.md`](supplement/oziewicz_on_science.md) gives
each of his slogans and where it can be found.

The notes try to keep faith with it in three ways:

- They state each claim in its strongest form before testing it, and do not
  discount a claim for being unorthodox.
- They check the mathematics, not allegiance: whether an identity holds, whether
  a construction composes, whether a statement follows from its premises. They
  take no position on which theory nature chooses.
- They report the result either way. Where a construction turns out to be
  standard special relativity in other notation, the note says so. Where a
  conflict he found survives, the note says that too.

He held that science needs no criterion for deciding who is right. A repository
that checks derivations does not share that view, and this section does not
claim that he would have agreed with its method.

## Getting started

Clone only `main`:

```bash
git clone --single-branch --branch main https://github.com/billpage/oziewicz.git
cd oziewicz
```

This skips the `output` branch, which holds figures and rendered notebooks as
binary files. Figures are embedded in the notes by raw GitHub URL and display
without cloning. To produce figures yourself, see
[Sharing figures](#sharing-figures-via-the-output-branch).

## Repository layout

```
analysis/     Derivations and review notes (a numbered ladder, once the first
              note exists)
supplement/   Background, worked test cases, summaries of unpublished drafts
talks/        Oziewicz's talks as narrated slide pages: notes and sources here,
              the pages with audio on the `output` branch (see talks/README.md)
notebooks/    Notebook companions (outputs stripped; rendered copies are on
              the `output` branch)
src/          Verification and graphics code only
  ozlib/      Shared modules: output-path helpers and the linters
references/   bibliography.md (links to papers; PDFs are NOT committed)
```

[`ORIENTATION.md`](ORIENTATION.md) says what the project is trying to do and
which claims are established, open or retracted. Each document directory has its
own README. The glossary and the theorem index
(`GLOSSARY.md`, `analysis/INDEX.md`) are provided to aid access to the notes by
subject.

## Output path convention

Python scripts write every generated file (figures, CSVs, ...) through the helpers
in `src/ozlib/utils.py`.

```python
from ozlib.utils import output_path, docs_path

fig.savefig(output_path("my_figure.png"), dpi=150, bbox_inches="tight")
dp = docs_path("my_figure.png")      # None unless OZ_DOCS is set
if dp:
    fig.savefig(dp, dpi=150, bbox_inches="tight")
```

| Context | `OZ_OUTPUT` | `OZ_DOCS` |
|---|---|---|
| Claude container | `/mnt/user-data/outputs` | (unset) |
| Kaggle | `/kaggle/working` | (unset) |
| Local | (unset: `./output`) | `~/oziewicz-output` (worktree) |

## Sharing figures via the `output` branch

Figures and rendered notebooks live on an orphan `output` branch, so `main` stays
free of binary files. One-time setup of a worktree:

```bash
git fetch origin output
git worktree add ../oziewicz-output output
```

Produce figures, then commit them from the worktree:

```bash
export OZ_OUTPUT=./output
export OZ_DOCS=~/oziewicz-output
python src/my_script.py
cd ~/oziewicz-output
git add figures/my_figure.png
git commit -m "add my_figure"
git push origin output
```

Embed on `main` with
`https://raw.githubusercontent.com/billpage/oziewicz/output/<subdir>/<filename>`.

The `output` branch is not reviewed commit by commit. Of its content only the
narrated slide pages in `narrated/` are published on the project's web pages, and
only those whose SHA-256 is listed in `talks/narrated.sha256` on `main`; see
[`AI-USE.md`](AI-USE.md) and [`talks/README.md`](talks/README.md).

## PDF releases

A document opts in to a PDF companion by linking to its own PDF at the stable URL
below, using its own filename stem:

```markdown
[PDF](https://github.com/billpage/oziewicz/releases/latest/download/my_note.pdf)
```

Pushing a tag `docs-v*` runs `.github/workflows/docs-release.yml`, which renders
every document under `analysis/`, `supplement/` and `notebooks/` that contains
such a self-link with `src/md_to_pdf.py` and opens a **draft** release. Nothing is
public until the draft is reviewed and published by hand. Filename stems must be
unique across those directories, because the release URL is flat. Keep version
identifiers in the tag, not in the PDF filename.

## Documentation checks

From the repository root, before committing a change to any markdown file
(needs `npm install katex mathjax-full` once; exits 1 on a problem):

```bash
PYTHONPATH=src python3 -m ozlib.check_md_math analysis supplement notebooks talks \
    README.md ORIENTATION.md AI-USE.md AGENTS.md GLOSSARY.md references
PYTHONPATH=src python3 -m ozlib.check_notebook_math notebooks
```

`check_md_math` finds math that GitHub will not render. It runs in CI on every
pull request. `check_notebook_math` checks notebook math delimiters and is not
run in CI. The ladder checks (`check_abstracts`, `check_index`, `where_used`) are
added with the first ladder.

## File conventions

- Follow the existing directory structure. Drop version suffixes from filenames:
  git tracks revisions.
- Do not commit copyrighted PDFs, personal files or admin material. Papers go in
  `references/bibliography.md` as links.
- Unpublished drafts are not committed. Link them where they are public;
  otherwise a summary written for this repository goes in `supplement/`.
- Exception: a talk in `talks/` (slides as images, transcript, recording) that
  Bill has decided to include, with a `NOTICE.md`. The PDF itself is not
  committed.

## AI collaboration and authorship

This repository is a collaboration between Bill Page and Claude (Anthropic).
Bill directs the research and decides every design and interpretive question.
Claude drafts notes, writes and runs verification code, and is credited as commit
author, but is not a research author. Changes to `main` arrive as pull requests
from `claude/<topic>` branches that Bill reviews and merges. Claude may push
directly to the `output` branch, whose contents are therefore not individually
reviewed. [`AI-USE.md`](AI-USE.md) gives the details and what "verified" means here.

## License

- **Code** (`src/`): [GNU Affero General Public License v3.0 or
  later](LICENSE) (`AGPL-3.0-or-later`).
- **Documentation, derivations and figures** (`analysis/`, `supplement/`,
  `notebooks/`, `references/`, the top-level markdown files, and the files on the
  `output` branch): [Creative Commons Attribution-ShareAlike 4.0
  International](LICENSE-DOCS) (`CC-BY-SA-4.0`).

These licences cover this repository's own content only. Oziewicz's papers, and
any text quoted from other authors, remain under their own terms. So do his
slides, the words of his talks and his recorded voice in `talks/` and in
`narrated/` on the `output` branch; each talk's `NOTICE.md` says what they are
and on what basis they are included.

## Citation

A machine-readable entry is in [`CITATION.cff`](CITATION.cff). Plain text:

> Bill Page (2026). *oziewicz: notes and derivations on the mathematical physics of
> Zbigniew Oziewicz* [Research notes]. https://github.com/billpage/oziewicz
