# PLAN: Website für NOI Ristorante Pizzeria, Bad Rothenfelde

Stand: 29.09.2026 · Phase: **Vorbereitung für den Bau** (Planung + Datensammlung, noch kein Code)

## Ziel

Eine eigene, schnelle und rechtssichere Website für das NOI (Birkenstraße 2, 49214 Bad Rothenfelde). Heute hat das NOI **keine eigene Website**. Gäste finden nur Facebook, Instagram und Fremdportale (Tripadvisor, Speisekarte-Seiten, Restaurant Guru). Diese Portale zeigen veraltete oder widersprüchliche Daten (siehe `daten/restaurant.json`, Feld `widersprueche`).

Die Website soll drei Dinge leisten:

1. **Tisch bekommen:** Anrufen oder reservieren mit einem Tipp, auf dem Handy.
2. **Speisekarte lesen:** aktuelle Karte als Text (nicht als PDF oder Foto), mit Monatskarte.
3. **Richtige Fakten:** Öffnungszeiten, Adresse, Anfahrt aus einer Quelle, die das NOI selbst pflegt.

## Nicht-Ziele (für Version 1)

- Kein Online-Shop, keine eigene Bezahlung.
- Keine eigene Lieferplattform. Lieferung/Abholung nur verlinken, falls das NOI es anbietet.
- Kein CMS oder Login. Pflege über eine Datendatei (siehe „Technik“).

## Vorbild: Collo Restaurant + Bar (Bad Rothenfelde)

Das Collo liegt im selben Ort (Osnabrücker Straße 6) und hat eine einfache Website. Wir nehmen sie als Vorlage für Umfang und Aufbau, verbessern aber die Schwachstellen.

Website: https://sites.google.com/view/collorestaurantbar/startseite

### Aufbau Collo

| Seite | Inhalt |
|---|---|
| Startseite | Großes Titelbild, Slogan „Spanisch-italienisch“, Abschnitte: Willkommen („Tauchen Sie ein in eine Welt voller mediterraner Genüsse!“), Frische Zutaten, „Ein Ort zum Verweilen“ (Anlässe), Bar |
| Speisekarte | Text-Karte mit Sprungmarken, 12 Kategorien: Neuigkeiten, Tapas, Pizzabrötchen, Salate, Bruschetta, Pizza, Spaghetti, Penne, Roastbeef, Hähnchen/Schwein, Fisch, Beilagen |
| Küchenchef | Porträt von Chefkoch Rafael Soto (seit 1996 in der Gastronomie), Küchenphilosophie |
| Kontakt | Adresse, Telefon, E-Mail, Öffnungszeiten, Online-Reservierung über resmio |

### Was wir übernehmen

- **Wenige Seiten, klare Navigation** (4 Hauptpunkte).
- **Speisekarte als Text mit Kategorien-Sprungmarken.** Gut für Handy, Suche und Google.
- **Menschen zeigen:** Collo zeigt den Koch. NOI zeigt die Inhaber Kevin und Mara (familiengeführt, Punkt in fast allen Bewertungen).
- **Rubrik „Neuigkeiten“** oben in der Karte. Beim NOI: die **Monatskarte**.
- **Online-Reservierung** als Option (Collo nutzt resmio).

### Was wir besser machen

| Schwachstelle Collo | Lösung NOI |
|---|---|
| Kein Impressum, keine Datenschutzerklärung (Pflicht in Deutschland, Abmahnrisiko) | Impressum + Datenschutz von Anfang an, im Footer jeder Seite |
| Keine eigene Domain (Google-Sites-Adresse) | Eigene Domain, z. B. `noi-badrothenfelde.de` (Verfügbarkeit prüfen) |
| E-Mail unterschiedlich geschrieben (`gmail.com` und `gmail.de`) | Kontaktdaten nur an einer Stelle pflegen (Datendatei), überall gleich ausgeben |
| Keine Karte/Anfahrt | Anfahrt mit Parkhinweis. Karte erst nach Klick laden (DSGVO) |
| Kein Klick-zum-Anrufen, keine Öffnungszeiten prominent auf der Startseite | Kopfzeile mit „Jetzt geöffnet / öffnet um 17:30“ und Anruf-Knopf |
| Keine Hinweise auf Allergene/Zusatzstoffe | Allergen- und Zusatzstoff-Kennzeichnung in der Karte (Pflicht gilt vor Ort; online empfohlen) |
| Keine strukturierten Daten für Google | `schema.org/Restaurant` mit Öffnungszeiten, Menü-Link, Adresse |

## Sitemap NOI (Version 1)

| Seite | Datei | Inhalt |
|---|---|---|
| Start | `index.html` | Titelbild (Fachwerkhaus/Pizza), Slogan, Öffnungsstatus live, Knöpfe „Anrufen“ + „Tisch reservieren“, Monatskarte-Teaser, 3 Stärken (Pizza wie in Italien, familiengeführt, Fachwerk-Ambiente), Bewertungs-Zitate (nur mit Erlaubnis), Anfahrt kurz |
| Speisekarte | `speisekarte.html` | Monatskarte oben, dann Kategorien (Antipasti/Bruschetta, Pizza, Pasta, Panini, Fritto Misto, Dolci, Getränke). Sprungmarken, Filter „vegetarisch“, Allergen-Kürzel |
| Über uns | `ueber-uns.html` | Kevin Gribat und Mara Calzona, Geschichte, das Haus (altes Fachwerk, italienische Deko mit Film- und Musikstars), Team |
| Reservieren & Kontakt | `kontakt.html` | Telefon, Öffnungszeiten, Reservierung (Telefon; optional Tool), Anfahrt, Parken, Barrierefreiheit, Gruppen/Feiern |
| Impressum | `impressum.html` | Pflichtangaben nach § 5 DDG |
| Datenschutz | `datenschutz.html` | DSGVO-Erklärung (Hosting, Reservierungstool, Karte, Social-Links) |

Später möglich (Version 2): Gutscheine, Veranstaltungen (z. B. Themenabende), Abholbestellung, Englisch für Kurgäste.

## Design-Richtung

- **Stimmung:** Italienische Trattoria im alten Fachwerkhaus. „Dolce Vita“ mit Kino- und Musik-Nostalgie (die Deko zeigt Schauspieler und Musiker).
- **Farben (Vorschlag, mit Inhabern abstimmen):** warmes Creme als Hintergrund, Tomatenrot als Akzent, Basilikumgrün sparsam, dunkles Holzbraun für Schrift. Dunkler Modus mit Holzbraun als Grund.
- **Schrift:** eine klassische Serifenschrift für Überschriften (Speisekarten-Gefühl), eine gut lesbare serifenlose für Text. Lokal eingebunden, nicht von Google geladen (DSGVO).
- **Fotos:** echte Fotos vom NOI (Pizza aus dem Ofen, Gastraum, Fachwerk-Fassade, Kevin und Mara). Keine Stockfotos. Bildrechte klären (siehe `OFFENE-FRAGEN.md`).
- **Handy zuerst:** Die meisten Besucher kommen vom Handy (Suche „Pizza Bad Rothenfelde“). Anruf-Knopf immer sichtbar.

## Technik (angelehnt an die bestehenden Projekte)

- **Statische Seiten (HTML/CSS/wenig JavaScript)** wie `homepage/` und `Shop.Linus`. Kein Server, keine Datenbank, schnell, günstig.
- **Eine Datendatei als einzige Quelle:** `daten/restaurant.json` (Kontakt, Zeiten) und später `daten/speisekarte.json` (Gerichte, Preise, Allergene). Ein Build-Skript (wie `homepage/build.py`) erzeugt daraus die Seiten und das `schema.org`-JSON-LD. Preis ändern = eine Zeile ändern.
- **Öffnungsstatus:** kleines Skript liest die Zeiten und zeigt „Jetzt geöffnet bis 23:00“ bzw. „Heute Ruhetag“.
- **Hosting:** Vorschau auf GitHub Pages. Für den echten Betrieb: Hosting mit Serverstandort EU und AV-Vertrag, eigene Domain mit HTTPS.
- **Keine Einbettungen ohne Einwilligung:** Instagram, Facebook, Google Maps nur als Link oder mit Zwei-Klick-Lösung. Keine Cookies nötig, daher kein Cookie-Banner.
- **Reservierung:** Version 1 per Telefon (bewährt). Optional ein Tool (resmio wie Collo, oder OpenTable/Quandoo). Entscheidung liegt bei den Inhabern (Kosten, Aufwand).

## Datensammlung

| Datei | Inhalt | Stand |
|---|---|---|
| `daten/restaurant.json` | Stammdaten aus Webquellen, jede Angabe mit Quelle und Status (`bestaetigt`, `unsicher`, `fehlt`), Widersprüche | gesammelt, **muss von Inhabern bestätigt werden** |
| `daten/speisekarte-fragmente.json` | Die wenigen öffentlich auffindbaren Gerichte mit Preis und Datum der Quelle | Fragmente, **aktuelle Karte fehlt** |
| `OFFENE-FRAGEN.md` | Checkliste für das Gespräch mit Kevin und Mara | offen |

Wichtig: Öffentliche Portale sind **keine verlässliche Quelle**. Die Karte-Fragmente sind von 2021 und 2024. Vor dem Bau brauchen wir die aktuelle Speisekarte direkt vom NOI.

## Bauablauf (nach der Vorbereitung)

1. **Gespräch mit Inhabern** anhand `OFFENE-FRAGEN.md`. Ergebnis: bestätigte Daten, Karte, Fotos, Wünsche.
2. **Daten fertig:** `restaurant.json` bereinigen, `speisekarte.json` anlegen.
3. **Entwurf:** Startseite als Klick-Prototyp, Farben und Schrift abstimmen.
4. **Bau:** alle Seiten + Build-Skript + JSON-LD.
5. **Rechtstexte:** Impressum und Datenschutz mit echten Angaben (Platzhalter gelb markieren wie bei Shop.Linus, bis bestätigt).
6. **Prüfung:** Handy (iPhone/Android), Ladezeit (Ziel: Lighthouse ≥ 90 in allen Kategorien), Barrierefreiheit (Kontrast, Alt-Texte, Tastatur).
7. **Livegang:** Domain, Hosting, Google-Unternehmensprofil auf neue Website verlinken, Instagram/Facebook-Bio anpassen.
8. **Portale korrigieren:** Zeiten auf Tripadvisor, Yelp, Speisekarten-Seiten angleichen (Inhaber-Zugang nötig).

## Akzeptanzkriterien Version 1

- Anruf und Reservierung erreichbar mit höchstens einem Tipp auf jeder Seite.
- Speisekarte vollständig als Text, Preise identisch mit der Karte im Restaurant.
- Öffnungszeiten stehen nur in `restaurant.json` und stimmen auf allen Seiten und im JSON-LD überein.
- Impressum und Datenschutz vorhanden und von jeder Seite verlinkt.
- Keine Verbindung zu Drittanbietern beim Laden der Seite (Schriften, Karten, Social lokal oder per Klick).
- Seite funktioniert ab 320 px Breite ohne seitliches Scrollen.

## Quellen (abgerufen am 29.09.2026)

- Collo Website: https://sites.google.com/view/collorestaurantbar/startseite (+ `/speisekarte`, `/kontakt`, `/küchenchef`)
- NOI Tripadvisor: https://www.tripadvisor.com/Restaurant_Review-g198417-d18782747-Reviews-Noi-Bad_Rothenfelde_Lower_Saxony.html
- NOI speisekarte.de: https://www.speisekarte.de/bad-rothenfelde/restaurant/noi/speisekarte
- NOI speisekartenweb.de: https://speisekartenweb.de/restaurants/rothenfelde/noi-ristorante-pizzeria-49410
- NOI mymenuweb: https://mymenuweb.com/de/restaurants/1811018/
- NOI placejoys: https://noi-ristorante-pizzeria.placejoys.com/
- NOI Restaurant Guru: https://restaurantguru.com/NOI-Bad-Rothenfelde
- NOI Instagram: https://www.instagram.com/makeitnoi/ · Facebook: https://www.facebook.com/MakeitNoi/
