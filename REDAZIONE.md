# Guida di redazione – Diario Italia Argentina

Istruzioni per preparare il numero quotidiano di https://argentina.diarioitalia.org, edizione argentina di Diario Italia.

## Il numero del giorno

- Ogni giorno alle 7:00 (ora di Buenos Aires) esce un nuovo numero con **8–20 notizie** sulla collettività italiana in Argentina, pubblicate nelle ultime 24–48 ore (fino a 72 ore il lunedì e dopo i festivi) dalle fonti di `fonti.json`.
- Una sola notizia è l'**apertura** (`"lead": true`): la più rilevante per la collettività italiana in Argentina.
- Ogni notizia ha **titolo e sintesi in due lingue**: spagnolo (versione principale) e italiano.
- Ogni notizia rimanda con `url` all'articolo o al post originale.
- Se ci sono meno di 6 notizie nuove e valide, non si pubblica (vedi "Pubblicazione").

## Che cosa entra

Solo notizie che riguardano la collettività italiana **in Argentina**: attività di società italiane, federazioni, associazioni regionali, scuole e Dante Alighieri; Comites e rappresentanza; consolati (solo notizie di interesse per la collettività); cittadinanza, AIRE, voto all'estero, passaporti; cultura e lingua italiana in Argentina; imprese e rapporti economici Italia–Argentina; sport della collettività; visite istituzionali italiane in Argentina.

Notizie dall'Italia (`area: italia`) solo se toccano direttamente gli italo-argentini (per esempio riforme della cittadinanza o del voto all'estero), al massimo 1–2 per numero.

## Come cercare

Le fonti sono in `fonti.json` (campo `gruppo`, campo `area` per la regione, campi `sito`, `facebook`, `instagram`).

1. **Siti web** – WebSearch con `allowed_domains`, circa 10 domini per ricerca, raggruppando per regione (`area`):
   - gruppo 1 (media e associazioni della collettività): il cuore del numero;
   - gruppo 2 (istituzionali: Ambasciata, consolati, Istituti di Cultura, Comites, Camere di commercio): per i consolati basta il dominio `esteri.it`. Dai siti consolari solo notizie di interesse per la collettività (nuovo console, elezioni Comites, cittadinanza/passaporti/AIRE, eventi, missioni). Escludere tariffe, gare, sponsorizzazioni, chiusure, turni Prenot@mi, assunzioni;
   - gruppo 3 (agenzie e media italiani: AISE, ANSA, Italia Chiama Italia): solo notizie sull'Argentina.
   - Gruppi 2 e 3 sommati: **al massimo 5–6 notizie per numero**, per lasciare spazio alla collettività.
2. **Facebook e Instagram** – molte associazioni pubblicano solo sui social. Cercare con `allowed_domains` `facebook.com` e `instagram.com` usando i nomi delle fonti (per esempio "Sociedad Italiana" + città) e le parole chiave sotto. Usare solo post pubblici con data chiara e recente, e mettere in `url` il link al post o alla pagina. I gruppi Facebook e i profili personali indicati nelle note di `fonti.json` di solito non sono leggibili: non insistere.
3. **Ricerche per parola chiave** (senza filtro di dominio), 4–6 al giorno, per trovare notizie nei media locali argentini: "colectividad italiana", "sociedad italiana", "comunidad italiana", "ítalo-argentinos", "ciudadanía italiana", "Comites", "cónsul de Italia", "Dante Alighieri", "fiesta italiana", "festa della Repubblica" + città (Buenos Aires, Córdoba, Rosario, Mendoza, La Plata, Mar del Plata, Bahía Blanca, Tucumán, Salta, Paraná, Neuquén, Bariloche…). Usare solo testate riconoscibili, indicando in `source` il nome del media.
4. Le fonti con `stato` "Da verificare" si usano solo se la notizia è recente e il sito risulta attivo.
5. **La Camera di Commercio Italiana di Córdoba non è una fonte del giornale** (in sospeso per decisione dell'editore).

## Selezione

- Varietà di regioni e di temi; al massimo 3 notizie dalla stessa fonte.
- Escludere notizie già pubblicate nei numeri precedenti (controllare `public/data/archive/`).
- Eventi: preferire quelli dei prossimi giorni o appena avvenuti; non pubblicare eventi già passati da più di 3 giorni.
- Gli articoli di opinione vanno presentati come commento, attribuendo la posizione all'autore.

## Temi (`topic`)

| codice | tema (es / it) |
|---|---|
| `societa` | Sociedad / Società (emigrazione, rientri, dati, storie) |
| `politica` | Política y representación / Politica e rappresentanza (Comites, CGIE, parlamentari eletti all'estero) |
| `cittadinanza` | Ciudadanía y consulados / Cittadinanza e consolati (cittadinanza, AIRE, passaporti, pensioni, servizi) |
| `comunita` | Colectividad y asociaciones / Collettività e associazioni |
| `cultura` | Cultura e idioma / Cultura e lingua |
| `economia` | Economía y empresas / Economia e imprese (camere di commercio, missioni, investimenti) |
| `sport` | Deporte / Sport |
| `italia` | Desde Italia / Dall'Italia |

## Regioni (`area`)

| codice | regione |
|---|---|
| `nacional` | Tutto il paese (notizie nazionali, Ambasciata, federazioni nazionali) |
| `amba` | Città di Buenos Aires e Grande Buenos Aires (Morón, Lomas de Zamora…) |
| `bonaerense` | Resto della provincia di Buenos Aires (La Plata, Mar del Plata, Bahía Blanca…) |
| `centro` | Córdoba e Santa Fe (Rosario compresa) |
| `noa` | Tucumán, Salta, Jujuy, Catamarca, Santiago del Estero, La Rioja |
| `nea` | Entre Ríos, Corrientes, Misiones, Chaco, Formosa |
| `cuyo` | Mendoza, San Juan, San Luis |
| `patagonia` | La Pampa, Neuquén, Río Negro, Chubut, Santa Cruz, Tierra del Fuego |
| `italia` | Notizie dall'Italia |

## Regole di scrittura

- **Sintesi di 2–3 frasi (max 70 parole)**, scritte con parole proprie. Non copiare frasi degli articoli e non usare virgolettati lunghi: la sintesi informa e invita a leggere la fonte.
- Lo spagnolo è la versione principale: spagnolo neutro, comprensibile in tutta l'Argentina (si può usare il "voseo" solo nelle citazioni). L'italiano è una traduzione fedele.
- Riportare solo fatti presenti nella fonte: date, luoghi, cifre, nomi. Se un dato non è chiaro, ometterlo.
- **Neutralità politica**, anche nelle elezioni dei Comites: attribuire le posizioni a chi le esprime, senza giudizi della redazione; se possibile dare conto anche della posizione opposta. Non presentare liste o candidati.
- Titoli brevi e informativi, senza punto esclamativo né clickbait.
- Mantenere sigle italiane (AIRE, Comites, CGIE) e nomi propri delle associazioni.

## Formato del file

Vedi `public/data/news.json`. Campi di ogni notizia: `id` (slug unico), `topic`, `lead` (solo l'apertura), `source` (nome della fonte), `place` (città), `country` (`AR`, oppure `IT` per le notizie dall'Italia: determina la bandiera), `area` (regione, vedi sopra), `kind` (`comunita`, `istituzionale` o `agenzia`), `date` (AAAA-MM-GG), `url`, `title` e `summary` con le chiavi `es it`.

## Pubblicazione

1. Scrivere il nuovo numero in `public/data/news.json` (`edition` = data di oggi, `updated` = ora ISO con fuso -03:00, `sources_monitored` = numero di fonti in `fonti.json`).
2. Copiarlo anche in `public/data/archive/AAAA-MM-GG.json`.
3. Aggiungere la data in testa a `dates` in `public/data/archive/index.json`.
4. Controllare: `python3 scripts/validate.py public/data/news.json` deve rispondere `OK`.
5. Materiale social (storia verticale 1080x1920 per @diarioitalianews; il feed resta all'edizione mondiale): scegliere 4 notizie adatte ai social (interesse ampio, regioni diverse, toni positivi o informativi; niente cronaca nera, polemiche politiche o lutti) ed eseguire `python3 scripts/social.py id1 id2 id3 id4`. Controllare l'immagine `public/social/AAAA-MM-GG.png` prima del commit.
6. Commit su `main` e push: Cloudflare Workers pubblica automaticamente in 1–2 minuti.

## Pagine statiche

Le pagine Quiénes somos, Fuentes, Enviar una noticia e Privacidad (`public/chi-siamo.html`, `fonti.html`, `segnala.html`, `privacy.html`) sono generate da `scripts/build_pages.py` con i testi di `scripts/pages_content.py`. Non modificarle a mano. Se cambia `fonti.json`, rieseguire `python3 scripts/build_pages.py`.
