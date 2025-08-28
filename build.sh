#!/usr/bin/env bash
set -e

echo "=== Creating bin directory ==="
mkdir -p bin

echo "=== Downloading Piper binary ==="
curl -L https://github.com/rhasspy/piper/releases/latest/download/piper_linux_x86_64 \
  -o bin/piper

echo "=== Making Piper executable ==="
chmod +x bin/piper

echo "=== Installing Python dependencies ==="
pip install -r requirements.txt
