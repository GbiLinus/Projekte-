"""Erzeugt index.html aus template.html und menu.py.

Aufruf:  python3 build.py
"""
from html import escape
from pathlib import Path

from menu import MENU, SPECIALS

ROOT = Path(__file__).parent
RESERVE = "https://app.resmio.com/collo-restaurant-bar/widget?id=collo-restaurant-bar"
MENU_DATE = "September 2026"
BAND = ["Tapas", "Pizza", "Pasta", "Roastbeef", "Fisch", "Vino", "Aperitivo", "Pan casero"]


def dish(no, name, desc, price, tag="li"):
    no_html = f'<span class="dish__no">{escape(no)}</span>' if no else ""
    desc_html = f'<p class="dish__desc">{escape(desc)}</p>' if desc else ""
    return (
        f'<{tag} class="dish">{no_html}'
        f'<div class="dish__body"><div class="dish__row">'
        f'<h4 class="dish__name">{escape(name)}</h4>'
        f'<span class="dish__dots" aria-hidden="true"></span>'
        f'<span class="dish__price">{price}</span></div>{desc_html}</div></{tag}>'
    )


def build():
    specials = "\n".join(
        f'      <li><span class="board__name">{escape(n)}</span>'
        f'<span class="board__price">{p}</span>'
        f'<span class="board__desc">{escape(d)}</span></li>'
        for _, n, d, p in SPECIALS
    )

    chips = "\n".join(
        f'      <a href="#{sid}">{escape(title)}</a>' for sid, title, *_ in MENU
    )

    sections = []
    for sid, title, intro, note, items in MENU:
        wide = " menu__sec--wide" if len(items) > 12 else ""
        intro_html = f'<p class="menu__sub">{escape(intro)}</p>' if intro else ""
        note_html = f'<p class="menu__foot">{escape(note)}</p>' if note else ""
        dishes = "\n".join("      " + dish(*i) for i in items)
        sections.append(
            f'  <section id="{sid}" class="menu__sec{wide}" aria-labelledby="{sid}-t">\n'
            f'    <header class="menu__sechead"><h3 id="{sid}-t">{escape(title)}</h3>'
            f'<span class="menu__count">{len(items)}</span>{intro_html}</header>\n'
            f'    <ul class="menu__list">\n{dishes}\n    </ul>\n'
            f'    {note_html}\n  </section>'
        )

    band = "".join(f"<span>{w}</span>" for w in BAND) * 2

    html = (ROOT / "template.html").read_text(encoding="utf-8")
    for key, val in {
        "SPECIALS": specials,
        "CHIPS": chips,
        "MENU": "\n\n".join(sections),
        "BAND": band,
        "RESERVE": RESERVE,
        "MENU_DATE": MENU_DATE,
    }.items():
        html = html.replace("{{" + key + "}}", val)
    assert "{{" not in html, "Platzhalter übrig"
    (ROOT / "index.html").write_text(html, encoding="utf-8")
    print("index.html geschrieben")


if __name__ == "__main__":
    build()
