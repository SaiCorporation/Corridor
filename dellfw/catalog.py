import json, os
from importlib import resources

def _data_path(name: str) -> str:
    return resources.files("dellfw").joinpath("firmware").joinpath(name)

def load_catalog():
    with resources.as_file(_data_path("catalog.json")) as p:
        with open(p, "r", encoding="utf-8") as f:
            return json.load(f)

def get_model_versions(model: str):
    cat = load_catalog()
    return cat["models"].get(model, {}).get("versions", [])

def get_firmware_path(model: str, version: str) -> str:
    fname = f"{model}-{version}.bin"
    with resources.as_file(_data_path(fname)) as p:
        return str(p)
