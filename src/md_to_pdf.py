#!/usr/bin/env python3
r"""
Render a GitHub-flavoured markdown document with LaTeX math to PDF.

Written for WPMW's docs (billpage/wpmw, src/md_to_pdf.py) and used unchanged as the
github-md-to-pdf skill's script; it works on any repository's markdown.  The source file is never
modified: every rewrite below is applied to a temporary copy, which is then
rendered by Pandoc with the xelatex engine.

Math forms
----------
GitHub accepts six.  Pandoc reads ``$...$`` and ``$$...$$`` natively, and
``\(...\)`` / ``\[...\]`` with the ``tex_math_single_backslash`` extension,
which is enabled.  The two forms WPMW actually uses (see "Style guide for
math in WPMW markdown" in billpage/wpmw's src/README.md) are rewritten:

- inline ``$`...`$`` (backtick-guarded, so ``_`` / ``*`` inside the LaTeX are
  not read as emphasis) becomes ``$...$``.  A span may wrap across a source
  line; a match that would cross a blank line (a paragraph break) is left
  alone, since that can only be an unclosed span, which the linter reports.
- fenced ```` ```math ```` blocks become ``$$...$$``.  A fence nested in a
  list item or blockquote carries that context's indentation and/or ``>``
  on every line; the prefix is captured, required on the closing fence, and
  reapplied to every line of the restored block, so the math stays nested.

``--latex-fences`` also reads ```` ```latex ```` fences as display math.
Exporters such as Claude Docs write a document's display formulas that way;
GitHub shows them as code, so the option is off by default.

Escaped brackets.  A ``\[...\]`` is display math only when its ``\[``
opens a line.  Anywhere else outside code and math, ``\[`` / ``\]`` is a
CommonMark bracket escape -- an exporter writes ``d[X, a]`` as
``d\[X, a\]`` and a citation ``[6]`` as ``\[6\]`` -- and stays a bracket;
Pandoc's extension would otherwise tear it out of the sentence as a display
equation.

Doubled-backslash escapes (``\\;``, ``\\{``, ``\\}``, ...) are GitHub's
workaround for its CommonMark preprocessor stripping a lone backslash before
punctuation inside ``$...$``/``$$...$$``.  Real LaTeX reads ``\\`` as a line
break, so they are reduced to single-backslash form -- but only inside
genuine ``$...$``/``$$...$$`` spans.  Content from ```` ```math ```` blocks
and ``$`...`$`` spans is already natural LaTeX and may hold a deliberate
``\\`` (e.g. in ``\begin{cases}``), so it is stashed first and left untouched.

Other GitHub-versus-Pandoc differences
--------------------------------------
- Lists.  A bullet list (or a list starting at 1.) directly under a
  paragraph line, with no blank line, is a list on GitHub; Pandoc would merge
  it into the paragraph.  A blank line is inserted.
- Mermaid.  ```` ```mermaid ```` blocks are drawn to PNG with mermaid-cli
  (``mmdc``, or ``npx -p @mermaid-js/mermaid-cli``), pointing Puppeteer at a
  local Chromium.  If that fails the block stays as code, with a warning.
  ``--no-mermaid`` skips the attempt.
- Images.  ``--image-map PREFIX=DIR`` points image URLs starting with PREFIX
  at local files -- for figures on a branch not yet pushed, or no network.
- Strikethrough.  Pandoc's template loads ``soul`` and emits ``\st{...}``,
  which corrupts or crashes on content containing math.  ``ulem``'s
  ``\sout`` does not, so it is loaded and ``\st`` aliased to it.
- Glyphs.  ✓ ✔ ✗ ✘ ≅ ⋆ ∎ 𝓗 are missing from DejaVu Serif and would be
  silently dropped; they are mapped to math symbols with ``newunicodechar``
  when that package is installed.
- Links.  A relative link (``[text](../src/verify_x.py)``, ``[step 1](mass_centre.md#3)``)
  works on GitHub and nowhere else: in a PDF it points at a file beside the PDF
  on the reader's disk.  Each one is rewritten to the absolute address of its
  target on the hosting site, ``<repository>/blob/<ref>/<path>`` (``tree`` for a
  directory), so that it opens from any viewer.  The repository address comes
  from ``--link-base``, else from GitHub Actions' environment, else from the
  ``origin`` remote; the ref from ``--link-ref``, else the tag being built in
  a release run (so a released PDF links to the files of its own release), else
  the remote's default branch.  Absolute links, ``#fragment`` links inside the
  document, images, and anything in code or math are left alone.  A source file
  outside a git checkout, or with no recognisable remote, is rendered with its
  links unchanged and a warning.  ``--keep-relative-links`` turns this off.

Pre-flight and post-flight
--------------------------
Before rendering, the source is scanned for control characters and for a
TAB that ate a LaTeX command.  Both are the signature of a backslash escape
(``\a``, ``\b``, ``\f``, ``\v``, ``\t``) consumed by a non-raw Python string
when the markdown was generated -- e.g. ``\approx`` -> BEL + ``pprox``.
GitHub shows garbage there too, so the render is refused (exit status 2) and
the lines are listed; fix the SOURCE.  ``--allow-control-chars`` overrides.

After rendering, ``pdftotext`` is scanned for leftover ``$```, ```` ```math ````
or raw LaTeX commands, which indicate math that was not typeset.

Requirements
------------
``pandoc``, ``xelatex`` and the TeX packages lmodern, soul, ulem, hyphenat
and microtype; newunicodechar is optional.  On Debian/Ubuntu::

    apt-get install -y pandoc texlive-xetex lmodern texlive-plain-generic \
                       texlive-latex-extra

Usage
-----
    python3 md_to_pdf.py supplement/example_note.md
    python3 md_to_pdf.py doc.md -o /tmp/out.pdf
    python3 md_to_pdf.py doc.md -o out.pdf \
        --image-map https://raw.githubusercontent.com/billpage/oziewicz/output/figures/=./figs
    python3 md_to_pdf.py exported_from_claude_docs.md --latex-fences
    python3 md_to_pdf.py doc.md --link-base https://github.com/OWNER/REPO --link-ref main

With no ``-o``, inside the oziewicz repository the PDF is written via
``output_path()`` (see "Output paths" in README.md)
using the input's stem; a standalone copy writes ``<stem>.pdf`` beside the
input.

Known limitation
----------------
Equivalent in content to GitHub's preview, not pixel-identical: this uses
LaTeX's own typesetting, not GitHub's browser-side MathJax/KaTeX.  Pixel
fidelity would need a headless browser on the pushed page -- out of scope.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import urllib.parse
import shutil
import subprocess
import sys
import tempfile

try:  # inside the oziewicz repository: default output goes through output_path()
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from ozlib.utils import output_path  # noqa: E402
except ImportError:  # standalone copy (e.g. the github-md-to-pdf skill)
    output_path = None

_HEADER_INCLUDES = r"""
\usepackage[htt]{hyphenat}
\usepackage{microtype}
\emergencystretch=3em
\sloppy
\usepackage[normalem]{ulem}
\let\st\sout
\usepackage{amssymb}
\IfFileExists{newunicodechar.sty}{%
  \usepackage{newunicodechar}%
  \newunicodechar{✓}{\ensuremath{\checkmark}}%
  \newunicodechar{✔}{\ensuremath{\checkmark}}%
  \newunicodechar{✗}{\ensuremath{\times}}%
  \newunicodechar{✘}{\ensuremath{\times}}%
  \newunicodechar{≅}{\ensuremath{\cong}}%
  \newunicodechar{⋆}{\ensuremath{\star}}%
  \newunicodechar{∎}{\ensuremath{\blacksquare}}%
  \newunicodechar{𝓗}{\ensuremath{\mathcal{H}}}%
}{}
"""

# Group 1 is whatever leading indentation and/or blockquote markers (">")
# precede the fence -- required to match identically on the closing fence
# via the \1 backreference, so a fence nested in a list item or blockquote
# doesn't let an unrelated later ``` anywhere in the document act as its
# closing marker (see module docstring).
_FENCED_MATH = re.compile(r"^([ \t>]*)```math\n(.*?)\n\1```", re.DOTALL | re.MULTILINE)
# With --latex-fences, ```latex fences are display math too (see module
# docstring); GitHub itself shows them as code, so this is opt-in.
_FENCED_MATH_OR_LATEX = re.compile(r"^([ \t>]*)```(?:math|latex)\n(.*?)\n\1```",
                                   re.DOTALL | re.MULTILINE)
_BACKTICK_DOLLAR = re.compile(r"\$`([^`]+?)`\$", re.DOTALL)
_BLOCK_MATH = re.compile(r"\$\$(.+?)\$\$", re.DOTALL)
_INLINE_MATH = re.compile(
    r"(?<![\\$])\$(?![ \t\n$`])([^\n$]+?)(?<![ \t])\$(?![0-9$])"
)
# Two literal backslashes followed by one ASCII-punctuation character --
# GitHub's documented workaround for its own CommonMark backslash-strip.
_DOUBLED_ESCAPE = re.compile(r"\\\\([!\"#$%&'()*+,\-./:;<=>?@\[\]^_`{|}~])")


_MERMAID = re.compile(r"^([ \t>]*)```mermaid[ \t]*\n(.*?)\n\1```[ \t]*$",
                      re.DOTALL | re.MULTILINE)
# A bullet item, or an ordered item numbered 1 -- the only list starts that
# CommonMark lets interrupt a paragraph (GitHub renders them as lists; Pandoc
# needs a blank line first).
_LIST_START = re.compile(r"^\s*(?:[-*+]|1[.)])\s+\S")
_LIST_ITEM = re.compile(r"^\s*(?:[-*+]|\d+[.)])\s+\S")
_CONTROL = re.compile(r"[\x00-\x08\x0b\x0c\x0e-\x1f]")
_EATEN_TAB = re.compile(r"\t(?:hinspace|heta|imes|ilde|ext|extbf|frac|au)\b")


# Regions where a "\[" is not a CommonMark bracket escape: code (fenced or
# inline), math ($$...$$, $...$), and a \[...\] display block opening a line.
_BRACKET_PROTECTED = re.compile(
    r"^[ \t>]*(`{3,})[^\n]*\n.*?^[ \t>]*\1[^\n]*$"   # fenced code / math
    r"|(`+).+?(?<!`)\2(?!`)"                        # inline code span
    r"|\$\$.+?\$\$"                                 # display math
    r"|(?<![\\$])\$(?![ \t\n$])[^\n$]+?(?<![ \t\\])\$"  # inline math
    r"|^[ \t>]*\\\[.*?\\\]",                        # \[...\] opening a line
    re.DOTALL | re.MULTILINE)
_ESCAPED_BRACKET = re.compile(r"(?<!\\)\\([\[\]])")


def escape_literal_brackets(text: str) -> str:
    r"""Keep ``\[`` / ``\]`` that are CommonMark bracket escapes as brackets.

    With ``tex_math_single_backslash`` enabled, Pandoc reads every ``\[...\]``
    as display math.  GitHub documents no ``\[...\]`` math delimiter, and a
    markdown exporter writes a literal bracket in prose as ``\[`` (e.g.
    ``d\[X, α\]`` for a Frölicher--Nijenhuis bracket, or a citation ``\[6\]``),
    which Pandoc then tore out of the sentence as a display equation.  A
    ``\[...\]`` whose ``\[`` opens a line is still display math; every other
    unescaped ``\[`` / ``\]`` outside code and math becomes an HTML entity,
    which Pandoc prints as the bracket itself.
    """
    out, pos = [], 0
    for m in _BRACKET_PROTECTED.finditer(text):
        out.append(_ESCAPED_BRACKET.sub(
            lambda b: "&#91;" if b.group(1) == "[" else "&#93;", text[pos:m.start()]))
        out.append(m.group(0))
        pos = m.end()
    out.append(_ESCAPED_BRACKET.sub(
        lambda b: "&#91;" if b.group(1) == "[" else "&#93;", text[pos:]))
    return "".join(out)


def _reduce_doubled_escapes(expr: str) -> str:
    """\\\\X -> \\X, for real LaTeX. See module docstring."""
    return _DOUBLED_ESCAPE.sub(r"\\\1", expr)


# ------------------------------------------------------------------ pre-flight
def find_control_chars(text: str) -> list[tuple[int, str]]:
    """Lines holding control characters or a TAB that ate a LaTeX command --
    the signature of a backslash escape (\\a \\b \\f \\v \\t) consumed by a
    non-raw Python string when the markdown was generated."""
    hits = []
    for n, line in enumerate(text.split("\n"), 1):
        if _CONTROL.search(line.replace("\t", "")) or _EATEN_TAB.search(line):
            hits.append((n, line.encode("unicode_escape").decode()[:120]))
    return hits


# ------------------------------------------------------------------ rewriting
def separate_lists(text: str) -> str:
    """Insert a blank line between a paragraph line and a list that starts
    directly under it.  GitHub renders such a list; Pandoc would merge it into
    the paragraph.  Skips code fences and multi-line $$ blocks."""
    out: list[str] = []
    in_fence = in_display = False
    for line in text.split("\n"):
        if line.lstrip(" \t>").startswith("```"):
            in_fence = not in_fence
        elif not in_fence and line.count("$$") % 2 == 1:
            in_display = not in_display
        if not in_fence and not in_display and out and _LIST_START.match(line):
            prev = out[-1]
            if (prev.strip() and not _LIST_ITEM.match(prev)
                    and not prev.startswith((" ", "\t", ">", "|", "#"))):
                out.append("")
        out.append(line)
    return "\n".join(out)


def map_images(text: str, mappings: list[tuple[str, str]]) -> str:
    """Point image links whose URL starts with PREFIX at files in DIR."""
    for prefix, local in mappings:
        def sub(m: re.Match) -> str:
            path = os.path.join(local, m.group(2)[len(prefix):])
            if not os.path.exists(path):
                print(f"WARNING: mapped image not found: {path}", file=sys.stderr)
            return f"{m.group(1)}({path}"
        text = re.sub(r"(!\[[^\]]*\])\((" + re.escape(prefix) + r"[^)\s]*)", sub, text)
    return text


def _mmdc_cmd() -> list[str] | None:
    if shutil.which("mmdc"):
        return ["mmdc"]
    if shutil.which("npx"):
        return ["npx", "-y", "-p", "@mermaid-js/mermaid-cli", "mmdc"]
    return None


def _chromium() -> str | None:
    cands = [os.path.join(os.environ.get("PLAYWRIGHT_BROWSERS_PATH", "/opt/pw-browsers"), "chromium")]
    cands += [shutil.which(n) for n in ("chromium", "chromium-browser", "google-chrome")]
    for c in cands:
        if c and os.path.exists(c):
            return c
    return None


def render_mermaid(text: str, workdir: str) -> str:
    """Replace ```mermaid blocks by PNGs drawn with mermaid-cli; on any
    failure leave the block as code and warn."""
    cmd = _mmdc_cmd()
    n = 0

    def sub(m: re.Match) -> str:
        nonlocal n
        n += 1
        pre, body = m.group(1), m.group(2)
        body = "\n".join(l[len(pre):] if l.startswith(pre) else l for l in body.split("\n"))
        if cmd is None:
            print("WARNING: mermaid-cli not available; diagram left as code", file=sys.stderr)
            return m.group(0)
        src = os.path.join(workdir, f"mermaid{n}.mmd")
        png = os.path.join(workdir, f"mermaid{n}.png")
        with open(src, "w", encoding="utf-8") as f:
            f.write(body + "\n")
        args = cmd + ["-i", src, "-o", png, "-s", "3", "-b", "white"]
        chrome = _chromium()
        if chrome:
            cfg = os.path.join(workdir, "puppeteer.json")
            with open(cfg, "w") as f:
                json.dump({"executablePath": chrome, "args": ["--no-sandbox"]}, f)
            args += ["-p", cfg]
        env = dict(os.environ, PUPPETEER_SKIP_DOWNLOAD="1")
        try:
            r = subprocess.run(args, capture_output=True, text=True, env=env, timeout=180)
            ok = r.returncode == 0 and os.path.exists(png)
            err = r.stderr
        except (OSError, subprocess.TimeoutExpired) as e:
            ok, err = False, str(e)
        if not ok:
            print(f"WARNING: mermaid render failed; left as code\n{err[-400:]}", file=sys.stderr)
            return m.group(0)
        return f"{pre}![Diagram {n}]({png})"

    return _MERMAID.sub(sub, text)


def convert_math_delimiters(text: str, latex_fences: bool = False) -> str:
    """Rewrite the two GitHub math forms Pandoc doesn't parse natively, and
    reduce doubled-backslash escapes within genuine $...$/$$...$$ spans.

    ```` ```math ... ``` ```` fenced blocks and ``` $`...`$ ``` inline spans
    are stashed out first (their content is already natural single-backslash
    LaTeX and must not be touched -- it may contain a deliberate ``\\`` line
    break), then restored verbatim under Pandoc-native ``$$`` / ``$``
    delimiters. What's left after stashing is genuine ``$...$``/``$$...$$``
    content as WPMW's docs actually write it, where a doubled escape is
    reduced to single-backslash form before Pandoc sees it. Already-native
    ``\\(...\\)`` and ``\\[...\\]`` are left untouched (handled by Pandoc's
    ``tex_math_single_backslash`` extension instead).

    A fenced block nested inside a list item or blockquote carries that
    context's marker (indentation and/or ``>``) on every line, including
    the fence lines themselves. That shared prefix is captured and stripped
    from the content before stashing, then reapplied to every line of the
    restored ``$$...$$`` block, so the math stays correctly nested rather
    than being hoisted out of its list item or blockquote.

    A ``` $`...`$ ``` span may itself wrap across a source line break (a
    long expression hand-wrapped in prose); the non-greedy, backtick-free
    content class already stops at the first ``` `$ ```, so this is safe
    for the ordinary case. As a guard against the one degenerate case that
    isn't -- a genuinely unclosed opening ``` $` ``` with no backtick
    before its eventual, unrelated closing marker -- a match that would
    cross a blank line (a paragraph break, where CommonMark could not have
    intended a single span to continue) is left untouched rather than
    stashed, matching this project's own linter, which already flags an
    unclosed ``` $`...`$ ``` as a lint error rather than something this
    script should try to repair.
    """
    fenced_store: list[tuple[str, str]] = []

    def _stash_fenced(m: re.Match) -> str:
        prefix, content = m.group(1), m.group(2)
        if prefix:
            content = "\n".join(
                line[len(prefix):] if line.startswith(prefix) else line
                for line in content.split("\n")
            )
        fenced_store.append((prefix, content))
        return f"{prefix}\x00FENCED{len(fenced_store) - 1}\x00"

    fence = _FENCED_MATH_OR_LATEX if latex_fences else _FENCED_MATH
    text = fence.sub(_stash_fenced, text)

    backtick_store: list[str] = []

    def _stash_backtick(m: re.Match) -> str:
        content = m.group(1)
        if re.search(r"\n[ \t]*\n", content):
            return m.group(0)
        backtick_store.append(content)
        return f"\x00BACKTICK{len(backtick_store) - 1}\x00"

    text = _BACKTICK_DOLLAR.sub(_stash_backtick, text)

    text = _BLOCK_MATH.sub(
        lambda m: f"$${_reduce_doubled_escapes(m.group(1))}$$", text)
    text = _INLINE_MATH.sub(
        lambda m: f"${_reduce_doubled_escapes(m.group(1))}$", text)

    for i, (prefix, content) in enumerate(fenced_store):
        restored = f"$$\n{content.strip(chr(10))}\n$$"
        if prefix:
            restored = "\n".join(prefix + line for line in restored.split("\n"))
        text = text.replace(f"{prefix}\x00FENCED{i}\x00", restored)
    for i, content in enumerate(backtick_store):
        text = text.replace(f"\x00BACKTICK{i}\x00", f"${content}$")

    return text


# ------------------------------------------------------------------ post-flight
_POST_PAT = re.compile(r"\$`|```math|\\(?:frac|hbar|thinspace|mathrm|sqrt|partial|begin|left|right)\b")


def _literal_code(src_text: str, latex_fences: bool = False) -> str:
    """The source's code -- fenced blocks other than math/mermaid, and inline
    code spans other than $`...`$ math -- where the post-flight's patterns
    may legitimately appear as text (e.g. a style guide quoting the syntax)."""
    not_code = {"math", "mermaid", "latex"} if latex_fences else {"math", "mermaid"}
    blocks = _fenced_blocks(src_text)
    spans = re.findall(r"(?<![$`])(`+)(.+?)(?<!`)\1(?![`$])", src_text)
    return ("\n".join(b for lang, b in blocks if lang not in not_code)
            + "\n" + "\n".join(c for _, c in spans))


_FENCE_LINE = re.compile(r"^[ \t>]*(`{3,})([^`\n]*)$")


def _fenced_blocks(text: str) -> list[tuple[str, str]]:
    """(info word, body) of each fenced code block, paired as CommonMark
    pairs them: a block opened by n backticks closes only on a line of at
    least n backticks with nothing after them.  Regex pairing that let
    "```" close on the first three backticks of a "````" line, or that
    skipped a math fence's opening line without consuming its block, paired
    the rest of the document's fences wrongly."""
    out: list[tuple[str, str]] = []
    open_n, info, body = 0, "", []
    for line in text.split("\n"):
        m = _FENCE_LINE.match(line)
        if open_n:
            if m and len(m.group(1)) >= open_n and not m.group(2).strip():
                out.append((info, "\n".join(body)))
                open_n = 0
            else:
                body.append(line)
        elif m:
            open_n, body = len(m.group(1)), []
            info = (m.group(2).split() or [""])[0]
    return out


def post_check(pdf: str, src_text: str = "", latex_fences: bool = False) -> list[str]:
    """Lines of the PDF's text that look like untypeset math.  A pattern is
    reported only if it occurs more often in the PDF than in the source's own
    code, so documents that quote the syntax are not flagged."""
    if not shutil.which("pdftotext"):
        return []
    txt = subprocess.run(["pdftotext", pdf, "-"], capture_output=True, text=True).stdout
    allowed: dict[str, int] = {}
    for m in _POST_PAT.finditer(_literal_code(src_text, latex_fences)):
        allowed[m.group(0)] = allowed.get(m.group(0), 0) + 1
    found: dict[str, list[str]] = {}
    for line in txt.split("\n"):
        for m in _POST_PAT.finditer(line):
            found.setdefault(m.group(0), []).append(line)
    out: list[str] = []
    for tok, lines in found.items():
        if len(lines) > allowed.get(tok, 0):
            out += lines[:3]
    return out[:10]


# A markdown inline link that is not an image: [text](target "title").  The
# text may hold one level of nested brackets and may wrap across a line.
_INLINE_LINK = re.compile(
    r"(?<!!)(\[(?:[^\[\]]|\[[^\[\]]*\])*\])\(\s*([^()\s]+)(\s+\"[^\"\n]*\")?\s*\)")
# A reference-style link definition:  [label]: target
_LINK_DEF = re.compile(r"^([ \t>]{0,3}\[[^\]\n]+\]:[ \t]*)(\S+)", re.MULTILINE)
_URL_SCHEME = re.compile(r"[A-Za-z][A-Za-z0-9+.\-]*:")


def _git(args: list[str], cwd: str) -> str | None:
    try:
        r = subprocess.run(["git", "-C", cwd] + args, capture_output=True, text=True,
                           timeout=30)
    except (OSError, subprocess.TimeoutExpired):
        return None
    return r.stdout.strip() if r.returncode == 0 and r.stdout.strip() else None


def _web_url(remote: str) -> str | None:
    """The browsable address of a git remote: ``git@host:o/r.git`` and
    ``https://user@host/o/r.git`` both give ``https://host/o/r``."""
    m = re.fullmatch(r"(?:ssh://)?git@([^:/]+)[:/](.+?)(?:\.git)?/?", remote)
    if m:
        return f"https://{m.group(1)}/{m.group(2)}"
    m = re.fullmatch(r"https?://(?:[^@/]+@)?([^/]+)/(.+?)(?:\.git)?/?", remote)
    if m and "." in m.group(1) and not re.match(r"[\d.:]+$|localhost", m.group(1)):
        return f"https://{m.group(1)}/{m.group(2)}"
    return None


def link_context(src_path: str, link_base: str | None = None,
                 link_ref: str | None = None) -> tuple[str, str, str] | None:
    """Where relative links of ``src_path`` point on the hosting site, as
    ``(repository root on disk, repository address, ref)``; None if unknown."""
    src_dir = os.path.dirname(os.path.abspath(src_path))
    root = _git(["rev-parse", "--show-toplevel"], src_dir)
    if root is None:
        return None
    env = os.environ
    base = link_base
    if not base and env.get("GITHUB_SERVER_URL") and env.get("GITHUB_REPOSITORY"):
        base = f"{env['GITHUB_SERVER_URL']}/{env['GITHUB_REPOSITORY']}"
    if not base:
        base = _web_url(_git(["remote", "get-url", "origin"], src_dir) or "")
    if not base:
        return None
    ref = link_ref
    if not ref and env.get("GITHUB_REF_TYPE") == "tag" and env.get("GITHUB_REF_NAME"):
        ref = env["GITHUB_REF_NAME"]
    if not ref:
        head = _git(["symbolic-ref", "-q", "--short", "refs/remotes/origin/HEAD"], src_dir)
        ref = head.split("/", 1)[1] if head and "/" in head else "main"
    return os.path.realpath(root), base.rstrip("/"), ref


def absolutize_links(text: str, src_path: str, ctx: tuple[str, str, str]) -> tuple[str, int]:
    """Rewrite relative link targets to absolute addresses on the hosting site.

    Returns the new text and the number of links rewritten.  Images are left
    for Pandoc to read from disk; links that start inside code or math are not
    links; a target that leaves the repository is left as it is, with a warning.
    """
    root, base, ref = ctx
    src_dir = os.path.dirname(os.path.realpath(src_path))
    protected = [(m.start(), m.end()) for m in _BRACKET_PROTECTED.finditer(text)]
    count = 0

    def inside(pos: int) -> bool:
        return any(a <= pos < b for a, b in protected)

    def absolute(target: str) -> str | None:
        if _URL_SCHEME.match(target) or target.startswith(("#", "//", "<")):
            return None
        path, sep, frag = target.partition("#")
        if not path:
            return None
        path = urllib.parse.unquote(path)
        full = (os.path.join(root, path.lstrip("/")) if path.startswith("/")
                else os.path.join(src_dir, path))
        full = os.path.normpath(full)
        rel = os.path.relpath(full, root)
        if rel == os.pardir or rel.startswith(os.pardir + os.sep):
            print(f"WARNING: link leaves the repository, left relative: {target}",
                  file=sys.stderr)
            return None
        if not os.path.exists(full):
            print(f"WARNING: link target not found in the checkout: {target}", file=sys.stderr)
        kind = "tree" if os.path.isdir(full) else "blob"
        rel = "" if rel == os.curdir else urllib.parse.quote(rel.replace(os.sep, "/"))
        url = f"{base}/{kind}/{urllib.parse.quote(ref, safe='/')}" + (f"/{rel}" if rel else "")
        return url + sep + frag

    def inline(m: re.Match) -> str:
        nonlocal count
        new = None if inside(m.start()) else absolute(m.group(2))
        if new is None:
            return m.group(0)
        count += 1
        return f"{m.group(1)}({new}{m.group(3) or ''})"

    def definition(m: re.Match) -> str:
        nonlocal count
        new = None if inside(m.start()) else absolute(m.group(2))
        if new is None:
            return m.group(0)
        count += 1
        return m.group(1) + new

    # Both passes use offsets into the same text, so do the definitions (whole
    # lines, never overlapping an inline link) on the result of the first pass
    # with the protected spans recomputed.
    text = _INLINE_LINK.sub(inline, text)
    protected = [(m.start(), m.end()) for m in _BRACKET_PROTECTED.finditer(text)]
    text = _LINK_DEF.sub(definition, text)
    return text, count


def prepare(text: str, workdir: str, image_map=(), mermaid: bool = True,
            latex_fences: bool = False, src_path: str | None = None,
            link_ctx: tuple[str, str, str] | None = None) -> str:
    """All source-to-Pandoc rewriting, in order."""
    if mermaid:
        text = render_mermaid(text, workdir)
    text = map_images(text, list(image_map))
    if src_path and link_ctx:
        text, n = absolutize_links(text, src_path, link_ctx)
        if n:
            print(f"Rewrote {n} relative link(s) to {link_ctx[1]}/blob/{link_ctx[2]}/...")
    text = separate_lists(text)
    text = convert_math_delimiters(text, latex_fences)
    return escape_literal_brackets(text)


def render_pdf(src_path: str, dst_path: str, timeout: int = 180, image_map=(),
               toc: bool = True, mermaid: bool = True,
               allow_control_chars: bool = False, latex_fences: bool = False,
               absolute_links: bool = True, link_base: str | None = None,
               link_ref: str | None = None) -> None:
    """Convert ``src_path`` (GitHub-flavoured math markdown) to a PDF at
    ``dst_path``.  Exits 2 if the pre-flight finds control characters."""
    with open(src_path, encoding="utf-8") as f:
        text = f.read()
    bad = find_control_chars(text)
    if bad:
        print("Control characters / eaten escapes in the source -- fix the SOURCE:",
              file=sys.stderr)
        for n, l in bad:
            print(f"  line {n}: {l}", file=sys.stderr)
        if not allow_control_chars:
            sys.exit(2)

    link_ctx = link_context(src_path, link_base, link_ref) if absolute_links else None
    if absolute_links and link_ctx is None:
        print("WARNING: no repository address found (not a git checkout, or no usable "
              "'origin'); relative links are left as they are. Pass --link-base.",
              file=sys.stderr)

    with tempfile.TemporaryDirectory() as td:
        prepped = prepare(text, td, image_map, mermaid, latex_fences, src_path, link_ctx)
        md_path = os.path.join(td, "prepped.md")
        header_path = os.path.join(td, "header.tex")
        with open(md_path, "w", encoding="utf-8") as f:
            f.write(prepped)
        with open(header_path, "w", encoding="utf-8") as f:
            f.write(_HEADER_INCLUDES)
        cmd = [
            "pandoc", md_path, "-o", dst_path,
            "-f", "markdown+tex_math_single_backslash",
            "--pdf-engine=xelatex",
            "-V", "mainfont=DejaVu Serif",
            "-V", "monofont=DejaVu Sans Mono",
            "-V", "geometry:margin=1in",
            "-V", "linkcolor=blue",
            "-H", header_path,
            "--resource-path", os.path.dirname(os.path.abspath(src_path)),
        ]
        if toc:
            cmd.append("--toc")
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)
        for l in r.stderr.splitlines():
            if any(k in l for k in ("Missing character", "Could not fetch", "rror")):
                print(l, file=sys.stderr)
        if r.returncode:
            miss = re.findall(r"File `([^']+\.sty)' not found", r.stderr)
            if miss:
                print(f"Missing TeX package(s): {miss} -- see the install line above",
                      file=sys.stderr)
            raise subprocess.CalledProcessError(r.returncode, cmd, r.stdout, r.stderr)

    left = post_check(dst_path, text, latex_fences)
    if left:
        print("WARNING: possible untypeset math in the PDF text:", file=sys.stderr)
        for l in left:
            print("  " + l[:120], file=sys.stderr)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.strip().splitlines()[0])
    parser.add_argument("input", help="path to the source markdown file")
    parser.add_argument("-o", "--output",
                        help="destination PDF (default: output_path(<stem>.pdf) inside "
                             "oziewicz, else <input stem>.pdf beside the input)")
    parser.add_argument("--image-map", action="append", default=[], metavar="PREFIX=DIR",
                        help="rewrite image URLs starting with PREFIX to files in DIR "
                             "(repeatable)")
    parser.add_argument("--no-toc", action="store_true", help="omit the table of contents")
    parser.add_argument("--no-mermaid", action="store_true",
                        help="leave ```mermaid blocks as code")
    parser.add_argument("--allow-control-chars", action="store_true",
                        help="render despite the control-character pre-flight")
    parser.add_argument("--latex-fences", action="store_true",
                        help="typeset ```latex fenced blocks as display math, as written by "
                             "exporters such as Claude Docs (GitHub shows them as code)")
    parser.add_argument("--link-base", metavar="URL",
                        help="repository address for relative links, e.g. "
                             "https://github.com/OWNER/REPO (default: GitHub Actions' "
                             "environment, else the 'origin' remote)")
    parser.add_argument("--link-ref", metavar="REF",
                        help="branch or tag that relative links point at (default: the tag "
                             "being built in a release run, else the default branch)")
    parser.add_argument("--keep-relative-links", action="store_true",
                        help="do not rewrite relative links to absolute addresses")
    args = parser.parse_args()

    maps = [tuple(m.split("=", 1)) for m in args.image_map]
    stem = os.path.splitext(os.path.basename(args.input))[0]
    if args.output:
        dst = args.output
    elif output_path is not None:
        dst = output_path(f"{stem}.pdf")
    else:
        dst = os.path.splitext(args.input)[0] + ".pdf"

    render_pdf(args.input, dst, image_map=maps, toc=not args.no_toc,
               mermaid=not args.no_mermaid,
               allow_control_chars=args.allow_control_chars,
               latex_fences=args.latex_fences,
               absolute_links=not args.keep_relative_links,
               link_base=args.link_base, link_ref=args.link_ref)
    print(f"Wrote {dst}")


if __name__ == "__main__":
    main()
