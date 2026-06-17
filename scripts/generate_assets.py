from __future__ import annotations

from pathlib import Path
from textwrap import wrap

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "public" / "assets"
OUT.mkdir(parents=True, exist_ok=True)

W, H = 1400, 788


def font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    candidates = [
        "/System/Library/Fonts/Supplemental/Arial Bold.ttf" if bold else "/System/Library/Fonts/Supplemental/Arial.ttf",
        "/System/Library/Fonts/Supplemental/Helvetica Bold.ttf" if bold else "/System/Library/Fonts/Supplemental/Helvetica.ttf",
        "/Library/Fonts/Arial.ttf",
    ]
    for path in candidates:
        try:
            return ImageFont.truetype(path, size=size)
        except OSError:
            continue
    return ImageFont.load_default()


def rr(draw: ImageDraw.ImageDraw, box, radius: int, fill, outline=None, width=1) -> None:
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)


def txt(draw: ImageDraw.ImageDraw, xy, text, fill, size=28, bold=False, anchor=None) -> None:
    draw.text(xy, text, font=font(size, bold), fill=fill, anchor=anchor)


def wrapped(draw: ImageDraw.ImageDraw, xy, text, fill, size=24, width=34, line_gap=7, bold=False) -> None:
    x, y = xy
    for line in wrap(text, width=width):
        txt(draw, (x, y), line, fill, size=size, bold=bold)
        y += size + line_gap


def arrow(draw: ImageDraw.ImageDraw, start, end, fill, width=5) -> None:
    x1, y1 = start
    x2, y2 = end
    draw.line((x1, y1, x2, y2), fill=fill, width=width)
    if x2 >= x1:
        pts = [(x2, y2), (x2 - 18, y2 - 12), (x2 - 18, y2 + 12)]
    else:
        pts = [(x2, y2), (x2 + 18, y2 - 12), (x2 + 18, y2 + 12)]
    draw.polygon(pts, fill=fill)


def card(draw: ImageDraw.ImageDraw, box, fill="#ffffff", outline="#d9e2e8") -> None:
    rr(draw, box, 24, fill, outline, 2)


def header(draw: ImageDraw.ImageDraw, title: str, subtitle: str, accent: str, ink="#17212b") -> None:
    txt(draw, (82, 68), title, ink, size=54, bold=True)
    txt(draw, (86, 132), subtitle, "#596b78", size=25)
    draw.line((84, 178, 1316, 178), fill=accent, width=5)


def chip(draw: ImageDraw.ImageDraw, box, label: str, fill: str, ink="#ffffff", size=21) -> None:
    rr(draw, box, 12, fill)
    x1, y1, x2, y2 = box
    txt(draw, ((x1 + x2) // 2, (y1 + y2) // 2), label, ink, size=size, bold=True, anchor="mm")


def make_canvas(bg="#f7fafb") -> tuple[Image.Image, ImageDraw.ImageDraw]:
    img = Image.new("RGB", (W, H), bg)
    d = ImageDraw.Draw(img)
    for x in range(-200, W, 80):
        d.line((x, 0, x + 300, H), fill="#eef3f5", width=2)
    return img, d


def malguard() -> None:
    img, d = make_canvas("#f5f8fa")
    header(d, "MalGuard-X", "Adversarial malware classification research workflow", "#1e6d7b")

    card(d, (70, 220, 420, 640), "#10202a", "#244b5a")
    txt(d, (104, 252), "Malware image", "#d9f2f4", 28, bold=True)
    palette = ["#49a6a3", "#d9a846", "#c7656f", "#6e91c7", "#e7edf1"]
    x0, y0, cell = 104, 315, 33
    for y in range(7):
        for x in range(8):
            d.rectangle(
                (x0 + x * cell, y0 + y * cell, x0 + x * cell + 24, y0 + y * cell + 24),
                fill=palette[(x * 2 + y) % len(palette)],
            )
    chip(d, (104, 575, 386, 618), "Image-based classifier", "#1e6d7b")

    card(d, (510, 236, 890, 624), "#ffffff", "#cad8de")
    txt(d, (552, 272), "FB-MalAT", "#16212b", 42, bold=True)
    wrapped(
        d,
        (554, 328),
        "Family-balanced adversarial training layered onto malware classification.",
        "#53636e",
        size=24,
        width=30,
    )
    for i, label in enumerate(["Balanced sampling", "Balanced Softmax", "Adversarial batches", "Robust checkpoint"]):
        y = 450 + i * 38
        rr(d, (552, y, 846, y + 28), 8, "#edf5f6", "#c2dadd", 1)
        txt(d, (572, y + 5), label, "#225c66", 19, bold=True)

    card(d, (980, 220, 1330, 640), "#ffffff", "#cad8de")
    txt(d, (1020, 252), "Evaluation", "#16212b", 34, bold=True)
    for i, label in enumerate(["FGSM", "PGD-20", "PGD-50"]):
        chip(d, (1022, 322 + i * 64, 1225, 366 + i * 64), label, "#244f7e")
    chip(d, (1022, 536, 1288, 584), "Grad-CAM analysis", "#7a5a18")
    arrow(d, (420, 430), (510, 430), "#1e6d7b")
    arrow(d, (890, 430), (980, 430), "#1e6d7b")

    img.save(OUT / "malguard-x.png", quality=96)


def space() -> None:
    img, d = make_canvas("#f8fbfa")
    header(d, "Project SPACE", "Computer vision for accessible-parking enforcement", "#217485")

    card(d, (70, 225, 1330, 620), "#ffffff", "#cbdbe0")
    steps = [
        ("Video frame", "Webcam / CCTV / upload"),
        ("Vehicle YOLO", "confirm car"),
        ("Label model", "Class 1 / Class 2"),
        ("Plate capture", "save misuse evidence"),
    ]
    x_positions = [118, 420, 720, 1010]
    for i, ((title, sub), x) in enumerate(zip(steps, x_positions)):
        rr(d, (x, 292, x + 225, 470), 22, "#f5f9fa", "#bdd0d7", 2)
        txt(d, (x + 26, 322), title, "#17212b", 29, bold=True)
        wrapped(d, (x + 26, 366), sub, "#5d6f79", size=21, width=17)
        if i < len(steps) - 1:
            arrow(d, (x + 235, 380), (x_positions[i + 1] - 18, 380), "#217485")

    # Camera frame and vehicle.
    rr(d, (112, 506, 400, 575), 18, "#17363d")
    rr(d, (150, 528, 280, 558), 12, "#62b8b3")
    d.ellipse((172, 552, 204, 584), fill="#10181d")
    d.ellipse((250, 552, 282, 584), fill="#10181d")

    # Dataset and training facts from report.
    chip(d, (450, 522, 675, 566), "Roboflow dataset", "#217485", size=19)
    chip(d, (695, 522, 1008, 566), "510 augmented annotations", "#2f6f52", size=18)
    chip(d, (1028, 522, 1288, 566), "3-model YOLO flow", "#244f7e", size=19)

    img.save(OUT / "project-space.png", quality=96)


def seating() -> None:
    img, d = make_canvas("#fbfaf6")
    header(d, "Project SeatingPlan", "Teacher workflow for creating and editing classroom layouts", "#2f7364")

    # Browser shell.
    card(d, (70, 220, 1330, 642), "#ffffff", "#d9dedc")
    rr(d, (70, 220, 1330, 278), 24, "#edf3f1", "#d9dedc", 2)
    for i, c in enumerate(["#d66a5f", "#d5a445", "#58a177"]):
        d.ellipse((106 + i * 36, 242, 126 + i * 36, 262), fill=c)
    txt(d, (232, 239), "Seating Plan Generator", "#31434a", 25, bold=True)

    # Left dashboard.
    rr(d, (112, 318, 430, 588), 18, "#f7faf9", "#cfdcda", 2)
    txt(d, (140, 348), "Teacher dashboard", "#233239", 27, bold=True)
    for i, label in enumerate(["Import class list", "Choose template", "Recent designs"]):
        rr(d, (140, 404 + i * 54, 398, 440 + i * 54), 9, "#ffffff", "#d7e2e0", 2)
        txt(d, (160, 413 + i * 54), label, "#43545b", 20, bold=True)

    # Seating grid with drag affordance.
    rr(d, (510, 315, 935, 590), 18, "#fbfdfd", "#cfdcda", 2)
    txt(d, (540, 346), "Drag-and-drop layout", "#233239", 27, bold=True)
    for row in range(4):
        for col in range(5):
            x = 560 + col * 68
            y = 405 + row * 42
            rr(d, (x, y, x + 48, y + 28), 7, "#e6f3ef", "#65a89a", 2)
            txt(d, (x + 24, y + 14), f"S{row+1}{col+1}", "#2f7364", 13, bold=True, anchor="mm")
    arrow(d, (700, 555), (780, 508), "#2f7364", width=4)

    # Firebase sync panel.
    rr(d, (1010, 335, 1255, 568), 18, "#153b39", "#2f7364", 2)
    txt(d, (1040, 374), "Firebase", "#dff7ef", 32, bold=True)
    wrapped(d, (1042, 426), "Auth, storage, realtime retrieval, and saved seating plans.", "#b8dcd3", size=22, width=19)
    chip(d, (1038, 520, 1222, 558), "Teacher-tested", "#d9a846", "#17212b")

    img.save(OUT / "seatingplan.png", quality=96)


def pawnify() -> None:
    img, d = make_canvas("#f6f8f8")
    header(d, "Pawnify Engine", "Browser chess GUI for advanced engine customization", "#7d6120")

    card(d, (70, 220, 1330, 642), "#101719", "#334449")
    # Chess board.
    board_x, board_y, sq = 112, 300, 44
    for r in range(8):
        for c in range(8):
            fill = "#eadfbe" if (r + c) % 2 == 0 else "#617b73"
            d.rectangle((board_x + c * sq, board_y + r * sq, board_x + (c + 1) * sq, board_y + (r + 1) * sq), fill=fill)
    txt(d, (112, 266), "Play screen", "#f3f6f5", 29, bold=True)
    chip(d, (112, 670 - 92, 326, 670 - 50), "Chess.js validation", "#2d7368")

    # Prep configuration panel.
    rr(d, (545, 282, 876, 570), 20, "#182528", "#485d62", 2)
    txt(d, (576, 318), "Prep controls", "#ffffff", 30, bold=True)
    controls = [("ELO", 76), ("Time", 52), ("Nodes", 64), ("Takebacks", 86), ("FEN", 70)]
    for i, (label, pos) in enumerate(controls):
        y = 372 + i * 34
        txt(d, (576, y), label, "#b7c7ca", 18, bold=True)
        rr(d, (690, y + 4, 835, y + 14), 5, "#2d3e42")
        rr(d, (690, y + 4, 690 + pos, y + 14), 5, "#d4a047")

    # Engine communication.
    rr(d, (955, 282, 1262, 570), 20, "#182528", "#485d62", 2)
    txt(d, (990, 318), "Stockfish.js", "#ffffff", 30, bold=True)
    for i, label in enumerate(["postMessage()", "bestmove", "evaluation", "engine lines"]):
        rr(d, (990, 374 + i * 40, 1224, 402 + i * 40), 8, "#233236", "#3b555b", 1)
        txt(d, (1012, 379 + i * 40), label, "#9fe1d4", 19, bold=True)
    arrow(d, (466, 470), (545, 470), "#d4a047")
    arrow(d, (876, 425), (955, 425), "#d4a047")

    img.save(OUT / "pawnify.png", quality=96)


def main() -> None:
    malguard()
    space()
    seating()
    pawnify()


if __name__ == "__main__":
    main()
