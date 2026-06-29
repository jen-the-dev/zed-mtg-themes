# MTG Zed Themes

Magic: The Gathering color identity and guild themes for [Zed](https://zed.dev).

## Themes (25)

- **Mono colors:** Plains White, Island Blue, Swamp Black, Mountain Red, Forest Green
- **Ravnica guilds:** Azorius, Dimir, Rakdos, Gruul, Selesnya, Orzhov, Izzet, Golgari, Boros, Simic
- **Alara shards:** Bant, Esper, Grixis, Jund, Naya
- **Extra:** Temur, Jeskai, Sultai, Mardu, Chrome Mox

## Install

```bash
git clone https://github.com/jen-the-dev/zed-mtg-themes.git
cd zed-mtg-themes
python3 scripts/generate_mtg_themes.py   # only needed if themes/ is missing
./install.sh
```

Restart Zed, then choose **Theme: Select Theme**.

## Cursor

Ported automatically in [cursor-themes](https://github.com/jen-the-dev/cursor-themes) as `Mtg - ...` themes.

## Regenerate

Edit palettes in `scripts/generate_mtg_themes.py`, then:

```bash
python3 scripts/generate_mtg_themes.py
```

## License

MIT

## Problem
Maintaining a large themed editor palette requires automation to keep generated files consistent.

## Solution
A generated Zed theme set based on Magic color identities with script-driven regeneration and installation workflow.

## Architecture Diagram
```mermaid
flowchart LR
  Palettes["MTG palette definitions"] --> Generator["Python theme generator"]
  Generator --> Themes["Zed theme JSON"]
  Themes --> Install["install.sh"]
```

## Tech Stack
- Python
- Shell scripts
- JSON theme definitions

## Setup Instructions
```bash
git clone https://github.com/jen-the-dev/zed-mtg-themes.git
cd zed-mtg-themes
python3 scripts/generate_mtg_themes.py
./install.sh
```

## Testing
- python3 scripts/generate_mtg_themes.py
- Manual theme validation in Zed

## Commit Convention
Use Conventional Commits for presentation clarity:
- `feat(scope): add new user-facing capability`
- `fix(scope): resolve functional defect`
- `test(scope): add or improve automated tests`
- `docs(readme): improve project documentation`

## Evidence Map
- `scripts/generate_mtg_themes.py`
- `themes/`
- `install.sh`
