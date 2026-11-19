# AI use and authorship in this repository

This document expands on the "AI collaboration and authorship" section of
[`README.md`](README.md). It tells a reader, collaborator or prospective citer how
AI was involved, what that does and does not mean for the reliability of a claim,
and how it bears on the licences in [`LICENSE`](LICENSE) and
[`LICENSE-DOCS`](LICENSE-DOCS).

Last reviewed: November 2026. Practice in this area (publisher policy, copyright
guidance, community norms) is still moving. The reasoning in the "Why AI isn't
listed" and "Copyright" sections is adapted from the same document in
`billpage/wpmw` as of its commit `4128ad9` (reviewed there September 2026); the
legal and policy statements were not independently re-checked for this repository.
On 12 November 2026 the description of branches, `output` and the narrated-page
hash gate was checked against `.github/workflows/pages.yml`, `talks/narrated.sha256`
and `talks/`; the description of the ruleset rests on the check recorded in
[`SCAFFOLD.md`](SCAFFOLD.md) (31 October 2026), not on a new look at the settings.

## Who does what

- **Bill Page** owns the repository and directs the research: he poses the
  questions, decides how Oziewicz's claims are to be read and what is worth
  pursuing, and merges every change to `main`. He was a co-author with Oziewicz of
  one of the papers examined (see [`ORIENTATION.md`](ORIENTATION.md)).
- **Claude** (Anthropic) drafts notes and derivations, writes and runs the code
  that checks them, builds figures and notebooks, researches the literature, and
  proposes options. It does not choose among them, set the direction, or approve
  its own work as the final check.
- There are no other collaborators at present.

Claude is credited at the commit level (`Claude <claude@anthropic.invalid>` in the
git history) but is not listed as an author in `CITATION.cff` or in any citation.
See "Why AI isn't listed as a research author" below.

## How changes are delivered

Claude has push access to this repository, under these rules:

| Branch | Who pushes | Review |
|---|---|---|
| `main` | Bill only, by merging a pull request | Bill reviews the diff before merging. |
| `claude/<topic>` | Claude | The branch is what Bill reviews, as a pull request. |
| `output` | Claude may push directly | **Not reviewed commit by commit.** |

`main` is protected by a repository ruleset ("first", enforcement active, applying
to the default branch) with three rules: no deletion, no force-push, and changes
only through a pull request. It requires no approving review, because Bill is the
only reviewer, so the protection ensures that every change is a visible pull
request, not that a second person approved it. The required `check-md-math`
status check is not part of the ruleset yet.

One qualification applies to the `output` branch. It holds figures, rendered
notebooks and narrated slide pages. Because Claude may push there without review, **a figure or rendered
notebook on `output` was not individually checked by a human before it landed**. A
document on `main` that embeds a figure has had its text reviewed; whether the
figure is the right one is a separate question, and the note says how it was
checked. Content from `output` is not published on the project's web pages, with
one exception: narrated slide pages in `narrated/`, whose SHA-256 must be listed
in `talks/narrated.sha256` on `main` before the Pages workflow will publish them.
That list changes only through a reviewed pull request, and Claude adds a hash
only for a page Bill has checked, so a published page is byte for byte one he
has seen.

## What "verified" means here

A claim marked verified was executed and checked against theory: run against the
current code, not only derived on paper, with the result compared to what the
derivation predicts, or to an exact solution or known limit. Where a claim can be
checked exactly (an identity, a coefficient, a sign), the note says which computer
algebra system was used; numerical checks are labelled as numerical. A
disagreement between a live result and a number quoted in a note is flagged
explicitly, not quietly reconciled.

Verified here never means that Oziewicz's claim is true or that a summary of his
claim is faithful to his paper. It means that a stated mathematical step was
reproduced. The reading of what he meant is an interpretation (see
[`ORIENTATION.md`](ORIENTATION.md)).

This standard guards against unverified, sometimes hallucinated, output entering
the record unexamined. It is not external peer review, which this repository has
not had.

## Why AI isn't listed as a research author

Guidance from the ACM, the Committee on Publication Ethics and most major
publishers converges: an AI system should not be listed as an author, because
authorship requires the ability to understand what was written, consent to its
publication and take responsibility if it is wrong. The same guidance asks for
disclosure of what was AI-assisted and how it was checked. This document and the
commit history are that disclosure.

## Copyright and the licence terms

United States copyright requires meaningful human authorship; work generated by
an AI system without meaningful human creative control is not copyrightable. Where
a human directs the work, exercises real editorial control and makes the
substantive decisions, using AI as a tool, the human is the author. The division of
labour above is the fact pattern that supports Bill's authorship, and is why
[`LICENSE`](LICENSE) (AGPL-3.0-or-later, for `src/`) and
[`LICENSE-DOCS`](LICENSE-DOCS) (CC-BY-SA-4.0, for the documents and figures) name
Bill Page as licensor. This is not legal advice. Material on the `output` branch
that Bill has not reviewed is the weakest part of that fact pattern.

The licences cover only this repository's own content. They do not cover
Oziewicz's papers, which are linked and not reproduced, nor the slides, words
and recordings of his talks in `talks/` and in `narrated/` on `output`, which are
included by Bill's decision with a `NOTICE.md` for each talk.

## Unpublished drafts

Bill has access to draft papers, some co-authored. They are not committed here. A
draft is linked where it is public; otherwise a summary written for this repository
may go in `supplement/`, produced in the same reviewed way as any other note and
making clear that it summarises a draft that is not available to the reader.

## For readers

Nothing here has been through external peer review. The verification standard is
internal to the project, carried out by the same people, and the same AI, that
produce the claims. Apply the scrutiny you would apply to any unreviewed research
repository, and follow the links in [`references/bibliography.md`](references/bibliography.md)
to the originals before relying on a statement about what Oziewicz wrote.
