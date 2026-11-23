#!/usr/bin/env python3
"""Genera il materiale social del giorno a partire da public/data/news.json.

Uso:
    python3 scripts/social.py                 # sceglie 4 notizie in automatico
    python3 scripts/social.py id1 id2 id3 id4 # notizie scelte dalla redazione

Produce in public/social/:
    AAAA-MM-GG.png   immagine 1080x1920 per le storie (Instagram/Facebook) di @diarioitalianews
    AAAA-MM-GG.txt   testo del post
    AAAA-MM-GG.html  pagina per scaricare l'immagine e copiare il testo dal telefono
    latest.png / latest.txt / latest.html / latest.json  copia dell'ultimo numero
"""
import html
import json
import shutil
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
NEWS = ROOT / "public" / "data" / "news.json"
OUT = ROOT / "public" / "social"
SITE = "https://argentina.diarioitalia.org"

W, H = 1080, 1920  # formato storia; in alto e in basso ~250 px restano liberi per l'interfaccia di Instagram
S = 2  # supersampling
INK, PAPER, MUTED, SOFT = "#15202e", "#f6f7f9", "#5a6575", "#3d4756"
GREEN, RED, GREY = "#0b6b45", "#b3122b", "#d9dde3"
CELESTE = "#2b6ea6"

MESI = ["gennaio", "febbraio", "marzo", "aprile", "maggio", "giugno", "luglio",
        "agosto", "settembre", "ottobre", "novembre", "dicembre"]
MESES = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio",
         "agosto", "septiembre", "octubre", "noviembre", "diciembre"]

HASHTAGS = ("#colectividaditaliana #italianosenargentina #italoargentinos "
            "#italianiinargentina #ciudadaniaitaliana #cittadinanzaitaliana "
            "#comunitaitaliana #argentina #noticias #notizie")

FONT_DIRS = ["/usr/share/fonts/truetype/liberation", "/usr/share/fonts/truetype/liberation2",
             "/usr/share/fonts/liberation", "/usr/share/fonts/truetype/dejavu"]
FONT_FILES = {
    "serif-bold": ["LiberationSerif-Bold.ttf", "DejaVuSerif-Bold.ttf"],
    "sans": ["LiberationSans-Regular.ttf", "DejaVuSans.ttf"],
    "sans-bold": ["LiberationSans-Bold.ttf", "DejaVuSans-Bold.ttf"],
}


def font(kind, size):
    for name in FONT_FILES[kind]:
        for d in FONT_DIRS:
            p = Path(d) / name
            if p.exists():
                return ImageFont.truetype(str(p), size * S)
    for p in Path("/usr/share/fonts").rglob("*.ttf"):
        if p.name in FONT_FILES[kind]:
            return ImageFont.truetype(str(p), size * S)
    return ImageFont.load_default()


def flag(code):
    if code == "AR":
        return "📍"  # niente bandiera argentina: le notizie sono quasi tutte dall'Argentina
    if len(code) != 2 or not code.isalpha():
        return ""
    return "".join(chr(0x1F1E6 + ord(c) - ord("A")) for c in code.upper())


def pick(items, ids):
    if ids:
        by_id = {i["id"]: i for i in items}
        missing = [x for x in ids if x not in by_id]
        if missing:
            sys.exit(f"id non trovati in news.json: {', '.join(missing)}")
        return [by_id[x] for x in ids][:4]
    chosen, countries, topics = [], set(), set()
    for it in items:  # prima passata: paesi e temi diversi
        if it.get("area") not in countries and it["topic"] not in topics:
            chosen.append(it); countries.add(it.get("area")); topics.add(it["topic"])
        if len(chosen) == 4:
            return chosen
    for it in items:  # seconda passata: completa
        if it not in chosen:
            chosen.append(it)
        if len(chosen) == 4:
            break
    return chosen


def wrap(draw, text, fnt, width):
    lines, cur = [], ""
    for word in text.split():
        test = (cur + " " + word).strip()
        if draw.textlength(test, font=fnt) <= width:
            cur = test
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def draw_logo(d, x, y, size):
    k = size / 48
    def r(v):
        return v * k
    lw = max(2, round(3.5 * k))
    d.ellipse([x + r(3.5), y + r(3.5), x + r(44.5), y + r(44.5)], fill="#ffffff", outline=INK, width=lw)
    d.ellipse([x + r(16), y + r(3.5), x + r(32), y + r(44.5)], outline=INK, width=max(2, round(2.4 * k)))
    d.rectangle([x + r(3.5), y + r(20), x + r(17.2), y + r(28)], fill=GREEN)
    d.rectangle([x + r(17.2), y + r(20), x + r(30.8), y + r(28)], fill="#ffffff", outline="#9aa3ae", width=max(1, round(0.8 * k)))
    d.rectangle([x + r(30.8), y + r(20), x + r(44.5), y + r(28)], fill=RED)


LANG_FLAGS = ["it", "es", "gb", "br", "de", "fr"]  # it, es, en, pt, de, fr


def draw_flag(d, code, x, y, w, h):
    """Bandiere semplificate per le 6 lingue."""
    if code == "it":
        for k, c in enumerate([GREEN, "#ffffff", RED]):
            d.rectangle([x + k * w / 3, y, x + (k + 1) * w / 3, y + h], fill=c)
    elif code == "fr":
        for k, c in enumerate(["#0055a4", "#ffffff", "#ef4135"]):
            d.rectangle([x + k * w / 3, y, x + (k + 1) * w / 3, y + h], fill=c)
    elif code == "de":
        for k, c in enumerate(["#000000", "#dd0000", "#ffce00"]):
            d.rectangle([x, y + k * h / 3, x + w, y + (k + 1) * h / 3], fill=c)
    elif code == "es":
        d.rectangle([x, y, x + w, y + h], fill="#aa151b")
        d.rectangle([x, y + h / 4, x + w, y + 3 * h / 4], fill="#f1bf00")
    elif code == "br":
        d.rectangle([x, y, x + w, y + h], fill="#009c3b")
        m = h * 0.12
        d.polygon([(x + w / 2, y + m), (x + w - m * 1.4, y + h / 2), (x + w / 2, y + h - m), (x + m * 1.4, y + h / 2)], fill="#ffdf00")
        rr = h * 0.22
        d.ellipse([x + w / 2 - rr, y + h / 2 - rr, x + w / 2 + rr, y + h / 2 + rr], fill="#002776")
    elif code == "gb":
        d.rectangle([x, y, x + w, y + h], fill="#012169")
        d.line([(x, y), (x + w, y + h)], fill="#ffffff", width=round(h * 0.2))
        d.line([(x + w, y), (x, y + h)], fill="#ffffff", width=round(h * 0.2))
        d.line([(x, y), (x + w, y + h)], fill="#c8102e", width=round(h * 0.07))
        d.line([(x + w, y), (x, y + h)], fill="#c8102e", width=round(h * 0.07))
        d.rectangle([x + w / 2 - h * 0.17, y, x + w / 2 + h * 0.17, y + h], fill="#ffffff")
        d.rectangle([x, y + h / 2 - h * 0.17, x + w, y + h / 2 + h * 0.17], fill="#ffffff")
        d.rectangle([x + w / 2 - h * 0.1, y, x + w / 2 + h * 0.1, y + h], fill="#c8102e")
        d.rectangle([x, y + h / 2 - h * 0.1, x + w, y + h / 2 + h * 0.1], fill="#c8102e")
    d.rectangle([x, y, x + w, y + h], outline="#c3c9d1", width=max(1, S))


def render(picks, date, total, path):
    img = Image.new("RGB", (W * S, H * S), PAPER)
    d = ImageDraw.Draw(img)
    third = W * S // 3
    d.rectangle([0, 0, third, 18 * S], fill=GREEN)
    d.rectangle([third, 0, 2 * third, 18 * S], fill="#ffffff")
    d.rectangle([2 * third, 0, W * S, 18 * S], fill=RED)

    L, R = 80 * S, (W - 80) * S
    y_, m_, g_ = (int(p) for p in date.split("-"))
    fb0 = font("sans-bold", 34)
    draw_logo(d, L, 236 * S, 56 * S)
    d.text((L + 72 * S, 246 * S), "Diario Italia", font=fb0, fill=INK)
    d.text((L + 72 * S + d.textlength("Diario Italia ", font=fb0), 246 * S), "ARGENTINA", font=fb0, fill=CELESTE)
    d.text((L, 340 * S), f"HOY · OGGI — {g_} DE {MESES[m_ - 1].upper()} DE {y_}", font=font("sans-bold", 26), fill=RED)
    d.text((L, 384 * S), "En el número de hoy", font=font("serif-bold", 72), fill=INK)

    y = 506 * S
    card_w = R - L
    pad = 32 * S
    gap = 22 * S
    title_size = 44
    while True:  # riduce il corpo se le schede non entrano
        ft = font("serif-bold", title_size)
        fl = font("sans-bold", 23)
        blocks = []
        for it in picks:
            lines = wrap(d, it["title"]["es"], ft, card_w - 2 * pad - 10 * S)
            hgt = pad + 30 * S + len(lines) * int(title_size * 1.24 * S) + pad - 8 * S
            blocks.append((it, lines, hgt))
        needed = sum(b[2] for b in blocks) + gap * (len(blocks) - 1)
        if y + needed <= 1540 * S or title_size <= 30:
            break
        title_size -= 2

    for n, (it, lines, hgt) in enumerate(blocks):
        d.rounded_rectangle([L, y, R, y + hgt], radius=20 * S, fill="#ffffff")
        d.rectangle([L, y + 2 * S, L + 10 * S, y + hgt - 2 * S], fill=GREEN if n % 2 == 0 else RED)
        tx = L + 10 * S + pad - 6 * S
        d.text((tx, y + pad - 4 * S), it.get("place", it["country"]).upper(), font=fl, fill=MUTED)
        ty = y + pad + 30 * S
        for line in lines:
            d.text((tx, ty), line, font=ft, fill=INK)
            ty += int(title_size * 1.24 * S)
        y += hgt + gap

    rest = total - len(picks)
    if rest > 0:
        d.text((L, y + 6 * S), f"+ {rest} noticias más en español e italiano", font=font("sans", 32), fill=SOFT)

    fy = 1630 * S
    d.rounded_rectangle([L, fy, R, fy + 96 * S], radius=48 * S, fill=INK)
    fs = font("sans-bold", 32)
    txt = "Todas las noticias en argentina.diarioitalia.org"
    d.text(((W * S - d.textlength(txt, font=fs)) // 2, fy + 26 * S), txt, font=fs, fill="#ffffff")

    img.resize((W, H), Image.LANCZOS).save(path, optimize=True)


def caption(picks, date, total):
    y_, m_, g_ = (int(p) for p in date.split("-"))
    out = [f"🗞️ Diario Italia Argentina · {g_} de {MESES[m_ - 1]} de {y_}", ""]
    out += [f"{flag(i['country'])} {i['title']['es']}" for i in picks]
    out += ["", f"🇮🇹 Oggi su Diario Italia Argentina · {g_} {MESI[m_ - 1]}", ""]
    out += [f"{flag(i['country'])} {i['title']['it']}" for i in picks]
    out += ["", f"Las {total} noticias del día en español e italiano · Tutte le notizie in spagnolo e italiano",
            "👉 argentina.diarioitalia.org (link en la bio)", "", HASHTAGS]
    return "\n".join(out)


def page(date, text):
    t = html.escape(text)
    return f"""<!doctype html><html lang="es"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex">
<title>Social · Diario Italia Argentina · {date}</title>
<style>body{{font-family:system-ui,Arial,sans-serif;background:#f6f7f9;color:#15202e;margin:0;padding:20px;max-width:560px;margin:auto}}
img{{width:100%;border-radius:12px;box-shadow:0 2px 10px #0002}}a.b,button{{display:block;width:100%;box-sizing:border-box;text-align:center;
padding:14px;margin:14px 0;border-radius:10px;border:0;background:#15202e;color:#fff;font-size:17px;font-weight:600;text-decoration:none}}
pre{{white-space:pre-wrap;background:#fff;padding:16px;border-radius:10px;border:1px solid #d9dde3;font:15px/1.5 system-ui,Arial,sans-serif}}</style></head>
<body><h2>Historia del {date} · Argentina</h2><img src="{date}.png" alt="Immagine del post">
<a class="b" href="{date}.png" download="DiarioItaliaArgentina_{date}.png">Descargar imagen · Scarica immagine</a>
<button id="c">Copiar texto · Copia testo</button><pre id="t">{t}</pre>
<script>document.getElementById('c').onclick=async function(){{try{{await navigator.clipboard.writeText(document.getElementById('t').textContent);this.textContent='Copiado ✓ · Copiato ✓'}}catch(e){{var r=document.createRange();r.selectNodeContents(document.getElementById('t'));var s=getSelection();s.removeAllRanges();s.addRange(r)}}}}</script>
</body></html>"""


def main():
    data = json.loads(NEWS.read_text(encoding="utf-8"))
    date, items = data["edition"], data["items"]
    picks = pick(items, sys.argv[1:])
    OUT.mkdir(parents=True, exist_ok=True)
    render(picks, date, len(items), OUT / f"{date}.png")
    text = caption(picks, date, len(items))
    (OUT / f"{date}.txt").write_text(text + "\n", encoding="utf-8")
    (OUT / f"{date}.html").write_text(page(date, text), encoding="utf-8")
    shutil.copyfile(OUT / f"{date}.png", OUT / "latest.png")
    shutil.copyfile(OUT / f"{date}.txt", OUT / "latest.txt")
    (OUT / "latest.html").write_text(page(date, text).replace(f'"{date}.png"', '"latest.png"'), encoding="utf-8")
    (OUT / "latest.json").write_text(json.dumps({
        "date": date, "image": f"{SITE}/social/{date}.png", "page": f"{SITE}/social/{date}.html",
        "caption": text, "ids": [p["id"] for p in picks]}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"{SITE}/social/{date}.html")


if __name__ == "__main__":
    main()
