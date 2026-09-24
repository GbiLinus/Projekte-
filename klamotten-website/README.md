# Klamotten-Website

Neue Website für eine Kleidungsmarke. Status: **Planung**, noch kein Code.

## Reihenfolge (wichtig)

1. **Erst die Website, die richtig funktioniert.** Sie muss alle Zwecke erfüllen: Produkte zeigen, Größen und Varianten, Warenkorb und Kauf (oder Anfrage), Über uns, Kontakt, Impressum und Datenschutz, mobil nutzbar, schnell.
2. **Erst ganz am Ende die große Animation.** Ein Kleidungsstück, das später ausgesucht wird, soll im **Nähvorgang** gezeigt werden, in der Art der Referenz unten. Die Animation ist ein Extra und darf die Funktion der Seite nicht bremsen.

## Referenz: „IGLOO“-Website (TikTok von @webhyped)

Video vom 24.09.2026, ca. 12 Sekunden Bildschirmaufnahme. Standbilder: [`referenz/igloo-animation-standbilder.jpg`](referenz/igloo-animation-standbilder.jpg)

![Standbilder der Referenz](referenz/igloo-animation-standbilder.jpg)

### Was passiert (Ablauf beim Scrollen)

| Zeit | Szene |
|---|---|
| 0,3 s | Drahtgitter/Punktlinien über einer Schneelandschaft, das Iglu entsteht aus dem Gitter |
| 1,5 s | Das Iglu ist fertig: realistische 3D-Szene, Kamera schräg von oben |
| 3,6 s | Beim Scrollen lösen sich einzelne Eisblöcke und schweben heraus, kleine Datenlabels hängen daran |
| 4,8 s | Die Blöcke setzen sich wieder zusammen |
| 5,8–6,8 s | Die Kamera fliegt hinein, Nebel und Weißblende, ein Eiskristall-Brocken rotiert |
| 7,3–9,0 s | Die Blöcke ordnen sich zu Ringen, ein Tunnel- oder Portal-Effekt mit Leuchten in der Mitte |
| 10,2 s | Eine Figur (Pinguin) aus tausenden Partikeln auf einer runden Plattform („Produkt-Bühne“) |
| 11,2 s | Die Blöcke fliegen zurück und bauen das Iglu wieder auf, der Kreis schließt sich |

### Design-Merkmale

- **Farben:** fast monochrom, eisiges Weiß, Hellgrau und kühles Blau. Keine bunten Akzente, das Objekt ist der Star.
- **Typografie/UI:** kleines Logo oben links („IGLOO“, breite Pixel- oder Tech-Schrift), winzige Monospace-Texte in den Ecken (Copyright, „Scroll down to discover“, „Sound: OFF“). Sehr zurückhaltend, wirkt wie ein technisches Interface.
- **Scroll-gesteuert:** Die Animation läuft nicht von selbst. Der Scrollbalken ist die Zeitleiste und treibt jeden Schritt an.
- **Ein Objekt, das sich zerlegt und neu zusammensetzt:** Teile lösen sich, schweben, ordnen sich neu und fügen sich wieder zusammen.
- **Weiche Übergänge:** Nebel, Weißblenden, Tiefenunschärfe, Kamera-Flüge statt harter Schnitte.
- **Partikel-Look:** Objekte bestehen teils aus Punktwolken oder Drahtgittern, bevor sie „fest“ werden.
- **Sound-Schalter:** optionaler Ton, standardmäßig aus.

## Übertragen auf Kleidung: „Nähvorgang“-Animation (später)

Idee für das ausgewählte Teil (z. B. Hoodie oder Jacke), gesteuert durch Scrollen:

1. **Schnittmuster:** Drahtgitter- oder Punktlinien zeichnen die Schnittteile flach auf den Hintergrund (wie das Gitter bei 0,3 s).
2. **Stoff:** Die Schnittteile bekommen Stofftextur und schweben einzeln im Raum (wie die losen Eisblöcke).
3. **Nähen:** Die Teile fliegen zueinander, eine Naht läuft als leuchtende Linie entlang der Kanten (Stich für Stich), Nadel oder Faden-Partikel optional.
4. **Details:** Kamera-Flug nah an Naht, Label, Reißverschluss, Nebel- oder Weißblende als Übergang.
5. **Fertig:** Das fertige Teil dreht sich auf einer runden Plattform (wie der Pinguin), daneben Name, Preis und „In den Warenkorb“.
6. **Optional:** Beim Weiterscrollen zerlegt es sich wieder in Schnittteile (Kreis schließt sich).

Stil übernehmen: ruhige Farbwelt passend zur Marke, kleine Monospace-UI in den Ecken, viel Leerraum, das Kleidungsstück im Mittelpunkt.

### Technik (Vorschlag für später)

- **Three.js** (WebGL) für die 3D-Szene, **GSAP ScrollTrigger** für die Kopplung an den Scrollbalken.
- 3D-Modell des Kleidungsstücks mit getrennten Schnittteilen, z. B. aus **CLO3D** oder **Marvelous Designer** (dort entstehen Schnittteile und Nähte sowieso), exportiert als glTF.
- Alternativ, einfacher: vorgerenderte Bildsequenz (z. B. aus Blender), die per Scroll durchgeblättert wird. Sieht fast gleich aus und läuft auf Handys stabiler.
- Rückfall ohne Animation für langsame Geräte und für „Bewegung reduzieren“ (`prefers-reduced-motion`).
