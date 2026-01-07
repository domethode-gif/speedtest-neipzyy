$bin="$env:USERPROFILE\speedtest-neipzyy.exe"
$url="https://github.com/domethode-gif/speedtest-neipzyy/releases/latest/download/speedtest-neipzyy.exe"
Invoke-WebRequest $url -OutFile $bin
Write-Host "✅ Installed! Restart terminal & run: speedtest-neipzyy"
