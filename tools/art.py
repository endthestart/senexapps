#!/usr/bin/env python3
"""Draws the site's night-sky band, favicon, share image, and the Lyra and Towpath icons.

The sky and the Lyra icon follow the SENEX icon template (DESIGN-TOKENS.md in Corvus and Pictor).
"""

import math
import random
from pathlib import Path

TOOLS = Path(__file__).resolve().parent
ASSETS = TOOLS.parent / "src" / "assets"
ACCENT = "#8FB4FF"
GROUND = "#0D1117"
STAR = "rgb(220,228,255)"
SPARKLE = "rgb(232,240,255)"

W, H = 1600, 640
SHARE_W, SHARE_H = 1200, 630
TREE_BASE = 0.93 * H

S, PAD = 1024, 100
TILE = f'<rect x="{PAD}" y="{PAD}" width="{S - 2 * PAD}" height="{S - 2 * PAD}" rx="185"'
LYRA_STARS = {
    "α": (279.235, 38.784, 0.03),
    "ε": (281.085, 39.670, 4.67),
    "ζ": (281.193, 37.605, 4.34),
    "δ": (283.626, 36.899, 4.22),
    "γ": (284.736, 32.690, 3.25),
    "β": (282.520, 33.363, 3.52),
}
LYRA_FIGURE = ("αεζα", "ζδγβζ")
LYRA_SEEDS = (23, 9)


def sparkle(cx, cy, r):
    points = []
    for k in range(8):
        angle = math.radians(k * 45 - 90)
        radius = r if k % 2 == 0 else 0.22 * r
        points.append(f"{cx + radius * math.cos(angle):.1f},{cy + radius * math.sin(angle):.1f}")
    return " ".join(points)


def milky_way():
    ellipses = []
    for k in range(60):
        t = k / 60
        cx = 120 + t * (W - 240)
        cy = 0.80 * H - t * 0.62 * H
        ellipses.append(f'<ellipse cx="{cx:.0f}" cy="{cy:.0f}" rx="190" ry="80"/>')
    return (
        '<g filter="url(#blur)" fill="rgb(150,165,230)" fill-opacity="0.045">'
        + "".join(ellipses)
        + "</g>"
    )


def stars(rng):
    dots = []
    for _ in range(320):
        x = rng.uniform(0, W)
        y = rng.uniform(0, 0.88 * H)
        r = rng.choice((0.7, 1.0, 1.4, 1.9))
        alpha = rng.randint(90, 255) / 255
        dots.append(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{r}" fill-opacity="{alpha:.2f}"/>')
    return f'<g fill="{STAR}">' + "".join(dots) + "</g>"


def bright_stars():
    marks = []
    for cx, cy, r in ((1240, 210, 17), (1470, 360, 11), (1010, 170, 9)):
        marks.append(
            f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{ACCENT}" fill-opacity="0.35" filter="url(#halo)"/>'
            f'<polygon points="{sparkle(cx, cy, r)}" fill="{SPARKLE}"/>'
        )
    return "".join(marks)


def treeline(rng):
    trees = []
    x = -20.0
    while x < W + 20:
        w = rng.uniform(26, 52)
        h = rng.uniform(40, 140)
        trees.append(f"M{x:.0f} {TREE_BASE:.0f}L{x + w / 2:.0f} {TREE_BASE - h:.0f}L{x + w:.0f} {TREE_BASE:.0f}Z")
        x += 0.8 * w
    ground = f"M0 {TREE_BASE - 1:.0f}H{W}V{H}H0Z"
    return f'<path fill="{GROUND}" d="{"".join(trees)}{ground}"/>'


def sky(size=""):
    rng_stars = random.Random(7)
    rng_trees = random.Random(3)
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}"{size} preserveAspectRatio="xMidYMax slice">'
        "<defs>"
        '<linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">'
        '<stop offset="0" stop-color="rgb(10,16,36)"/><stop offset="1" stop-color="rgb(24,38,78)"/>'
        "</linearGradient>"
        '<filter id="blur" x="-20%" y="-20%" width="140%" height="140%"><feGaussianBlur stdDeviation="40"/></filter>'
        '<filter id="halo" x="-100%" y="-100%" width="300%" height="300%"><feGaussianBlur stdDeviation="8"/></filter>'
        "</defs>"
        f'<rect width="{W}" height="{H}" fill="url(#sky)"/>'
        + milky_way()
        + stars(rng_stars)
        + bright_stars()
        + treeline(rng_trees)
        + "</svg>\n"
    )


def share():
    font = "-apple-system, 'Helvetica Neue', Helvetica, Arial, sans-serif"
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {SHARE_W} {SHARE_H}">'
        + sky(f' width="{SHARE_W}" height="{SHARE_H}"').strip()
        + f'<polygon points="{sparkle(102, 216, 26)}" fill="{ACCENT}"/>'
        f'<g font-family="{font}" font-weight="600" fill="#e6eaf0">'
        '<text x="146" y="236" font-size="54" letter-spacing="10">SENEX</text>'
        '<text x="76" y="352" font-size="62" letter-spacing="-1.2">Apps that run on your own machines.</text>'
        '</g>'
        f'<text x="76" y="412" font-family="{font}" font-size="30" fill="#c9d1dc">'
        "Photo, music, a personal archive and local AI.</text>"
        "</svg>\n"
    )


def favicon():
    return (
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">'
        f'<rect width="64" height="64" rx="14" fill="{GROUND}"/>'
        f'<polygon points="{sparkle(32, 32, 22)}" fill="{ACCENT}"/>'
        "</svg>\n"
    )


def project(stars):
    ras = [ra for ra, _, _ in stars.values()]
    decs = [dec for _, dec, _ in stars.values()]
    ra0, dec0 = (min(ras) + max(ras)) / 2, (min(decs) + max(decs)) / 2
    flat = {
        name: (-(ra - ra0) * math.cos(math.radians(dec0)), -(dec - dec0))
        for name, (ra, dec, _) in stars.items()
    }
    width = 2 * max(abs(x) for x, _ in flat.values())
    height = 2 * max(abs(y) for _, y in flat.values())
    scale = 0.34 * S / max(width, height)
    return {name: (0.50 * S + x * scale, 0.36 * S + y * scale) for name, (x, y) in flat.items()}


def emblem(stars, figure):
    at = project(stars)
    lines = "".join(
        '<polyline points="' + " ".join(f"{at[name][0]:.1f},{at[name][1]:.1f}" for name in path) + '"/>'
        for path in figure
    )
    filters, halos, sparkles = [], [], []
    for index, (name, (_, _, magnitude)) in enumerate(stars.items()):
        cx, cy = at[name]
        r = min(64, max(28, 64 - 16 * (magnitude - 2.6)))
        filters.append(
            f'<filter id="halo{index}" x="-150%" y="-150%" width="400%" height="400%">'
            f'<feGaussianBlur stdDeviation="{0.5 * r:.1f}"/></filter>'
        )
        halos.append(
            f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r:.1f}" fill="{ACCENT}" fill-opacity="0.47"'
            f' filter="url(#halo{index})"/>'
        )
        sparkles.append(f'<polygon points="{sparkle(cx, cy, r)}" fill="{SPARKLE}"/>')
    figure_lines = (
        f'<g fill="none" stroke="{ACCENT}" stroke-opacity="0.59" stroke-width="5" stroke-linecap="round"'
        f' stroke-linejoin="round">{lines}</g>'
    )
    return "".join(filters), figure_lines + "".join(halos) + "".join(sparkles)


def icon(stars, figure, seeds):
    rng_dots, rng_trees = random.Random(seeds[0]), random.Random(seeds[1])
    ellipses = []
    for k in range(60):
        t = k / 60
        cx = PAD + 80 + t * (S - 2 * PAD - 160)
        ellipses.append(f'<ellipse cx="{cx:.0f}" cy="{0.62 * S - t * 0.38 * S:.0f}" rx="120" ry="60"/>')
    dots = []
    for _ in range(140):
        x = rng_dots.uniform(PAD, S - PAD)
        y = rng_dots.uniform(PAD, 0.72 * S)
        r = rng_dots.choice((1.2, 1.6, 2.2, 2.8))
        alpha = rng_dots.randint(120, 255) / 255
        dots.append(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{r}" fill-opacity="{alpha:.2f}"/>')
    base = 0.78 * S
    trees = []
    x = float(PAD)
    while x < S - PAD:
        w = rng_trees.uniform(26, 52)
        h = rng_trees.uniform(60, 190)
        trees.append(f"M{x:.0f} {base:.0f}L{x + w / 2:.0f} {base - h:.0f}L{x + w:.0f} {base:.0f}Z")
        x += 0.8 * w
    ground = f"M{PAD} {base:.0f}H{S - PAD}V{S - PAD}H{PAD}Z"
    halo_filters, figure_marks = emblem(stars, figure)
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {S} {S}">'
        "<defs>"
        '<linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">'
        '<stop offset="0" stop-color="rgb(10,16,36)"/><stop offset="1" stop-color="rgb(24,38,78)"/>'
        "</linearGradient>"
        '<filter id="blur" x="-20%" y="-20%" width="140%" height="140%"><feGaussianBlur stdDeviation="40"/></filter>'
        f'<clipPath id="tile">{TILE}/></clipPath>'
        + halo_filters
        + "</defs>"
        '<g clip-path="url(#tile)">'
        f'<rect width="{S}" height="{S}" fill="url(#sky)"/>'
        '<g filter="url(#blur)" fill="rgb(150,165,230)" opacity="0.04">' + "".join(ellipses) + "</g>"
        f'<g fill="{STAR}">' + "".join(dots) + "</g>"
        + figure_marks
        + f'<path fill="rgb(6,9,14)" d="{"".join(trees)}{ground}"/>'
        "</g></svg>\n"
    )


def towpath_icon():
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {S} {S}">'
        f'{TILE} fill="#1d1f27"/>'
        '<g fill="none" stroke-linecap="round">'
        '<path d="M250 730C470 730 520 450 780 430" stroke="#2c4a7a" stroke-width="96"/>'
        f'<path d="M250 580C420 580 470 310 700 290" stroke="{ACCENT}" stroke-width="26" stroke-dasharray="1 62"/>'
        "</g>"
        f'<circle cx="760" cy="286" r="34" fill="{SPARKLE}"/>'
        "</svg>\n"
    )


def main():
    (ASSETS / "img").mkdir(parents=True, exist_ok=True)
    (ASSETS / "sky.svg").write_text(sky())
    (ASSETS / "favicon.svg").write_text(favicon())
    (ASSETS / "img" / "lyra.svg").write_text(icon(LYRA_STARS, LYRA_FIGURE, LYRA_SEEDS))
    (ASSETS / "img" / "towpath.svg").write_text(towpath_icon())
    (TOOLS / "share.svg").write_text(share())


if __name__ == "__main__":
    main()
