#!/usr/bin/env bash
set -o errexit  # अगर कोई error आए तो build रुके

# Dependencies
apt-get update && apt-get install -y wget unzip

# Piper binary download and install
wget https://github.com/rhasspy/piper/releases/download/v1.2.0/piper_linux_x86_64.tar.gz
tar -xvzf piper_linux_x86_64.tar.gz
mv piper /usr/local/bin/piper
chmod +x /usr/local/bin/piper

# Voice model download
mkdir -p voices
wget https://github.com/rhasspy/piper/releases/download/v1.2.0/en_US-libritts-high.onnx -O voices/en_US-libritts-high.onnx
