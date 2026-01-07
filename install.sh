#!/bin/bash
set -e
BIN="/usr/local/bin/speedtest-neipzyy"
URL="https://github.com/USERNAME/speedtest-neipzyy/releases/latest/download/speedtest-neipzyy"

echo "Installing speedtest-neipzyy..."
sudo curl -L $URL -o $BIN
sudo chmod +x $BIN
echo "✅ Done! Run: speedtest-neipzyy"