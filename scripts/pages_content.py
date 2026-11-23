# Testi delle pagine statiche di Diario Italia Argentina, in spagnolo (principale) e italiano (Markdown).
# Adattati dai testi di Diario Italia (documento "Diario Italia – Testi delle nuove pagine", 15/11/2026).
# Dopo una modifica: python3 scripts/build_pages.py

MAIL = "[info@diarioitalia.org](mailto:info@diarioitalia.org)"

NAV = {
    "es": {"home": "Noticias", "chi-siamo": "Quiénes somos", "fonti": "Fuentes", "segnala": "Enviar una noticia", "privacy": "Privacidad y aviso legal"},
    "it": {"home": "Notizie", "chi-siamo": "Chi siamo", "fonti": "Fonti", "segnala": "Segnala una notizia", "privacy": "Privacy e note legali"},
}

# Etichette per la pagina Fonti
FONTI_UI = {
    "es": {"kinds": {"1": "Colectividad", "2": "Institución", "3": "Agencia"}, "count": "{n} fuentes", "web": "Sitio", "fb": "Facebook", "ig": "Instagram"},
    "it": {"kinds": {"1": "Collettività", "2": "Istituzione", "3": "Agenzia"}, "count": "{n} fonti", "web": "Sito", "fb": "Facebook", "ig": "Instagram"},
}

PAGES = {}

# ---------------------------------------------------------------- CHI SIAMO
PAGES["chi-siamo"] = {
"es": f"""# Quiénes somos

**Diario Italia Argentina reúne cada mañana las noticias de la colectividad italiana en Argentina y las cuenta en español e italiano.**

Argentina tiene la colectividad de ciudadanos italianos más grande del mundo fuera de Italia, y millones de argentinos descienden de italianos. Su vida se cuenta todos los días en diarios y radios de la colectividad, en las páginas de consulados y Comites y en las redes de cientos de sociedades italianas, federaciones y asociaciones regionales, de Buenos Aires a Salta y de Rosario a la Patagonia. Diario Italia Argentina reúne esas noticias en una única cita diaria, fácil de leer y de compartir.

Es la edición argentina de [Diario Italia](https://diarioitalia.org), el diario de los italianos en el mundo.

## Cómo se arma cada número

1. Cada día seguimos casi un centenar de fuentes: medios de la colectividad, la Embajada, los consulados, los Comites, las Cámaras de Comercio italianas, las federaciones y las asociaciones de todo el país, también en sus páginas de Facebook e Instagram.
2. Seleccionamos las noticias más relevantes de las últimas 24–48 horas, buscando variedad de regiones y de temas.
3. De cada noticia escribimos una breve síntesis original, en español y en italiano.
4. Cada síntesis indica la fuente y enlaza a la publicación completa.
5. El número está en línea cada mañana a las 7 y queda disponible en el archivo.

## Nuestros criterios

- **Siempre la fuente.** No reemplazamos a los medios ni a las asociaciones de la colectividad: los damos a conocer. Cada noticia lleva al sitio o a la página que la publicó.
- **Neutralidad.** No tomamos posición sobre partidos, candidatos o listas, tampoco en las elecciones de los Comites. Las opiniones siempre se atribuyen a quien las expresa.
- **Utilidad.** Damos espacio a lo que sirve a la colectividad: ciudadanía, servicios consulares, cultura, idioma, trabajo, vida de las asociaciones.
- **Textos propios.** Las síntesis las escribimos nosotros; no reproducimos los artículos originales.

## Contacto

Avisos, correcciones y propuestas de colaboración: {MAIL}.
""",
"it": f"""# Chi siamo

**Diario Italia Argentina raccoglie ogni mattina le notizie della collettività italiana in Argentina e le racconta in spagnolo e in italiano.**

L'Argentina ospita la più grande collettività di cittadini italiani al mondo fuori dall'Italia, e milioni di argentini discendono da italiani. La loro vita si racconta ogni giorno nei giornali e nelle radio della collettività, nelle pagine di consolati e Comites e sui social di centinaia di società italiane, federazioni e associazioni regionali, da Buenos Aires a Salta e da Rosario alla Patagonia. Diario Italia Argentina riunisce queste notizie in un unico appuntamento quotidiano, facile da leggere e da condividere.

È l'edizione argentina di [Diario Italia](https://diarioitalia.org), il giornale degli italiani nel mondo.

## Come nasce ogni numero

1. Ogni giorno seguiamo quasi un centinaio di fonti: media della collettività, l'Ambasciata, i consolati, i Comites, le Camere di commercio italiane, le federazioni e le associazioni di tutto il paese, anche sulle loro pagine Facebook e Instagram.
2. Selezioniamo le notizie più rilevanti delle ultime 24–48 ore, cercando varietà di regioni e di temi.
3. Di ogni notizia scriviamo una breve sintesi originale, in spagnolo e in italiano.
4. Ogni sintesi indica la fonte e rimanda alla pubblicazione completa.
5. Il numero è online ogni mattina alle 7 e resta consultabile nell'archivio.

## I nostri criteri

- **Sempre la fonte.** Non sostituiamo i media e le associazioni della collettività: li facciamo conoscere. Ogni notizia porta al sito o alla pagina che l'ha pubblicata.
- **Neutralità.** Non prendiamo posizione su partiti, candidati o liste, nemmeno nelle elezioni dei Comites. Le opinioni sono sempre attribuite a chi le esprime.
- **Utilità.** Diamo spazio a ciò che serve alla collettività: cittadinanza, servizi consolari, cultura, lingua, lavoro, vita associativa.
- **Testi propri.** Le sintesi sono scritte da noi; non riproduciamo gli articoli originali.

## Contatti

Segnalazioni, correzioni e proposte di collaborazione: {MAIL}.
""",
}

# ---------------------------------------------------------------- FONTI
PAGES["fonti"] = {
"es": f"""# Fuentes

**Cada número de Diario Italia Argentina nace del trabajo de los medios, las instituciones y las asociaciones de la colectividad italiana en todo el país.**

Esta página las enumera por región, con el enlace a su sitio o a sus redes sociales. Si un tema le interesa, vaya a la fuente: allí encontrará la información completa, y seguirlas es la mejor manera de apoyarlas.

Las fuentes son de tres tipos:

- **Colectividad** – diarios, radios y portales de la colectividad, federaciones, sociedades italianas, asociaciones regionales y escuelas. Son el corazón de cada número.
- **Instituciones** – Embajada, consulados, Comites, Istituti Italiani di Cultura y Cámaras de Comercio italianas, para las noticias de servicio y de interés para la colectividad.
- **Agencias y medios italianos** – agencias especializadas en los italianos en el mundo, solo para lo que se refiere a Argentina.

La lista crece todo el tiempo. ¿Su asociación o su medio no está? Escríbanos a {MAIL}.
""",
"it": f"""# Fonti

**Ogni numero di Diario Italia Argentina nasce dal lavoro dei media, delle istituzioni e delle associazioni della collettività italiana in tutto il paese.**

Questa pagina le elenca per regione, con il link al sito o ai profili social. Se un tema ti interessa, vai alla fonte: lì trovi l'informazione completa, e seguirle è il modo migliore per sostenerle.

Le fonti sono di tre tipi:

- **Collettività** – giornali, radio e portali della collettività, federazioni, società italiane, associazioni regionali e scuole. Sono il cuore di ogni numero.
- **Istituzioni** – Ambasciata, consolati, Comites, Istituti Italiani di Cultura e Camere di commercio italiane, per le notizie di servizio e di interesse per la collettività.
- **Agenzie e media italiani** – agenzie specializzate sugli italiani nel mondo, solo per ciò che riguarda l'Argentina.

L'elenco cresce di continuo. La tua associazione o il tuo giornale non c'è? Scrivici a {MAIL}.
""",
}

# ---------------------------------------------------------------- SEGNALA
PAGES["segnala"] = {
"es": f"""# Enviar una noticia

**¿Su sociedad italiana, asociación o Comites tiene una noticia? Envíenosla: Diario Italia Argentina puede hacerla llegar a toda la colectividad del país, en español y en italiano.**

Nos interesan en particular:

- actividades de sociedades italianas, asociaciones regionales, federaciones, Comites y círculos;
- eventos culturales, fiestas, muestras, cursos de idioma;
- historias de italianos y descendientes que se destacan en su ciudad;
- novedades sobre ciudadanía, servicios consulares, voto en el exterior, escuelas y becas;
- aniversarios y celebraciones de las colectividades.

## Cómo enviarla

Escriba a {MAIL} con:

1. el enlace a la noticia ya publicada (en su sitio, en su página de Facebook o Instagram) o un texto breve con una foto;
2. la ciudad;
3. el nombre de la institución y un contacto.

Es la mejor vía para las asociaciones que publican en grupos de Facebook o en perfiles personales, que no podemos seguir cada día. Las instituciones que deseen ser seguidas pueden escribirnos para entrar en la lista de fuentes.

## Qué pasa después

La redacción evalúa cada aviso. No podemos publicarlos todos ni garantizar plazos: damos prioridad a las noticias de interés general, verificables y recientes. No publicamos comunicados comerciales ni de propaganda electoral.
""",
"it": f"""# Segnala una notizia

**La tua società italiana, associazione o Comites ha una notizia? Mandacela: Diario Italia Argentina può farla arrivare a tutta la collettività del paese, in spagnolo e in italiano.**

Ci interessano in particolare:

- attività di società italiane, associazioni regionali, federazioni, Comites e circoli;
- eventi culturali, feste, mostre, corsi di lingua;
- storie di italiani e discendenti che si distinguono nella loro città;
- novità su cittadinanza, servizi consolari, voto all'estero, scuole e borse di studio;
- anniversari e celebrazioni delle collettività.

## Come inviarla

Scrivi a {MAIL} indicando:

1. il link alla notizia già pubblicata (sul sito, sulla pagina Facebook o Instagram) oppure un breve testo con una foto;
2. la città;
3. il nome dell'istituzione e un contatto.

È la via migliore per le associazioni che pubblicano in gruppi Facebook o su profili personali, che non possiamo seguire ogni giorno. Le istituzioni che desiderano essere seguite possono scriverci per entrare nell'elenco delle fonti.

## Cosa succede dopo

La redazione valuta ogni segnalazione. Non possiamo pubblicarle tutte né garantire i tempi: diamo priorità alle notizie di interesse generale, verificabili e recenti. Non pubblichiamo comunicati commerciali né propaganda elettorale.
""",
}

# ---------------------------------------------------------------- PRIVACY
PAGES["privacy"] = {
"es": f"""# Privacidad y aviso legal

**Diario Italia Argentina no usa cookies de seguimiento, no pide registrarse y no recoge datos personales de los lectores.**

## Datos y cookies

- **Ninguna cookie de seguimiento ni publicitaria.** El sitio no muestra publicidad ni usa herramientas de perfilado.
- **Preferencias técnicas.** El idioma y el tema claro/oscuro elegidos se guardan solo en su dispositivo, para recordarlos en la próxima visita. No se nos envían.
- **Estadísticas de visitas.** Usamos Cloudflare Web Analytics, que cuenta las visitas de forma agregada y anónima, sin cookies y sin identificar a cada lector.
- **Alojamiento.** El sitio está alojado en Cloudflare, que por razones técnicas y de seguridad trata datos de conexión como la dirección IP.
- **Email.** Si nos escribe, usamos su dirección y el contenido del mensaje solo para responderle. Puede pedir que se borren en cualquier momento.

## Contenidos

- Las síntesis publicadas son textos originales de Diario Italia Argentina. Cada noticia indica la fuente y enlaza a la publicación completa, que sigue siendo propiedad de sus autores.
- Los nombres y marcas de los medios e instituciones citados pertenecen a sus legítimos titulares.
- Hacemos lo posible por ser precisos, pero pueden escaparse errores. Avisos, correcciones o pedidos de eliminación: {MAIL}. Respondemos lo antes posible.
- Los enlaces a sitios externos llevan a contenidos de los que Diario Italia Argentina no es responsable.

## Titular

Diario Italia Argentina – argentina.diarioitalia.org – {MAIL}

*Última actualización: noviembre de 2026.*
""",
"it": f"""# Privacy e note legali

**Diario Italia Argentina non usa cookie di tracciamento, non chiede di registrarsi e non raccoglie dati personali dei lettori.**

## Dati e cookie

- **Nessun cookie di tracciamento o pubblicitario.** Il sito non mostra pubblicità e non usa strumenti di profilazione.
- **Preferenze tecniche.** La lingua e il tema chiaro/scuro scelti sono salvati solo sul tuo dispositivo, per ricordarli alla visita successiva. Non ci vengono inviati.
- **Statistiche delle visite.** Usiamo Cloudflare Web Analytics, che conta le visite in forma aggregata e anonima, senza cookie e senza identificare i singoli lettori.
- **Hosting.** Il sito è ospitato da Cloudflare, che per ragioni tecniche e di sicurezza tratta dati di connessione come l'indirizzo IP.
- **Email.** Se ci scrivi, usiamo il tuo indirizzo e il contenuto del messaggio solo per risponderti. Puoi chiederne la cancellazione in qualsiasi momento.

## Contenuti

- Le sintesi pubblicate sono testi originali di Diario Italia Argentina. Ogni notizia indica la fonte e rimanda alla pubblicazione completa, che resta di proprietà dei suoi autori.
- I nomi e i marchi dei media e delle istituzioni citati appartengono ai legittimi titolari.
- Facciamo il possibile per essere precisi, ma possono sfuggire errori. Segnalazioni, correzioni o richieste di rimozione: {MAIL}. Rispondiamo al più presto.
- I link a siti esterni portano a contenuti di cui Diario Italia Argentina non è responsabile.

## Titolare

Diario Italia Argentina – argentina.diarioitalia.org – {MAIL}

*Ultimo aggiornamento: novembre 2026.*
""",
}
