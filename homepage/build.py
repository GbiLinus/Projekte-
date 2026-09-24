#!/usr/bin/env python3
"""Erzeugt homepage/index.html aus soelden-skiurlaub/SOELDEN-SKIURLAUB.md.

Aufruf aus dem Repo-Root: python3 homepage/build.py
"""
import html
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
GUIDE = ROOT / "soelden-skiurlaub" / "SOELDEN-SKIURLAUB.md"
TEMPLATE = Path(__file__).with_name("template.html")
OUT = Path(__file__).with_name("index.html")

ICONS = {
    "Piste": "⛷️",
    "Freeride": "🏔️",
    "Genuss": "🧀",
    "Après": "🍻",
    "Abend": "🌙",
    "Schlechtwetter": "☁️",
}


def section(text: str, title: str) -> str:
    m = re.search(rf"^## {re.escape(title)}\n(.*?)(?=^## |\Z)", text, re.M | re.S)
    return m.group(1).strip() if m else ""


def inline(s: str) -> str:
    """Escape text and turn bare URLs into links."""
    s = html.escape(s)
    return re.sub(r"(https?://[^\s<]+)", r'<a href="\1" target="_blank" rel="noopener">Link</a>', s)


def ideas(text: str) -> str:
    out = []
    current = None
    for block in re.split(r"^### ", section(text, "Ideen"), flags=re.M):
        block = block.strip()
        if not block:
            continue
        head, _, body = block.partition("\n")
        if not re.match(r"\d+\.", head):
            if current:
                out.append("</div></div>")
            current = head.strip()
            icon = ICONS.get(current, "❄️")
            out.append(f'<div class="kategorie" id="kat-{html.escape(current.lower())}">'
                       f'<h3><span class="icon">{icon}</span>{html.escape(current)}</h3><div class="karten">')
            continue
        num, title = head.split(".", 1)
        fields = dict(re.findall(r"^- \*\*(.+?):\*\* (.*)$", body, re.M))
        rel = fields.get("Verlässlichkeit", "")
        badge = "ok" if rel.startswith("✅") else "warn"
        budget = fields.get("Budget", "").split(" – ")[0]
        out.append(f"""
<article class="karte" id="idee-{int(num)}">
  <div class="karte-kopf"><button class="nr" type="button" title="Als erledigt abhaken" aria-pressed="false">{int(num)}</button><span class="budget">{html.escape(budget)}</span></div>
  <h4>{html.escape(title.strip())}</h4>
  <p class="wo">📍 {inline(fields.get("Wo", ""))}</p>
  <p>{inline(fields.get("Warum speziell", ""))}</p>
  <p class="planb"><strong>Plan B:</strong> {inline(fields.get("Plan B", ""))}</p>
  <p class="rel {badge}">{inline(rel)}</p>
  <p class="quelle">{inline(fields.get("Quelle", ""))}</p>
</article>""")
    if current:
        out.append("</div></div>")
    return "\n".join(out)


def woche(text: str) -> str:
    items = []
    for line in section(text, "Beispielwoche").splitlines():
        m = re.match(r"Tag (\d) – ([^:]+): (.*)", line.strip())
        if m:
            items.append(f'<li><span class="tag">Tag {m[1]}<small>{html.escape(m[2])}</small></span>'
                         f'<span>{inline(m[3])}</span></li>')
    return "\n".join(items)


def checkliste(text: str) -> str:
    items = []
    for line in section(text, "Vor der Reise buchen").splitlines():
        m = re.match(r"- \*\*(.+?):\*\* (.*)", line.strip())
        if m:
            items.append(f"<li><strong>{html.escape(m[1])}:</strong> {inline(m[2])}</li>")
    return "\n".join(items)


def main() -> None:
    text = GUIDE.read_text(encoding="utf-8")
    page = TEMPLATE.read_text(encoding="utf-8")
    page = (page.replace("{{IDEEN}}", ideas(text))
                .replace("{{WOCHE}}", woche(text))
                .replace("{{CHECKLISTE}}", checkliste(text)))
    OUT.write_text(page, encoding="utf-8")
    count = page.count('class="karte"')
    print(f"{OUT} geschrieben: {count} Ideen")


if __name__ == "__main__":
    main()
