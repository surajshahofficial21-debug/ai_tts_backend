#!/bin/bash
set -e

# Fetch latest Piper release dynamically
LATEST_URL=$(curl -s https://api.github.com/repos/rhasspy/piper/releases/latest \
  | grep browser_download_url \
  | grep linux_x86_64.tar.gz \
  | cut -d '"' -f 4)

echo "Downloading Piper from: $LATEST_URL"
curl -L -o piper.tar.gz "$LATEST_URL"
tar -xvzf piper.tar.gz
chmod +x piper
