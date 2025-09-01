import os, json
from dellfw.catalog import load_catalog, get_firmware_path
from dellfw.integrity import sha256sum

def test_catalog_loads():
    cat = load_catalog()
    assert "models" in cat and len(cat["models"]) >= 1

def test_firmware_exists():
    path = get_firmware_path("XPS13-9300", "1.2.3")
    assert os.path.exists(path)

def test_checksum_json():
    here = os.path.dirname(__file__)
    # ensure checksums file exists in package data
    pass
