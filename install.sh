#!/usr/bin/env bash
# Install script for Linux (creates venv and installs dependencies)
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
VENV_DIR="$ROOT_DIR/.venv"

echo "Creating venv in $VENV_DIR..."
python3 -m venv "$VENV_DIR"
echo "Activating venv and upgrading pip..."
# shellcheck disable=SC1090
source "$VENV_DIR/bin/activate"
python -m pip install --upgrade pip
python -m pip install -r "$ROOT_DIR/requirements.txt"

echo "Install complete. To use the venv run:"
echo "  source $VENV_DIR/bin/activate"
echo "Then you can run tests: python -m unittest discover -v"
