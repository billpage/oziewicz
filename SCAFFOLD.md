# Scaffold record

This repository was created from `billpage/wpmw` using the `research-repo-scaffold`
skill (plugin `research` in `billpage/claude-plugins`). Copied files differ from
their originals only in names and in the path changes listed below, so drift can
be found by diffing against the recorded commit.

| Parameter | Value |
|---|---|
| REPO | billpage/oziewicz |
| PKG | ozlib |
| PREFIX | OZ (`OZ_OUTPUT`, `OZ_DOCS`) |
| DOCS_ROOT | `.` (repository root) |
| SECTIONS | analysis supplement notebooks |
| wpmw commit | `4128ad93b34dc3edcaf88aad4fc3b4fa0007ef9d` (2026-10-29) |
| Scaffolded | 2026-10-31 |

## Copied from wpmw

| Here | wpmw original |
|---|---|
| `src/ozlib/utils.py` | `src/wpmwlib/wpmw_utils.py` |
| `src/ozlib/check_md_math.py` | `src/wpmwlib/check_md_math.py` |
| `src/ozlib/check_notebook_math.py` | `src/wpmwlib/check_notebook_math.py` |
| `src/md_to_pdf.py` | `src/md_to_pdf.py` |
| `.github/workflows/check_md_math.yml` | same name |
| `.github/workflows/docs-release.yml` | same name |
| `.github/workflows/pages.yml` | same name |
| `.gitignore`, `LICENSE`, `LICENSE-DOCS` | same names |

Changes: identifiers (`wpmwlib` to `ozlib`, `WPMW_` to `OZ_`, repository name); the
default paths of the two linters, now the root section directories; the workflows
now read `analysis supplement notebooks` instead of `docs/`; `pages.yml` builds the
root with `source: .` and has no step that publishes the `output` branch (wpmw's
narrated-slides step); `docs-release.yml` loops over the section directories;
wording of the AGPL notice and of `LICENSE-DOCS` (which directories it covers);
a few comments in `check_md_math.py` and `md_to_pdf.py` keep naming wpmw where
they cite wpmw documents. `_config.yml` is new (Jekyll excludes).

Not copied: demos, wpmw physics modules, narration tools, `kaggle_runner.ipynb`,
`kaggle_batch.py`, `check_abstracts`, `check_index`, `where_used`, any wpmw
document. The last three tools and `GLOSSARY.md` / `analysis/INDEX.md` come with
the first derivation ladder and need the same default-path change.

## Not yet done (owner)

- Settings, Pages, Source: GitHub Actions.
- Protect `main` (require a pull request; require the `check` job of the `check-md-math` workflow
  once it has run once). Then delete the qualification in `AI-USE.md` that says
  protection is not yet enabled.
- Actions workflow permissions, if workflow runs are restricted.
