from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "public" / "assets"
OUT.mkdir(parents=True, exist_ok=True)


def font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    candidates = [
        "/System/Library/Fonts/Supplemental/Arial Bold.ttf" if bold else "/System/Library/Fonts/Supplemental/Arial.ttf",
        "/System/Library/Fonts/SFNS.ttf",
        "/Library/Fonts/Arial.ttf",
    ]
    for path in candidates:
        try:
            return ImageFont.truetype(path, size=size)
        except OSError:
            continue
    return ImageFont.load_default()


def rounded_rect(draw: ImageDraw.ImageDraw, box, radius: int, fill, outline=None, width=1) -> None:
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)


def label(draw, xy, text, fill=(255, 255, 255), size=34, bold=False):
    draw.text(xy, text, font=font(size, bold), fill=fill)


def malguard() -> None:
    img = Image.new("RGB", (1400, 788), "#0f1820")
    d = ImageDraw.Draw(img)
    for i in range(0, 1400, 70):
        d.line((i, 0, i - 260, 788), fill="#183444", width=2)
    rounded_rect(d, (70, 72, 1330, 716), 32, "#13242d", "#2f5262", 3)
    label(d, (112, 114), "MalGuard-X", size=52, bold=True)
    label(d, (116, 178), "Family-balanced adversarial malware classification", "#a6c9d3", 25)
    colors = ["#57b7b2", "#dca84a", "#b95f6a", "#7aa2d8"]
    x0, y0, cell = 132, 285, 48
    for y in range(6):
        for x in range(10):
            shade = colors[(x + y) % len(colors)]
            d.rectangle((x0 + x * cell, y0 + y * cell, x0 + x * cell + 35, y0 + y * cell + 35), fill=shade)
    d.line((710, 260, 710, 610), fill="#33596b", width=3)
    for idx, txt in enumerate(["Balanced Softmax", "FGSM / PGD evaluation", "Grad-CAM explainability"]):
        y = 304 + idx * 92
        rounded_rect(d, (780, y, 1190, y + 54), 14, "#203844", "#4f7b8a", 2)
        label(d, (806, y + 13), txt, "#e8f7f7", 24, bold=True)
    img.save(OUT / "malguard-x.png", quality=95)


def space() -> None:
    img = Image.new("RGB", (1400, 788), "#f1f5f4")
    d = ImageDraw.Draw(img)
    d.rectangle((0, 505, 1400, 788), fill="#333b40")
    d.polygon([(0, 505), (1400, 505), (1170, 430), (220, 430)], fill="#58656d")
    d.line((700, 510, 700, 788), fill="#f7ce59", width=12)
    rounded_rect(d, (120, 146, 1280, 646), 28, "#ffffff", "#c8d6db", 3)
    label(d, (160, 188), "Project SPACE", "#12343d", 50, bold=True)
    label(d, (164, 250), "YOLOv8 monitoring for accessible parking misuse", "#47616b", 25)
    rounded_rect(d, (190, 395, 578, 542), 30, "#1b5969")
    d.ellipse((250, 510, 318, 578), fill="#11181d")
    d.ellipse((448, 510, 516, 578), fill="#11181d")
    rounded_rect(d, (760, 336, 1040, 512), 18, "#e8f3f5", "#31778a", 4)
    d.rectangle((785, 374, 1015, 480), outline="#31778a", width=5)
    label(d, (818, 404), "LABEL", "#31778a", 34, bold=True)
    rounded_rect(d, (1080, 452, 1225, 504), 8, "#f9fbfb", "#6b7d86", 3)
    label(d, (1097, 464), "Plate", "#25343b", 24, bold=True)
    img.save(OUT / "project-space.png", quality=95)


def seating() -> None:
    img = Image.new("RGB", (1400, 788), "#fffdf8")
    d = ImageDraw.Draw(img)
    rounded_rect(d, (88, 76, 1312, 712), 30, "#ffffff", "#d9d2c4", 3)
    label(d, (130, 120), "Project SeatingPlan", "#1c2930", 50, bold=True)
    label(d, (134, 184), "Teacher workflow: create, drag, store, edit", "#667174", 25)
    rounded_rect(d, (150, 265, 510, 594), 18, "#f5f8fa", "#cbd7df", 2)
    for i, name in enumerate(["Import class", "Blank plan", "Templates", "Recent designs"]):
        y = 300 + i * 62
        rounded_rect(d, (188, y, 468, y + 42), 9, "#ffffff", "#d7e0e7", 2)
        label(d, (210, y + 9), name, "#30434d", 22, bold=True)
    x0, y0 = 650, 268
    for row in range(4):
        for col in range(5):
            x = x0 + col * 105
            y = y0 + row * 70
            rounded_rect(d, (x, y, x + 78, y + 44), 9, "#eaf4f2", "#509082", 2)
            label(d, (x + 18, y + 10), f"S{row}{col}", "#2d5f55", 18, bold=True)
    rounded_rect(d, (736, 600, 1145, 650), 12, "#1f685c")
    label(d, (765, 612), "Firebase-backed storage", "#ffffff", 24, bold=True)
    img.save(OUT / "seatingplan.png", quality=95)


def pawnify() -> None:
    img = Image.new("RGB", (1400, 788), "#111719")
    d = ImageDraw.Draw(img)
    rounded_rect(d, (76, 66, 1324, 722), 30, "#182123", "#3b4f52", 3)
    label(d, (120, 112), "Pawnify Engine", "#ffffff", 52, bold=True)
    label(d, (124, 176), "Customizable browser chess engine interface", "#b9c7c9", 25)
    board_x, board_y, sq = 135, 270, 58
    for r in range(8):
        for c in range(8):
            fill = "#e1d4b2" if (r + c) % 2 == 0 else "#59736c"
            d.rectangle((board_x + c * sq, board_y + r * sq, board_x + (c + 1) * sq, board_y + (r + 1) * sq), fill=fill)
    for text, x, y in [("FEN", 770, 284), ("PGN", 770, 360), ("EVAL", 770, 436), ("LINES", 770, 512)]:
        rounded_rect(d, (740, y, 1190, y + 48), 10, "#232f32", "#53676b", 2)
        label(d, (765, y + 11), text, "#8fe3d1", 22, bold=True)
        d.line((855, y + 24, 1160, y + 24), fill="#53676b", width=3)
    rounded_rect(d, (1040, 620, 1202, 670), 12, "#b9832f")
    label(d, (1064, 632), "Stockfish.js", "#111719", 23, bold=True)
    img.save(OUT / "pawnify.png", quality=95)


def main() -> None:
    malguard()
    space()
    seating()
    pawnify()


if __name__ == "__main__":
    main()
