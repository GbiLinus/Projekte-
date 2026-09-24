# mein-plugin

Start-Plugin für Claude Code.

## Inhalt

| Bestandteil | Datei | Zweck |
|---|---|---|
| Befehl | `commands/hallo.md` | `/mein-plugin:hallo [name]`: Begrüßung und Projektüberblick |
| Skill | `skills/hallo/SKILL.md` | Wird automatisch genutzt, wenn nach einer Projektzusammenfassung gefragt wird |
| Agent | `agents/pruefer.md` | Prüft aktuelle Änderungen und ändert dabei nichts |
| Hook | `hooks/hooks.json` | Meldung beim Sitzungsstart |

## Installation

In Claude Code:

```
/plugin marketplace add GbiLinus/Projekte-
/plugin install mein-plugin@gbilinus-plugins
```

Lokal zum Testen (aus dem Repo-Wurzelverzeichnis):

```
/plugin marketplace add ./
/plugin install mein-plugin@gbilinus-plugins
```

Oder ohne Installation: `claude --plugin-dir ./mein-plugin`

## Erweitern

- Neue Befehle: weitere `.md`-Dateien in `commands/`
- Neue Skills: `skills/<name>/SKILL.md`
- Neue Agenten: `agents/<name>.md`
- Nach Änderungen `version` in `.claude-plugin/plugin.json` und `marketplace.json` erhöhen.
