# Scaffold record

This repository was created from `billpage/wpmw` using the `research-repo-scaffold`
skill (plugin `research` in `billpage/claude-plugins`). Copied files differ from
their originals only in names, paths and the changes listed below, so drift can
be found by diffing against the recorded commit. Last checked 3 November 2026: the
13 files of the next section were diffed against that commit, after the identifier
substitutions, and every difference is one listed here.

| Parameter | Value |
|---|---|
| REPO | billpage/oziewicz |
| PKG | ozlib |
| PREFIX | OZ (`OZ_OUTPUT`, `OZ_DOCS`) |
| DOCS_ROOT | `.` (repository root) |
| SECTIONS | analysis supplement notebooks |
| Later section | talks (2026-11-02): linted in CI, not in the linters' default paths or in `docs-release.yml` |
| wpmw commit | `4128ad93b34dc3edcaf88aad4fc3b4fa0007ef9d` (2026-10-29) |
| Scaffolded | 2026-10-31 |

## Copied from wpmw

| Here | wpmw original |
|---|---|
| `src/ozlib/utils.py` | `src/wpmwlib/wpmw_utils.py` |
| `src/ozlib/check_md_math.py` | `src/wpmwlib/check_md_math.py` |
| `src/ozlib/check_notebook_math.py` | `src/wpmwlib/check_notebook_math.py` |
| `src/ozlib/check_abstracts.py`, added 2026-11-01 with step 1 | `src/wpmwlib/check_abstracts.py` |
| `src/ozlib/check_index.py`, added the same day | `src/wpmwlib/check_index.py` |
| `src/ozlib/where_used.py`, added the same day | `src/wpmwlib/where_used.py` |
| `src/md_to_pdf.py` | `src/md_to_pdf.py` |
| `.github/workflows/check_md_math.yml` | same name |
| `.github/workflows/docs-release.yml` | same name |
| `.github/workflows/pages.yml` | same name |
| `.gitignore`, `LICENSE`, `LICENSE-DOCS` | same names |

Changes made when copying: identifiers (`wpmwlib` to `ozlib`, `WPMW_` to `OZ_`,
repository name); the default paths of the linters, now the root section
directories; the workflows read the section directories instead of `docs/`;
`pages.yml` builds the root with `source: .`; `docs-release.yml` loops over the
section directories; wording of the AGPL notice and of `LICENSE-DOCS` (which
directories it covers); the docstring of `docs_path`, which now describes the
`output` branch; the examples in `where_used.py`. A few comments in
`check_md_math.py` and `md_to_pdf.py` keep naming wpmw where they cite wpmw
documents, and each ladder tool names the wpmw commit in its first lines.

Changes since, to copied files:

- `check_md_math.yml`: also runs `check_abstracts` and `check_index` (2026-11-01),
  and lints `talks/` (2026-11-02). wpmw's workflow does neither.
- `pages.yml` (2026-11-02): the scaffold had removed wpmw's step that publishes
  narrated pages from the `output` branch. It is back in a stricter form: wpmw
  copies every narrated page, and this repository copies only those whose SHA-256
  is listed in `talks/narrated.sha256` on `main`.

Written here, not copied: `_config.yml` (Jekyll excludes),
`src/narration/build_slides.py`, the `src/verify_*.py` scripts, `GLOSSARY.md` and
`analysis/INDEX.md`.

Not copied: demos, wpmw physics modules, the narration tools
(`voiceover.py` is run from a clone of wpmw; see `talks/npa2009/README.md`),
`kaggle_runner.ipynb`, any wpmw document, and `kaggle_batch.py`, which is to be
copied when the first long run needs it.

## Owner steps

Done 2026-10-31 (checked from public GitHub data after the merge): Pages source is
GitHub Actions and the `pages` workflow succeeded; the site answers at
https://billpage.github.io/oziewicz/; `main` is protected by an active ruleset
requiring a pull request. Read from the GitHub API on 3 November 2026: the ruleset
"first" is active on the default branch, with no deletion, no force-push, and a pull
request with no approving review required.

Still open:

- **Publish a first PDF release.** Push a `docs-v*` tag, review the draft release
  and publish it. `docs-release.yml` has not been run and no tag exists, so the PDF
  links in five documents are dead until then: `clock_centre`, `metric_free_body`,
  `ternary_mass_centre`, `bodies_first` and `velocity_draft`. Its render step was
  tried locally on 3 November 2026 and all five built, with a stand-in for
  `ulem.sty`, which the sandbox lacks; whether the packages CI installs provide it
  is what the first run will show. `analysis/mass_centre.md` and
  `supplement/oziewicz_on_science.md` have no PDF link.
- **Required status check.** The ruleset has none. Do not add the `check` job of
  `check-md-math` as the workflow stands. Its `paths` filter means that a pull
  request touching none of those paths never reports the check, and GitHub then
  [keeps it pending and blocks the merge](https://docs.github.com/en/pull-requests/how-tos/merge-and-close-pull-requests/troubleshooting-required-status-checks).
  Remove the filter first. The filter also omits `check_abstracts.py` and
  `check_index.py`.
- Actions workflow permissions: not checked (the session cannot read that setting).
