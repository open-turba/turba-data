from __future__ import annotations

import json
from importlib.resources import as_file, files
from pathlib import Path

import pandas as pd


def _load_registry() -> dict:
    registry_path = files("turba_data").joinpath("registry.json")
    return json.loads(registry_path.read_text(encoding="utf-8"))


def list_datasets() -> list[str]:
    registry = _load_registry()
    return [dataset["id"] for dataset in registry["datasets"]]



def load_dataset(dataset: str):
    registry = _load_registry()

    for item in registry["datasets"]:
        if dataset == item["id"]:
            resource = files("turba_data").joinpath(item["file"])
            with as_file(resource) as local_path:
                return pd.read_parquet(Path(local_path))

    available = ", ".join(list_datasets())
    raise ValueError(f"Unknown dataset: {dataset}. Available datasets: {available}")
