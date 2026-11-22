#!/usr/bin/env python3
"""Draw the 22 November 2026 world-news front page (1024x1024 PNG).

Deterministic: same input -> same bytes. No network, stdlib + Pillow only.
Run: python3 draw.py  (writes entry.png next to this file)
"""
import textwrap
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (247, 243, 234)
INK = (26, 26, 26)
NAVY = (20, 36, 62)
GOLD = (201, 162, 39)
RED = (179, 38, 30)
TEAL = (15, 118, 110)
GREY = (90, 90, 90)
WHITE = (255, 255, 255)
PANEL = (255, 255, 255)

FONT_DIR = "/usr/share/fonts/truetype/dejavu/"
SERIF_B = FONT_DIR + "DejaVuSerif-Bold.ttf"
SANS_B = FONT_DIR + "DejaVuSans-Bold.ttf"
SANS = FONT_DIR + "DejaVuSans.ttf"

img = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(img)


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    """Greedy word wrap returning list of lines fitting max_w pixels."""
    lines, cur = [], ""
    for word in text.split(" "):
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def draw_text_block(x, y, text, fnt, color, max_w, leading):
    lines = wrap(d, text, fnt, max_w)
    for ln in lines:
        d.text((x, y), ln, font=fnt, fill=color)
        y += leading
    return y


# ---------------------------------------------------------------- masthead
d.rectangle([0, 0, W, 138], fill=NAVY)
d.rectangle([0, 138, W, 144], fill=GOLD)
d.text((512, 18), "THE WORLD TODAY", font=font(SERIF_B, 58),
       fill=WHITE, anchor="ma")
d.text((512, 92), "SUNDAY  •  22 NOVEMBER 2026", font=font(SANS_B, 26),
       fill=GOLD, anchor="ma")

# ---------------------------------------------------------------- lead: COP31
LX, LY, LW, LH = 24, 164, 976, 252
d.rectangle([LX, LY, LX + LW, LY + LH], fill=PANEL, outline=NAVY, width=3)
d.rectangle([LX, LY, LX + LW, LY + 44], fill=RED)
d.text((LX + 18, LY + 8), "LEAD STORY  —  CLIMATE", font=font(SANS_B, 24),
       fill=WHITE)

# globe icon with a crack, left side of the lead panel
cx, cy, r = LX + 108, LY + 138, 72
d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(214, 235, 245),
          outline=NAVY, width=5)
d.ellipse([cx - 28, cy - r + 6, cx + 28, cy + r - 6], outline=NAVY, width=3)
d.line([cx - r + 4, cy, cx + r - 4, cy], fill=NAVY, width=3)
d.arc([cx - r + 14, cy - r + 26, cx + r - 14, cy + r - 26],
      start=200, end=340, fill=NAVY, width=3)
# crack: red zigzag across the globe
d.line([(cx - 46, cy - 52), (cx - 12, cy - 18), (cx - 30, cy + 8),
        (cx + 6, cy + 34), (cx - 8, cy + 62)], fill=RED, width=6,
       joint="curve")
d.text((cx, cy + r + 8), "ANTALYA, TURKEY", font=font(SANS_B, 17),
       fill=GREY, anchor="ma")

tx = LX + 220
d.text((tx, LY + 58), "CLIMATE TALKS COLLAPSE", font=font(SANS_B, 40),
       fill=INK)
draw_text_block(tx, LY + 112,
                "COP31 ends with no deal at all after the EU rejects a "
                "final text with no mention of fossil fuels.",
                font(SANS, 25), INK, LW - 240, 34)
d.text((tx, LY + 206), "No agreement. No fossil-fuel phase-out.",
       font=font(SANS_B, 22), fill=RED)

# ---------------------------------------------------------------- 2x2 grid
def panel(x, y, w, h, tag, tag_color, headline, body, icon):
    d.rectangle([x, y, x + w, y + h], fill=PANEL, outline=NAVY, width=2)
    d.rectangle([x, y, x + w, y + 34], fill=tag_color)
    d.text((x + 12, y + 5), tag, font=font(SANS_B, 19), fill=WHITE)
    icon(x + 14, y + 48)
    tx = x + 118
    tw = w - 132
    yy = draw_text_block(tx, y + 46, headline, font(SANS_B, 27), INK, tw, 32)
    draw_text_block(tx, yy + 4, body, font(SANS, 20), (60, 60, 60), tw, 26)


def icon_missile(x, y):
    # diagonal rocket with flame
    d.polygon([(x + 8, y + 58), (x + 34, y + 6), (x + 52, y + 34),
               (x + 30, y + 66)], fill=NAVY)
    d.polygon([(x + 34, y + 6), (x + 44, y + 2), (x + 48, y + 14)],
              fill=RED)
    d.polygon([(x + 8, y + 58), (x + 2, y + 74), (x + 18, y + 72)],
              fill=(245, 158, 11))
    d.polygon([(x + 52, y + 34), (x + 66, y + 40), (x + 56, y + 52)],
              fill=RED)


def icon_badge(x, y):
    # sheriff-style star badge
    cx, cy, r1, r2 = x + 32, y + 34, 34, 15
    pts = []
    import math
    for i in range(10):
        ang = math.pi / 2 + i * math.pi / 5
        rr = r1 if i % 2 == 0 else r2
        pts.append((cx + rr * math.cos(ang), cy - rr * math.sin(ang)))
    d.polygon(pts, fill=GOLD, outline=NAVY)
    d.ellipse([cx - 11, cy - 11, cx + 11, cy + 11], fill=NAVY)
    d.text((cx, cy - 9), "$", font=font(SANS_B, 20), fill=WHITE, anchor="ma")


def icon_building(x, y):
    # apartment block, broken top, smoke
    d.rectangle([x + 6, y + 26, x + 58, y + 70], fill=NAVY)
    d.polygon([(x + 6, y + 26), (x + 18, y + 12), (x + 30, y + 24),
               (x + 44, y + 10), (x + 58, y + 26)], fill=NAVY)
    for wy in (36, 50):
        for wx in (14, 30, 46):
            d.rectangle([x + wx, y + wy, x + wx + 8, y + wy + 8],
                        fill=GOLD)
    for sx, sy, sr in ((x + 22, y + 2, 7), (x + 40, y - 4, 9),
                       (x + 52, y + 6, 6)):
        d.ellipse([sx - sr, sy - sr, sx + sr, sy + sr], fill=(150, 150, 150))


def icon_scales(x, y):
    # scales of justice
    cx = x + 32
    d.line([(cx, y + 6), (cx, y + 64)], fill=NAVY, width=4)
    d.line([(cx - 28, y + 14), (cx + 28, y + 14)], fill=NAVY, width=4)
    d.polygon([(cx - 40, y + 40), (cx - 16, y + 40), (cx - 28, y + 16)],
              outline=NAVY, width=3)
    d.polygon([(cx + 16, y + 40), (cx + 40, y + 40), (cx + 28, y + 16)],
              outline=NAVY, width=3)
    d.line([(cx - 28, y + 16), (cx - 28, y + 40)], fill=NAVY, width=2)
    d.line([(cx + 28, y + 16), (cx + 28, y + 40)], fill=NAVY, width=2)
    d.rectangle([cx - 24, y + 64, cx + 24, y + 70], fill=NAVY)


GX, GY = 24, 436
GW, GH, GAP = 483, 212, 10
panel(GX, GY, GW, GH, "MIDDLE EAST", RED,
      "IRAN STRIKES BAHRAIN",
      "Missiles hit a civilian site in Sitra; two people hurt. "
      "Tankers struck near the Strait of Hormuz.",
      icon_missile)
panel(GX + GW + GAP, GY, GW, GH, "MEXICO", TEAL,
      "CARTEL BOSS CAPTURED",
      "\u2018El Chapo Isidro\u2019 seized in a Sinaloa raid; 11 killed, "
      "four of them soldiers.",
      icon_badge)
panel(GX, GY + GH + GAP, GW, GH, "UKRAINE", NAVY,
      "KYIV APARTMENT HIT",
      "A Russian drone collapses a block near Kyiv; at least "
      "14 people missing.",
      icon_building)
panel(GX + GW + GAP, GY + GH + GAP, GW, GH, "JUSTICE", (107, 33, 98),
      "WORLD COURT: GENOCIDE",
      "Myanmar found responsible for the Rohingya genocide \u2014 "
      "a first for the court.",
      icon_scales)

# ---------------------------------------------------------------- bottom strip
BY = 890
d.rectangle([24, BY, 1000, BY + 96], fill=NAVY)
d.text((512, BY + 10), "ALSO ON THIS DAY", font=font(SANS_B, 20),
       fill=GOLD, anchor="ma")
d.text((512, BY + 38),
       "BepiColombo reaches Mercury orbit after an 8-year journey",
       font=font(SANS, 20), fill=WHITE, anchor="ma")
d.text((512, BY + 64), "US stocks slide into correction",
       font=font(SANS, 20), fill=WHITE, anchor="ma")
d.text((512, 996), "Six stories that defined Sunday, 22 November 2026",
       font=font(SANS, 16), fill=GREY, anchor="ma")

img.save("entry.png", optimize=True)
print("saved entry.png", img.size)
