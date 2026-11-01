#!/usr/bin/env python3
"""Draws the site's night-sky band and favicon from the SENEX icon template (docs: DESIGN-TOKENS.md)."""

import math
import random
from pathlib import Path

ASSETS = Path(__file__).resolve().parent.parent / "src" / "assets"
ACCENT = "#8FB4FF"
GROUND = "#0D1117"
STAR = "rgb(220,228,255)"
SPARKLE = "rgb(232,240,255)"

W, H = 1600, 640
TREE_BASE = 0.93 * H


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


def sky():
    rng_stars = random.Random(7)
    rng_trees = random.Random(3)
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" preserveAspectRatio="xMidYMax slice">'
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


def favicon():
    return (
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">'
        f'<rect width="64" height="64" rx="14" fill="{GROUND}"/>'
        f'<polygon points="{sparkle(32, 32, 22)}" fill="{ACCENT}"/>'
        "</svg>\n"
    )


def main():
    ASSETS.mkdir(parents=True, exist_ok=True)
    (ASSETS / "sky.svg").write_text(sky())
    (ASSETS / "favicon.svg").write_text(favicon())


if __name__ == "__main__":
    main()
