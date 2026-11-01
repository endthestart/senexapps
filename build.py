#!/usr/bin/env python3
"""Builds senexapps.com into site/: wraps each page in src/pages with src/layout.html.

A page starts with `key: value` lines (title, description, optional nav), then a line `---`.
The build fails on a missing header field or a link to a file the site does not have.
"""

import re
import shutil
from pathlib import Path
from string import Template

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "src"
OUT = ROOT / "site"
REQUIRED = {"title", "description"}
NAV = (
    ("pictor", "/pictor/", "Pictor"),
    ("corvus", "/corvus/", "Corvus"),
    ("support", "/support/", "Support"),
    ("about", "/about/", "About"),
)
SPARKLE = (
    '<svg viewBox="0 0 16 16" aria-hidden="true" focusable="false">'
    '<polygon fill="currentColor" points="8,0 9.24,6.76 16,8 9.24,9.24 8,16 6.76,9.24 0,8 6.76,6.76"/>'
    "</svg>"
)
LOCAL_LINK = re.compile(r'(?:href|src)="(/[^"#]*)')


def parse(page):
    head, sep, body = page.read_text().partition("\n---\n")
    if not sep:
        raise SystemExit(f"{page}: no '---' line after the header")
    meta = dict(line.split(": ", 1) for line in head.splitlines())
    missing = REQUIRED - meta.keys()
    if missing:
        raise SystemExit(f"{page}: header lacks {', '.join(sorted(missing))}")
    if meta.get("nav") not in (None, *(key for key, _, _ in NAV)):
        raise SystemExit(f"{page}: unknown nav {meta['nav']!r}")
    return meta, body.strip()


def url_path(relative):
    if relative.name == "index.html":
        parent = relative.parent.as_posix()
        return "/" if parent == "." else f"/{parent}/"
    return f"/{relative.as_posix()}"


def nav_items(active):
    items = []
    for key, href, label in NAV:
        current = ' aria-current="page"' if key == active else ""
        items.append(f'      <li><a href="{href}"{current}>{label}</a></li>')
    return "\n".join(items)


def check_links():
    broken = []
    for page in OUT.rglob("*.html"):
        for link in LOCAL_LINK.findall(page.read_text()):
            target = OUT / link.lstrip("/")
            if link.endswith("/"):
                target = target / "index.html"
            if not target.is_file():
                broken.append(f"{page.relative_to(OUT)} → {link}")
    if broken:
        raise SystemExit("Broken links:\n" + "\n".join(broken))


def main():
    layout = Template((SRC / "layout.html").read_text())
    if OUT.exists():
        shutil.rmtree(OUT)
    shutil.copytree(SRC / "assets", OUT / "assets")
    pages = sorted((SRC / "pages").rglob("*.html"))
    for page in pages:
        meta, body = parse(page)
        relative = page.relative_to(SRC / "pages")
        target = OUT / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(
            layout.substitute(
                title=meta["title"],
                description=meta["description"],
                path=url_path(relative),
                nav=nav_items(meta.get("nav")),
                sparkle=SPARKLE,
                content=body,
            )
        )
    check_links()
    print(f"Built {len(pages)} pages into {OUT.relative_to(ROOT)}/")


if __name__ == "__main__":
    main()
