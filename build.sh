#!/bin/bash
set -e

echo "Downloading Piper..."
curl -L -o piper.tar.gz https://github.com/rhasspy/piper/releases/download/v1.2.0/piper_linux_x86_64.tar.gz
tar -xzf piper.tar.gz
rm piper.tar.gz

echo "Download voice model..."
mkdir -p voices
curl -L -o voices/en_US-amy-low.onnx https://github.com/rhasspy/piper/releases/download/v1.2.0/en_US-amy-low.onnx

chmod +x piper/piper
echo "Build complete."
