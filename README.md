<h1 align="center">turba-data</h1>

<p align="center">
  <strong>Dataset package for site-specific NPK fertilizer recommendations in Morocco.</a></strong>
</p>

<p align="center">
  <!-- PyPI version -->
  <a href="https://pypi.org/project/turba-data/">
    <img src="https://img.shields.io/pypi/v/turba-data.svg?label=PyPI" alt="PyPI" />
  </a>

  <!-- Security -->
  <a href="https://badge.socket.dev/pypi/package/turba-data/0.1.0?artifact_id=tar-gz">
    <img src="https://badge.socket.dev/pypi/package/turba-data/0.1.0?artifact_id=tar-gz" alt="Socket Security" />
  </a>

  <!-- Downloads -->
  <a href="https://pepy.tech/project/turba-data">
    <img src="https://static.pepy.tech/badge/turba-data" alt="Downloads" />
  </a>

  <!-- License -->
  <a href="LICENSE">
    <img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License: MIT" />
  </a>
</p>

`turba-data` is the data package of the turba ecosystem. It provides a simple way to discover the datasets currently available and load them directly into Python. Future work will expand the catalog with additional datasets covering more crops, sources, and regions, add more notebooks for analysis and comparison, and introduce hosted remote downloads as the collection grows.

## Install

```bash
pip install turba-data
```

This also pulls:
- `pandas`
- `pyarrow`

## Quick start

```python
import turba_data as td

print(td.list_datasets())

df = td.load_dataset("esa_worldcereal_morocco_cereals_medium")
print(df.head())
```

Users can convert parquet to CSV themselves after loading:

```python
import turba_data as td

df = td.load_dataset("esa_worldcereal_morocco_cereals_medium")
df.to_csv("esa_worldcereal_morocco_cereals_medium.csv", index=False)
```

## First release dataset

Current snapshot for the first packaged dataset:
- dataset id: `esa_worldcereal_morocco_cereals_medium`
- file: `esa_worldcereal_morocco_cereals_medium.parquet`
- rows: 132,017
- columns: 22
- unique sites: 44,096
- regions: 10
- provinces: 66
- communes: 1,149

## Repository structure

```text
turba-data/
├── src/
│   └── turba_data/
│       ├── __init__.py
│       ├── core.py
│       ├── registry.json
│       └── datasets/
│           └── esa_worldcereal_morocco_cereals_medium.parquet
├── tests/
│   └── test_api.py
├── LICENSE
├── pyproject.toml
└── README.md
```
