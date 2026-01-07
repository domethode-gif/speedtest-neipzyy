import argparse
import json
import speedtest
from rich.console import Console
from rich.table import Table

console = Console()

parser = argparse.ArgumentParser(
    prog="speedtest-neipzyy",
    description="⚡ Speedtest CLI by Neipzyy"
)
parser.add_argument("--json", action="store_true", help="Output JSON")
parser.add_argument("--simple", action="store_true", help="Simple output")
args = parser.parse_args()

console.print("[bold cyan]⚡ SPEEDTEST - NEIPZYY[/bold cyan]\n")

st = speedtest.Speedtest()
st.get_best_server()

download = st.download()
upload = st.upload()
ping = st.results.ping

result = {
    "ping_ms": round(ping, 2),
    "download_mbps": round(download / 1_000_000, 2),
    "upload_mbps": round(upload / 1_000_000, 2)
}

if args.json:
    print(json.dumps(result, indent=2))
elif args.simple:
    print(f"{result['download_mbps']} Mbps ↓ | {result['upload_mbps']} Mbps ↑ | {result['ping_ms']} ms")
else:
    table = Table(title="Hasil Speedtest")
    table.add_column("Metric", style="cyan")
    table.add_column("Value", style="green")
    for k, v in result.items():
        table.add_row(k, str(v))
    console.print(table)