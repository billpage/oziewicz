# Instructions for AI agents

Read [`README.md`](README.md), [`ORIENTATION.md`](ORIENTATION.md) and
[`AI-USE.md`](AI-USE.md) first. This file is the short version of the rules.

- **Delivery.** Never push to `main`. Push a branch named `claude/<topic>` and let
  the owner open and merge the pull request. Pushing directly to the `output`
  branch is allowed (figures and rendered notebooks only) and is disclosed in
  `AI-USE.md`. Commit as `Claude <claude@anthropic.invalid>`.
- **Before committing markdown:** `npm install katex mathjax-full` once, then
  `PYTHONPATH=src python3 -m ozlib.check_md_math analysis supplement notebooks README.md ORIENTATION.md AI-USE.md AGENTS.md GLOSSARY.md references`.
  Notebooks: `PYTHONPATH=src python3 -m ozlib.check_notebook_math notebooks`.
  Ladder: `PYTHONPATH=src python3 -m ozlib.check_abstracts analysis` (README entry
  = the note's title blockquote, word for word) and
  `PYTHONPATH=src python3 -m ozlib.check_index analysis` (every labelled result
  and open item has a row in `analysis/INDEX.md`).
- **Math in markdown:** GitHub conventions as described in the docstring of
  `src/ozlib/check_md_math.py` (inline math in backtick-dollar form, display math
  in fenced `math` blocks).
- **Output paths:** write every generated file through `ozlib.utils.output_path`
  (and `docs_path` for the `output` branch). No hardcoded paths, no `shutil.copy2`.
- **Never commit:** copyrighted PDFs (link to arXiv, the publisher or ResearchGate
  in `references/bibliography.md`), unpublished drafts, personal or admin files.
- **Claims about Oziewicz's papers** are interpretations. Say which paper and
  which statement, and do not present a summary as verified fact about the paper.
- **Exact before numerical:** check identities with a computer algebra system and
  say which; mark anything numerical as numerical.
- Drop version suffixes from filenames. Code is for verification and graphics only.
