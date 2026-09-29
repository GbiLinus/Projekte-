# Collo – Restaurant + Bar, Bad Rothenfelde

Website-Entwurf für das spanisch-italienische Restaurant Collo, Osnabrücker Straße 6, 49214 Bad Rothenfelde.

Live (nach Merge in `main`): https://gbilinus.github.io/Projekte-/Collo-BadRothenfelde/

## Aufbau

| Datei | Inhalt |
|---|---|
| `menu.py` | Speisekarte (Tafel-Specials + alle Kategorien, Nummern, Preise) |
| `template.html` | Seitenaufbau mit Platzhaltern |
| `build.py` | Baut `index.html` aus Template und Karte |
| `style.css` | Gestaltung |
| `main.js` | „Jetzt geöffnet?“-Anzeige, heutiger Tag, aktive Kategorie |
| `fonts/` | Bodoni Moda und Karla, lokal (keine externen Server, DSGVO) |
| `FEHLT.md` | Was noch fehlt oder unsicher ist |

Karte oder Texte ändern: `menu.py` bzw. `template.html` bearbeiten, dann

```
python3 build.py
```

Lokal ansehen: `python3 -m http.server` und `http://localhost:8000` öffnen.

## Quellen

- Eigene Website: https://sites.google.com/view/collorestaurantbar/startseite (Texte, Karte, Küchenchef, Öffnungszeiten, Reservierungslink)
- Facebook: https://www.facebook.com/Collo.de/ (Adresse, Telefon, E-Mail)
- Osnabrücker Land: https://www.osnabruecker-land.de/gastro/collo-restaurant-bar (Adresse, Zeiten, Küche)
- Speisekarte.de, Tripadvisor, Yelp: nur zum Abgleich, Abweichungen in `FEHLT.md`
