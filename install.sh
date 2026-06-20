#!/usr/bin/env bash
set -euo pipefail
REPO_DIR="$(cd "$(dirname "$0")/.." && pwd)"
TARGET="$HOME/.config/zed/themes"
SOURCE="$REPO_DIR/themes"

if [[ ! -d "$SOURCE" ]]; then
  echo "Run: python3 scripts/generate_mtg_themes.py" >&2
  exit 1
fi

mkdir -p "$(dirname "$TARGET")"
if [[ -e "$TARGET" && ! -L "$TARGET" ]]; then
  mv "$TARGET" "${TARGET}.backup.$(date +%Y%m%dT%H%M%S)"
fi
ln -sfn "$SOURCE" "$TARGET"
echo "Linked $TARGET -> $SOURCE"
