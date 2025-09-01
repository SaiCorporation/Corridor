import argparse, json, sys, time, os
from rich.console import Console
from rich.table import Table
from rich.progress import Progress, BarColumn, TimeElapsedColumn, TimeRemainingColumn
from .catalog import load_catalog, get_model_versions, get_firmware_path
from .smbios import detect_model
from .integrity import sha256sum
from .core import logger, ensure_logs_dir

console = Console()

def cmd_list_models(args):
    catalog = load_catalog()
    table = Table(title="Supported Models (Simulated)")
    table.add_column("Model")
    table.add_column("Latest Version")
    for m, meta in catalog["models"].items():
        table.add_row(m, meta["latest"])
    console.print(table)

def cmd_detect(args):
    model = detect_model()
    console.print(f"[bold green]Detected model[/]: {model} (simulated)")

def cmd_fetch(args):
    catalog = load_catalog()
    path = get_firmware_path(args.model, args.version)
    if not os.path.exists(path):
        console.print(f"[red]Firmware not found[/]: {args.model} {args.version}")
        sys.exit(2)
    h = sha256sum(path)
    ensure_logs_dir()
    logger.info(f"FETCH {{'model': '{args.model}', 'version': '{args.version}', 'sha256': '{h}'}}")
    console.print(f"[green]Fetched[/] {path} (sha256: {h})")

def cmd_verify(args):
    path = get_firmware_path(args.model, args.version)
    h = sha256sum(path)
    console.print(f"[cyan]SHA-256[/]: {h}")

def cmd_flash(args):
    path = get_firmware_path(args.model, args.version)
    if args.dry_run:
        console.print(f"[yellow]Dry run[/]: would flash {args.model} {args.version} from {path}")
    else:
        console.print(f"[bold red]WARNING[/]: This is a simulation. No real flashing will occur.")
    with Progress("{task.description}", BarColumn(), "[progress.percentage]{task.percentage:>3.0f}%", TimeElapsedColumn(), TimeRemainingColumn()) as prog:
        t = prog.add_task("Flashing (simulated)", total=100)
        for _ in range(100):
            time.sleep(0.02)
            prog.advance(t, 1)
    console.print("[bold green]Done (simulated).[/]")
    ensure_logs_dir()
    logger.info(f"FLASH {{'model': '{args.model}', 'version': '{args.version}', 'dry_run': {args.dry_run}}}")

def main(argv=None):
    p = argparse.ArgumentParser(prog="dellfw", description="Custom Dell Device Firmware Manager (simulated)")
    sub = p.add_subparsers(dest="cmd", required=True)

    s1 = sub.add_parser("list-models", help="List supported models")
    s1.set_defaults(func=cmd_list_models)

    s2 = sub.add_parser("detect", help="Detect model (simulated)")
    s2.set_defaults(func=cmd_detect)

    s3 = sub.add_parser("fetch", help="Fetch firmware (simulated)")
    s3.add_argument("--model", required=True)
    s3.add_argument("--version", required=True)
    s3.set_defaults(func=cmd_fetch)

    s4 = sub.add_parser("verify", help="Verify firmware checksum")
    s4.add_argument("--model", required=True)
    s4.add_argument("--version", required=True)
    s4.set_defaults(func=cmd_verify)

    s5 = sub.add_parser("flash", help="Flash firmware (simulated)")
    s5.add_argument("--model", required=True)
    s5.add_argument("--version", required=True)
    s5.add_argument("--dry-run", action="store_true", help="Do not perform real actions")
    s5.set_defaults(func=cmd_flash)

    args = p.parse_args(argv)
    args.func(args)

if __name__ == "__main__":
    main()
