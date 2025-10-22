#!/bin/bash
# Pfad zu deinem Skript im Repo
SCRIPT_PATH="$(pwd)/mensa.py"

# Zielpfad
TARGET="/usr/local/bin/mensa"

# Kopieren und ausführbar machen
sudo cp "$SCRIPT_PATH" "$TARGET"
sudo chmod +x "$TARGET"

echo "Mensa installiert! Du kannst es jetzt mit 'mensa' ausführen."
