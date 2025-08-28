#!/usr/bin/env bash
set -e

echo "Downloading Piper..."
curl -L -o piper https://github.com/rhasspy/piper/releases/download/v0.0.2/piper_linux_x86_64
chmod +x piper
mv piper /usr/local/bin/piper

echo "Build complete"
