import importlib.util

import turba_data as td


def test_list_datasets():
    datasets = td.list_datasets()
    assert datasets == ["esa_worldcereal_morocco_cereals_medium"]


def test_load_dataset_if_pyarrow_available():
    if importlib.util.find_spec("pyarrow") is None:
        return

    df = td.load_dataset("esa_worldcereal_morocco_cereals_medium")
    assert len(df) > 0
