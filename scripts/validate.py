#!/usr/bin/env python3
"""Controlla il numero del giorno prima della pubblicazione.

Uso: python3 scripts/validate.py public/data/news.json
Esce con codice 1 e un elenco di errori se qualcosa non va.
"""
import json
import re
import sys

LANGS = ["es", "it"]
AREAS = {"nacional", "amba", "bonaerense", "centro", "noa", "nea", "cuyo", "patagonia", "italia"}
TOPICS = {"societa", "politica", "cittadinanza", "comunita", "cultura", "economia", "sport", "italia"}
DATE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
COUNTRY = re.compile(r"^[A-Z]{2}$")
KINDS = {"comunita", "istituzionale", "agenzia"}


def main(path):
    errors = []
    data = json.load(open(path, encoding="utf-8"))
    for key in ("edition", "updated", "sources_monitored", "items"):
        if key not in data:
            errors.append(f"manca il campo '{key}'")
    if errors:
        return errors
    if not DATE.match(data["edition"]):
        errors.append("edition deve essere AAAA-MM-GG")
    items = data["items"]
    if not 5 <= len(items) <= 25:
        errors.append(f"numero di notizie anomalo: {len(items)}")
    leads = [i for i in items if i.get("lead")]
    if len(leads) != 1:
        errors.append(f"serve esattamente una notizia di apertura (lead), trovate {len(leads)}")
    ids, urls = set(), set()
    for n, it in enumerate(items, 1):
        tag = it.get("id", f"#{n}")
        for key in ("id", "topic", "source", "place", "date", "url", "title", "summary"):
            if key not in it:
                errors.append(f"{tag}: manca '{key}'")
        if it.get("id") in ids:
            errors.append(f"{tag}: id duplicato")
        ids.add(it.get("id"))
        if it.get("url") in urls:
            errors.append(f"{tag}: url duplicato")
        urls.add(it.get("url"))
        if it.get("topic") not in TOPICS:
            errors.append(f"{tag}: tema non valido '{it.get('topic')}'")
        if not str(it.get("url", "")).startswith("http"):
            errors.append(f"{tag}: url non valido")
        if not COUNTRY.match(str(it.get("country", ""))):
            errors.append(f"{tag}: country deve essere un codice ISO di 2 lettere maiuscole (es. AR, BR, IT)")
        if it.get("area") not in AREAS:
            errors.append(f"{tag}: area deve essere una tra {', '.join(sorted(AREAS))}")
        if it.get("kind") not in KINDS:
            errors.append(f"{tag}: kind deve essere comunita, istituzionale o agenzia")
        if not DATE.match(str(it.get("date", ""))):
            errors.append(f"{tag}: data non valida")
        for field in ("title", "summary"):
            block = it.get(field, {})
            for lg in LANGS:
                text = (block.get(lg) or "").strip()
                if not text:
                    errors.append(f"{tag}: {field}.{lg} vuoto")
                elif field == "summary" and len(text.split()) > 75:
                    errors.append(f"{tag}: summary.{lg} troppo lungo ({len(text.split())} parole, max 75)")
    return errors


if __name__ == "__main__":
    errs = main(sys.argv[1] if len(sys.argv) > 1 else "public/data/news.json")
    if errs:
        print("ERRORI:")
        print("\n".join(" - " + e for e in errs))
        sys.exit(1)
    print("OK")
