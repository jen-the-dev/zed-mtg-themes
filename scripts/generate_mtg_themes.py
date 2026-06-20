#!/usr/bin/env python3
"""Generate Magic: The Gathering Zed theme JSON files."""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
THEMES_DIR = ROOT / "themes"
AUTHOR = "Jen the Dev MTG Collection"


@dataclass(frozen=True)
class Palette:
    background: str
    foreground: str
    accent: str
    muted: str
    string: str
    keyword: str
    appearance: str = "dark"


THEMES: dict[str, tuple[str, Palette]] = {
    "mtg-plains-white": ("Plains White", Palette("#171512", "#f8f0d8", "#d4af37", "#8a8272", "#e8dcc0", "#fff3bf")),
    "mtg-island-blue": ("Island Blue", Palette("#081018", "#9fd4ff", "#0e68ab", "#5a7a94", "#7ec8e3", "#4db8ff")),
    "mtg-swamp-black": ("Swamp Black", Palette("#0d0a0f", "#c8b6d8", "#6b46a1", "#5c4d66", "#a78bfa", "#9333ea")),
    "mtg-mountain-red": ("Mountain Red", Palette("#160909", "#ffb199", "#d3202a", "#7a4444", "#ff8a65", "#ff5252")),
    "mtg-forest-green": ("Forest Green", Palette("#08140d", "#a8e6c1", "#00733e", "#4d6655", "#66bb6a", "#2ecc71")),
    "mtg-azorius-wu": ("Azorius Senate", Palette("#101820", "#d7ebff", "#7eb6ff", "#6b7f94", "#a8d4ff", "#4da3ff")),
    "mtg-dimir-ub": ("Dimir House", Palette("#090d14", "#9db7d8", "#3d5a80", "#566578", "#7aa2ff", "#5c7cfa")),
    "mtg-rakdos-br": ("Rakdos Carnival", Palette("#14080d", "#ffb3c1", "#c9184a", "#70404f", "#ff758f", "#ff4d6d")),
    "mtg-gruul-rg": ("Gruul Clans", Palette("#101408", "#d6f5a8", "#558b2f", "#5f6b4f", "#aed581", "#7cb342")),
    "mtg-selesnya-gw": ("Selesnya Conclave", Palette("#101610", "#e8f5ce", "#7cb342", "#66735a", "#c5e1a5", "#9ccc65")),
    "mtg-orzhov-wb": ("Orzhov Syndicate", Palette("#121016", "#efe2c4", "#bfa14a", "#756a58", "#d4c4a8", "#f0d78c")),
    "mtg-izzet-ur": ("Izzet League", Palette("#120d10", "#ffd6a5", "#ff6f59", "#7a5a52", "#ff9f1c", "#ff595e")),
    "mtg-golgari-bg": ("Golgari Swarm", Palette("#0b100c", "#b7d7a8", "#4a7c59", "#566456", "#81c784", "#6a994e")),
    "mtg-boros-rw": ("Boros Legion", Palette("#160f0c", "#ffe0b2", "#e65100", "#80624d", "#ffb74d", "#ff7043")),
    "mtg-simic-ug": ("Simic Combine", Palette("#081418", "#b2ebf2", "#00838f", "#4f6d70", "#4dd0e1", "#26c6da")),
    "mtg-bant-gwu": ("Bant Shard", Palette("#0d1418", "#dff7ff", "#56cfe1", "#607080", "#90e0ef", "#48cae4")),
    "mtg-esper-wub": ("Esper Shard", Palette("#0f1018", "#d9dcff", "#7b68ee", "#646880", "#b39ddb", "#9575cd")),
    "mtg-grixis-ubr": ("Grixis Shard", Palette("#100a12", "#f3c4ff", "#9d4edd", "#6a5870", "#e0aaff", "#c77dff")),
    "mtg-jund-brg": ("Jund Shard", Palette("#120c0a", "#ffc8a2", "#bc4749", "#73574d", "#f9844a", "#e85d04")),
    "mtg-naya-rgw": ("Naya Shard", Palette("#121008", "#ffe8a3", "#ee9b00", "#75664a", "#ffb703", "#fb8500")),
    "mtg-temur-urg": ("Temur Frontier", Palette("#081018", "#9fe7ff", "#219ebc", "#567080", "#8ecae6", "#023047")),
    "mtg-jeskai-urw": ("Jeskai Way", Palette("#10131a", "#fff1c1", "#4895ef", "#687080", "#a2d2ff", "#4361ee")),
    "mtg-sultai-gub": ("Sultai Brood", Palette("#08100e", "#b7e4c7", "#40916c", "#53655c", "#74c69d", "#2d6a4f")),
    "mtg-mardu-rwb": ("Mardu Horde", Palette("#140e0c", "#ffd6a5", "#d00000", "#735f52", "#ffba08", "#dc2f02")),
    "mtg-chrome-mox": ("Chrome Mox", Palette("#111111", "#f5f5f5", "#ffd700", "#777777", "#e0e0e0", "#ffc300")),
}


def build_theme(slug: str, title: str, palette: Palette) -> dict:
    return {
        "name": f"MTG {title}",
        "author": AUTHOR,
        "themes": [
            {
                "name": f"MTG {title}",
                "appearance": palette.appearance,
                "style": {
                    "background": palette.background,
                    "foreground": palette.foreground,
                    "text": palette.foreground,
                    "text.accent": palette.accent,
                    "text.muted": palette.muted,
                    "editor.background": palette.background,
                    "editor.foreground": palette.foreground,
                    "editor.active_line.background": "#ffffff0a",
                    "editor.line_number": palette.muted,
                    "editor.active_line_number": palette.accent,
                    "editor.gutter.background": palette.background,
                    "surface.background": "#ffffff08",
                    "element.background": "#ffffff10",
                    "element.hover": "#ffffff18",
                    "border": palette.muted,
                    "border.focused": palette.accent,
                    "tab_bar.background": palette.background,
                    "tab.active_background": "#ffffff08",
                    "tab.inactive_background": palette.background,
                    "panel.background": "#ffffff05",
                    "title_bar.background": palette.background,
                    "status_bar.background": palette.background,
                    "terminal.background": palette.background,
                    "terminal.foreground": palette.foreground,
                    "terminal.ansi.black": palette.background,
                    "terminal.ansi.red": "#ff5555",
                    "terminal.ansi.green": palette.string,
                    "terminal.ansi.yellow": palette.accent,
                    "terminal.ansi.blue": palette.keyword,
                    "terminal.ansi.magenta": palette.foreground,
                    "terminal.ansi.cyan": palette.accent,
                    "terminal.ansi.white": palette.foreground,
                    "syntax": {
                        "keyword": {"color": palette.keyword, "font_weight": 600},
                        "string": {"color": palette.string},
                        "comment": {"color": palette.muted, "font_style": "italic"},
                        "function": {"color": palette.foreground, "font_weight": 500},
                        "type": {"color": palette.accent},
                        "number": {"color": palette.accent},
                        "boolean": {"color": palette.accent},
                        "operator": {"color": palette.foreground},
                        "variable": {"color": palette.foreground},
                        "property": {"color": palette.foreground},
                        "constant": {"color": palette.keyword, "font_weight": 600},
                        "punctuation": {"color": palette.muted},
                        "tag": {"color": palette.accent},
                        "attribute": {"color": palette.foreground},
                        "constructor": {"color": palette.accent},
                        "embedded": {"color": palette.string},
                        "emphasis": {"font_style": "italic"},
                        "strong": {"font_weight": 700},
                        "link": {"color": palette.accent, "underline": True},
                    },
                },
            }
        ],
    }


def main() -> int:
    THEMES_DIR.mkdir(parents=True, exist_ok=True)
    for slug, (title, palette) in THEMES.items():
        path = THEMES_DIR / f"{slug}.json"
        path.write_text(json.dumps(build_theme(slug, title, palette), indent=2) + "\n")
        print(f"generated {path.name}")
    print(f"generated {len(THEMES)} themes")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
