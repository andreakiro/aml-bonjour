import pickle
import gzip
from typing import Dict, List

from kedro.io import AbstractDataSet
from pathlib import Path

class ZippedPickleDataSet(AbstractDataSet):
    """
    Dataset reader for zipped pickle files.
    """

    def __init__(self, filepath):
        self._filepath = filepath

    def _load(self) -> List[Dict]:
        with gzip.open(self._filepath, 'rb') as f:
            loaded_object = pickle.load(f)
            return loaded_object

    def _save(self, obj: List[Dict]) -> None:
        with gzip.open(self._filepath, 'wb') as f:
            pickle.dump(obj, f, 2)

    def _exists(self) -> bool:
        return Path(self._filepath.as_posix()).exists()

    def _describe(self):
        return
