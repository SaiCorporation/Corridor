# DellFw
Custom Dell Device Firmware Manager for a select models of devices released by Dell.

> **NOTE**: This is a **simulation** project for demos/testing. It does not interact with hardware.

## Simulated Features
- Model detection via mocked SMBIOS
- Firmware catalog and semver handling
- Integrity checks (SHA-256)
- Dry-run "flash" with progress bar
- JSON & human-readable logs
- Pluggable transport backends (mocked WMI/EC/NVMe)

## CLI
```bash
pip install .
dellfw --help
dellfw list-models
dellfw detect
dellfw fetch --model XPS13-9300 --version 1.2.3
dellfw verify --model XPS13-9300 --version 1.2.3
dellfw flash --model XPS13-9300 --version 1.2.3 --dry-run
```
