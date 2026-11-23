#!/usr/bin/env python3
"""Genera le pagine statiche (chi-siamo, fonti, segnala, privacy) in public/.

Testi in scripts/pages_content.py; l'elenco della pagina Fonti viene da fonti.json.
Rieseguire dopo ogni modifica dei testi o di fonti.json:
    python3 scripts/build_pages.py
"""
import html
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

import markdown

sys.path.insert(0, str(Path(__file__).resolve().parent))
from pages_content import FONTI_UI, NAV, PAGES  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
PUBLIC = ROOT / "public"
LANGS = [("es", "Español"), ("it", "Italiano")]
TAGLINE = {
    "es": "Las noticias de la colectividad italiana en Argentina, cada día",
    "it": "Le notizie della collettività italiana in Argentina, ogni giorno",
}
REGION_LABEL = {
    "es": {"nacional": "Todo el país", "amba": "Buenos Aires y AMBA", "bonaerense": "Provincia de Buenos Aires", "centro": "Centro (Córdoba, Santa Fe)",
           "noa": "Noroeste", "nea": "Noreste y Litoral", "cuyo": "Cuyo", "patagonia": "Patagonia"},
    "it": {"nacional": "Tutto il paese", "amba": "Buenos Aires e AMBA", "bonaerense": "Provincia di Buenos Aires", "centro": "Centro (Córdoba, Santa Fe)",
           "noa": "Nord-ovest", "nea": "Nord-est e Litorale", "cuyo": "Cuyo", "patagonia": "Patagonia"},
}
REGION_ORDER = ["nacional", "amba", "bonaerense", "centro", "noa", "nea", "cuyo", "patagonia"]
SITE = "https://argentina.diarioitalia.org"
PAGE_ORDER = ["chi-siamo", "fonti", "segnala"]  # nel menu in alto; privacy solo nel piè di pagina
LOGO = ('<svg class="logo" viewBox="0 0 48 48" aria-hidden="true"><circle cx="24" cy="24" r="20.5" fill="none" stroke="currentColor" stroke-width="3.5"/>'
        '<ellipse cx="24" cy="24" rx="8" ry="20.5" fill="none" stroke="currentColor" stroke-width="2.4"/>'
        '<rect x="3.5" y="20" width="13.7" height="8" fill="#0b6b45"/><rect x="17.2" y="20" width="13.6" height="8" fill="#fff" stroke="#9aa3ae" stroke-width="0.8"/>'
        '<rect x="30.8" y="20" width="13.7" height="8" fill="#b3122b"/></svg>')

PAGE_CSS = """
.pagenav a[data-nav="home"] { display: inline; }
.page { max-width: 760px; padding-block: 32px 56px; }
.page h1 { font-family: var(--font-display); font-weight: 700; font-size: clamp(2rem, 4vw, 2.6rem); line-height: 1.1; margin: 0 0 18px; }
.page h2 { font-family: var(--font-display); font-weight: 700; font-size: 1.45rem; margin: 34px 0 10px; }
.page p, .page li { font-size: 1.05rem; line-height: 1.6; }
.page p:first-of-type strong { font-family: var(--font-display); font-weight: 600; font-size: 1.25rem; line-height: 1.4; display: block; }
.page ul, .page ol { padding-left: 1.3em; }
.page li { margin: 6px 0; }
.page a { color: var(--accent); }
[data-lang] { display: none; }
[data-lang].on { display: block; }
.src-region { margin-top: 30px; }
.src-region h2 { display: flex; align-items: baseline; justify-content: space-between; gap: 12px; border-bottom: 2px solid var(--ink); padding-bottom: 6px; }
.src-region h2 small { font: 500 0.85rem/1 var(--font-body); color: var(--muted); }
.page .src-country { margin: 14px 0 4px; font: 700 0.78rem/1 var(--font-body); letter-spacing: 0.08em; text-transform: uppercase; color: var(--muted); }
.src-list { list-style: none; padding: 0 !important; margin: 0; }
.src-list li { display: flex; align-items: baseline; gap: 10px; border-bottom: 1px solid var(--rule); padding: 7px 0; margin: 0; font-size: 0.98rem; }
.src-list li a { color: var(--ink); text-decoration: none; font-weight: 500; }
.src-list li a:hover { color: var(--accent); text-decoration: underline; }
.src-list .kind { margin-left: auto; flex: none; }
.src-list { }
.src-list li { flex-wrap: wrap; }
.src-city { color: var(--muted); font-size: 0.88rem; }
.page .src-list a.soc { font-size: 0.8rem; font-weight: 600; color: var(--accent); }
.ar { display: block; font: 700 clamp(0.95rem, 2vw, 1.2rem)/1 var(--font-body); letter-spacing: 0.32em; text-transform: uppercase; color: var(--celeste); margin-top: 6px; }
"""


def index_css():
    s = (PUBLIC / "index.html").read_text(encoding="utf-8")
    m = re.search(r"<style>(.*?)</style>", s, re.S)
    return m.group(1)


def md(text):
    return markdown.markdown(text, extensions=["sane_lists"])


def fonti_html(lang):
    fonti = json.loads((ROOT / "fonti.json").read_text(encoding="utf-8"))
    ui = FONTI_UI[lang]
    reg = defaultdict(list)
    for f in fonti:
        reg[f.get("area") or "nacional"].append(f)
    kind_cls = {"1": "comunita", "2": "istituzionale", "3": "agenzia"}
    out = []
    for r in REGION_ORDER:
        if r not in reg:
            continue
        out.append(f'<section class="src-region"><h2>{html.escape(REGION_LABEL[lang][r])} <small>{ui["count"].format(n=len(reg[r]))}</small></h2><ul class="src-list">')
        for f in sorted(reg[r], key=lambda x: (x["gruppo"], (x.get("citta") or ""), x["testata"].lower())):
            g = f["gruppo"][0]
            name = html.escape(f["testata"])
            main = f.get("sito") or f.get("facebook") or f.get("instagram") or ""
            link = f'<a href="{html.escape(main)}" target="_blank" rel="noopener">{name}</a>' if main.startswith("http") else name
            city = f'<span class="src-city">{html.escape(f.get("citta") or "")}</span>'
            social = "".join(f'<a class="soc" href="{html.escape(f[k])}" target="_blank" rel="noopener">{ui[lab]}</a>'
                             for k, lab in (("facebook", "fb"), ("instagram", "ig")) if f.get(k) and f.get(k) != main)
            out.append(f'<li>{link}{city}{social}<span class="kind kind-{kind_cls[g]}">{ui["kinds"][g]}</span></li>')
        out.append("</ul></section>")
    return "\n".join(out)


def title_of(text):
    return re.match(r"#\s+(.+)", text.strip()).group(1)


def build(slug):
    css = index_css() + PAGE_CSS
    texts = PAGES[slug]
    sections = []
    for code, _ in LANGS:
        body = md(texts[code])
        if slug == "fonti":
            body += fonti_html(code)
        sections.append(f'<article data-lang="{code}" lang="{code}"{" class=\"on\"" if code == "es" else ""}>\n{body}\n</article>')
    titles = {c: title_of(PAGES[slug][c]) for c, _ in LANGS}
    first = re.sub(r"<[^>]+>", "", md(texts["es"]).split("</p>")[0].split("<p>")[-1])
    data = json.dumps({"nav": NAV, "tagline": TAGLINE, "titles": titles, "slug": slug}, ensure_ascii=False)
    nav_links = "".join(f'<a href="/{p}" data-nav="{p}"{" aria-current=\"page\"" if p == slug else ""}>{NAV["es"][p]}</a>' for p in PAGE_ORDER)
    page = f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(titles["es"])} · Diario Italia Argentina</title>
<meta name="description" content="{html.escape(first)}">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="icon" href="/favicon-32.png" sizes="32x32" type="image/png">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="canonical" href="https://argentina.diarioitalia.org/{slug}">
<meta name="theme-color" content="#15202e">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Diario Italia Argentina">
<meta property="og:title" content="{html.escape(titles["es"])} · Diario Italia Argentina">
<meta property="og:description" content="{html.escape(first)}">
<meta property="og:url" content="https://argentina.diarioitalia.org/{slug}">
<meta property="og:image" content="https://argentina.diarioitalia.org/og.png">
<script>try{{var t=localStorage.getItem("diario-theme");if(t==="dark"||t==="light")document.documentElement.setAttribute("data-theme",t);}}catch(e){{}}</script>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Newsreader:opsz,wght@6..72,400;6..72,600;6..72,700&family=Public+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>{css}</style>
</head>
<body>
<!-- Pagina generata da scripts/build_pages.py: non modificare a mano. -->
<div class="tricolore" aria-hidden="true"><span></span><span></span><span></span></div>
<header class="mast">
  <div class="wrap">
    <div class="mast-inner">
      <a class="brand" href="/" style="text-decoration:none">
        {LOGO}
        <div>
          <span class="wordmark"><span class="h1">Diario Italia<span class="ar">Argentina</span></span><span class="rule3" aria-hidden="true"><span></span><span></span><span></span></span></span>
          <p id="tagline">{TAGLINE["es"]}</p>
        </div>
      </a>
    </div>
    <div class="langrow"><div class="langbar" role="group" aria-label="Idioma / Lingua" id="langbar"></div>
      <nav class="pagenav" id="pagenav" aria-label="Diario Italia Argentina"><a href="/" data-nav="home">{NAV["es"]["home"]}</a>{nav_links}</nav></div>
  </div>
</header>
<main class="wrap page">
{chr(10).join(sections)}
</main>
<footer>
  <div class="wrap foot">
    <div><p class="footnav" id="footnav"></p></div>
    <div><p><a href="mailto:info@diarioitalia.org">info@diarioitalia.org</a></p></div>
  </div>
</footer>
<script>
const D = {data};
const LANGS = {json.dumps(LANGS, ensure_ascii=False)};
function pick() {{
  const h = (location.hash || "").replace("#", "");
  if (D.nav[h]) return h;
  try {{ const s = localStorage.getItem("diario-ar-lang"); if (D.nav[s]) return s; }} catch (e) {{}}
  return "es";
}}
function render(lang) {{
  document.documentElement.lang = lang;
  document.title = D.titles[lang] + " · Diario Italia Argentina";
  document.getElementById("tagline").textContent = D.tagline[lang];
  document.querySelectorAll("[data-lang]").forEach(a => a.classList.toggle("on", a.dataset.lang === lang));
  document.querySelectorAll("#pagenav [data-nav]").forEach(a => {{
    a.textContent = D.nav[lang][a.dataset.nav];
    a.href = (a.dataset.nav === "home" ? "/" : "/" + a.dataset.nav) + "#" + lang;
  }});
  const fn = document.getElementById("footnav"); fn.textContent = "";
  ["home", "chi-siamo", "fonti", "segnala", "privacy"].forEach((p, i) => {{
    if (i) fn.append(" · ");
    const a = document.createElement("a"); a.href = (p === "home" ? "/" : "/" + p) + "#" + lang; a.textContent = D.nav[lang][p]; fn.append(a);
  }});
  const bar = document.getElementById("langbar"); bar.textContent = "";
  LANGS.forEach(([code, name]) => {{
    const b = document.createElement("button");
    b.type = "button"; b.textContent = code.toUpperCase(); b.title = name;
    b.setAttribute("aria-pressed", String(code === lang));
    b.onclick = () => {{ try {{ localStorage.setItem("diario-ar-lang", code); }} catch (e) {{}} history.replaceState(null, "", "#" + code); render(code); }};
    bar.append(b);
  }});
  document.querySelector(".brand").href = "/#" + lang;
}}
render(pick());
window.addEventListener("hashchange", () => render(pick()));
</script>
</body>
</html>
"""
    (PUBLIC / f"{slug}.html").write_text(page, encoding="utf-8")
    return PUBLIC / f"{slug}.html"


if __name__ == "__main__":
    for slug in PAGES:
        print(build(slug))
