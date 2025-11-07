#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
VENV_DIR="$ROOT_DIR/.venv"

if [ -f "$VENV_DIR/bin/activate" ]; then
  # shellcheck disable=SC1090
  source "$VENV_DIR/bin/activate"
fi

echo "Running unit tests..."
# Explicitly discover tests under the `tests` directory to avoid cases where
# discovery from the project root finds no tests (some environments or layouts
# can make discovery pick the wrong start dir). This mirrors how developers
# expect the suite to be run in CI and locally.
python -m unittest discover -s tests -p "test*.py" -v
