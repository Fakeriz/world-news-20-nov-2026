#!/usr/bin/env python3
"""Draw the 20 Nov 2026 world-news front page: 1024x1024 PNG."""
from PIL import Image, ImageDraw, ImageFont
import math

W, H = 1024, 1024
PAPER = (253, 252, 248)
INK = (26, 26, 26)
RED = (176, 30, 36)
GREY = (201, 196, 184)
DARKGREY = (90, 88, 84)

F = "/usr/share/fonts/truetype/dejavu/"
serif_b = ImageFont.truetype(F + "DejaVuSerif-Bold.ttf", 96)
sans_b34 = ImageFont.truetype(F + "DejaVuSans-Bold.ttf", 34)
sans_b30 = ImageFont.truetype(F + "DejaVuSans-Bold.ttf", 30)
sans_b17 = ImageFont.truetype(F + "DejaVuSans-Bold.ttf", 17)
sans19 = ImageFont.truetype(F + "DejaVuSans.ttf", 19)
sans17 = ImageFont.truetype(F + "DejaVuSans.ttf", 17)
sans16 = ImageFont.truetype(F + "DejaVuSans.ttf", 16)

img = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(img)
MX = 36  # side margin


def center(y, text, font, fill):
    w = d.textlength(text, font=font)
    d.text(((W - w) / 2, y), text, font=font, fill=fill)


def wrap(text, font, maxw):
    words, lines, cur = text.split(), [], ""
    for word in words:
        trial = (cur + " " + word).strip()
        if d.textlength(trial, font=font) <= maxw:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


# ---------------- masthead ----------------
center(22, "THE WORLD", serif_b, INK)
d.rectangle([MX, 132, W - MX, 136], fill=RED)
center(146, "FRIDAY 20 NOVEMBER 2026", sans_b34, RED)
d.rectangle([MX, 192, W - MX, 194], fill=INK)

# ---------------- tile illustrations ----------------
def ill_markets(bx, by, bw, bh):
    d.rectangle([bx, by, bx + bw, by + bh], fill=(31, 42, 68))
    for gx in range(1, 6):
        x = bx + gx * bw // 6
        d.line([x, by + 8, x, by + bh - 8], fill=(255, 255, 255, 40), width=1)
    pts = [(bx + 12, by + 16), (bx + 90, by + 30), (bx + 160, by + 24),
           (bx + 240, by + 48), (bx + 320, by + 44), (bx + bw - 16, by + bh - 14)]
    d.line(pts, fill=(232, 72, 72), width=6, joint="curve")
    for (x, y) in pts:
        d.ellipse([x - 5, y - 5, x + 5, y + 5], fill=(255, 255, 255))
    ex, ey = pts[-1]
    d.polygon([(ex, ey - 10), (ex + 16, ey + 2), (ex, ey + 10)], fill=(232, 72, 72))


def ill_climate(bx, by, bw, bh):
    d.rectangle([bx, by, bx + bw, by + bh], fill=(14, 107, 92))
    cx, cy, r = bx + 120, by + bh // 2, 34
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(127, 200, 181))
    d.ellipse([cx - 22, cy - 18, cx + 2, cy + 2], fill=(46, 139, 87))
    d.ellipse([cx - 2, cy + 6, cx + 22, cy + 24], fill=(46, 139, 87))
    sx, sy = bx + bw - 70, by + 22
    d.ellipse([sx - 14, sy - 14, sx + 14, sy + 14], fill=(245, 200, 80))
    for ang in range(0, 360, 45):
        a = math.radians(ang)
        x1 = sx + 20 * math.cos(a); y1 = sy + 20 * math.sin(a)
        x2 = sx + 28 * math.cos(a); y2 = sy + 28 * math.sin(a)
        d.line([x1, y1, x2, y2], fill=(245, 200, 80), width=4)


def ill_ukraine(bx, by, bw, bh):
    d.rectangle([bx, by, bx + bw, by + bh], fill=(46, 74, 122))
    base = by + bh
    heights = [34, 52, 28, 60, 40, 48, 30, 56]
    x = bx + 8
    for hgt in heights:
        wdt = (bw - 130) // len(heights)
        d.rectangle([x, base - hgt, x + wdt - 3, base], fill=(22, 38, 66))
        x += wdt
    sx = bx + bw - 108
    d.polygon([(sx, by + 12), (sx + 64, by + 12), (sx + 64, by + 44),
               (sx + 32, by + 72), (sx, by + 44)], fill=(245, 200, 80))
    d.rectangle([sx + 14, by + 26, sx + 50, by + 34], fill=(46, 74, 122))
    d.rectangle([sx + 14, by + 40, sx + 50, by + 46], fill=(255, 255, 255))


def ill_europe(bx, by, bw, bh):
    d.rectangle([bx, by, bx + bw, by + bh], fill=(220, 233, 245))
    cx, cy = bx + 110, by + bh // 2
    for i in range(12):
        a = math.radians(i * 30)
        x = cx + 52 * math.cos(a); y = cy + 30 * math.sin(a)
        d.ellipse([x - 5, y - 5, x + 5, y + 5], fill=(245, 200, 80))
    d.ellipse([cx - 16, cy - 16, cx + 16, cy + 16], fill=(38, 68, 140))
    d.line([bx + 230, by + 20, bx + 230, by + bh - 20], fill=(38, 68, 140), width=5)
    d.line([bx + 240, by + 20, bx + bw - 20, by + 20], fill=(38, 68, 140), width=5)
    d.polygon([(bx + 240, by + 20), (bx + bw - 20, by + 20),
               (bx + bw - 20, by + 34), (bx + 240, by + 34)], fill=(245, 200, 80))
    d.polygon([(bx + 240, by + 44), (bx + bw - 20, by + 44),
               (bx + bw - 20, by + 58), (bx + 240, by + 58)], fill=(176, 30, 36))


def ill_usa(bx, by, bw, bh):
    d.rectangle([bx, by, bx + bw, by + bh], fill=(243, 233, 215))
    cx, cy, r = bx + 110, by + bh // 2, 36
    d.ellipse([cx - r, cy - r, cx + r, cy + r], outline=(176, 30, 36), width=4, fill=(255, 255, 255))
    d.arc([cx - 26, cy - 26, cx + 26, cy + 26], 205, 335, fill=(176, 30, 36), width=4)
    d.arc([cx - 26, cy - 26, cx + 26, cy + 26], 25, 155, fill=(176, 30, 36), width=4)
    d.line([bx + 250, by + 66, bx + 322, by + 18], fill=(150, 105, 60), width=13)
    d.ellipse([bx + 316, by + 10, bx + 334, by + 28], fill=(120, 80, 40))
    d.ellipse([bx + 240, by + 60, bx + 256, by + 76], fill=(120, 80, 40))


def ill_tech(bx, by, bw, bh):
    d.rectangle([bx, by, bx + bw, by + bh], fill=(18, 59, 42))
    cx, cy = bx + 110, by + bh // 2
    d.ellipse([cx - 34, cy - 26, cx + 34, cy + 26], fill=(64, 160, 110))
    d.line([cx + 30, cy + 24, cx + 52, cy + 34], fill=(140, 220, 170), width=4)
    for (nx, ny) in [(bx + 250, by + 20), (bx + 320, by + 46), (bx + 270, by + 66), (bx + 380, by + 30)]:
        d.line([cx + 40, cy, nx, ny], fill=(140, 220, 170), width=3)
        d.ellipse([nx - 7, ny - 7, nx + 7, ny + 7], fill=(245, 200, 80))
    d.ellipse([cx + 33, cy - 7, cx + 47, cy + 7], fill=(245, 200, 80))


ILL = {"markets": ill_markets, "climate": ill_climate, "ukraine": ill_ukraine,
       "europe": ill_europe, "usa": ill_usa, "tech": ill_tech}

STORIES = [
    ("markets", "MARKETS", "AI-bubble fears sink Asian markets",
     "Nikkei falls; SoftBank down over 16% as Wall Street drops for a fifth day."),
    ("climate", "CLIMATE", "COP31 talks stall as fossil-fuel pledge cut",
     "Near-final texts drop the transition language; no deal in sight at crunch time."),
    ("ukraine", "UKRAINE", "Kyiv hit again as UK pledges 1,000 drones",
     "Fresh missile attack on Friday; £260m package for Ukraine."),
    ("europe", "EUROPE", "UK and EU agree youth mobility 'reset'",
     "Deal struck at Brussels summit to reset relations."),
    ("usa", "USA", "Trump pardons Pete Rose, posthumously",
     "Baseball legend cleared decades after his ban."),
    ("tech", "TECH", "Meta rethinks 2030 net-zero goal as AI grows",
     "Company 'reevaluating' climate target amid AI buildout."),
]

# ---------------- grid ----------------
GX, GY = MX, 206
TW, TH, GAP = 468, 240, 12
for i, (key, kicker, headline, deck) in enumerate(STORIES):
    col, row = i % 2, i // 2
    x = GX + col * (TW + GAP)
    y = GY + row * (TH + GAP)
    d.rectangle([x, y, x + TW, y + TH], outline=GREY, width=2)
    ILL[key](x + 14, y + 12, TW - 28, 84)
    tx = x + 16
    d.text((tx, y + 106), kicker, font=sans_b17, fill=RED)
    hl = wrap(headline, sans_b30, TW - 32)
    hy = y + 126
    for line in hl[:2]:
        d.text((tx, hy), line, font=sans_b30, fill=INK)
        hy += 34
    dl = wrap(deck, sans19, TW - 32)
    dy = y + 194
    for line in dl[:2]:
        d.text((tx, dy), line, font=sans19, fill=DARKGREY)
        dy += 22

# ---------------- footer ----------------
fy = GY + 3 * TH + 2 * GAP + 8
d.rectangle([MX, fy, W - MX, fy + 2], fill=INK)
center(fy + 12, "Somalia expels UAE ambassador  •  Senegal boat capsizes, four dead",
       sans17, INK)
center(fy + 36, "5.6 quake strikes near New Caledonia  •  make.fun · 20 Nov 2026",
       sans17, INK)

img.save("/home/hatch/workspace/makefun/news-image-entry/entry.png")
print("saved")
