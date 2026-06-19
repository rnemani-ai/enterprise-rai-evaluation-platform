import json
from pathlib import Path

from benchmarks.benchmark_dataset import BenchmarkDataset


class DatasetLoader:
    """
    Loads evaluation benchmark datasets from JSON files.
    """

    @staticmethod
    def load(path: str | Path) -> BenchmarkDataset:

        dataset_path = Path(path)

        if not dataset_path.exists():
            raise FileNotFoundError(
                f"Dataset not found: {dataset_path}"
            )

        with open(dataset_path, "r", encoding="utf-8") as file:
            records = json.load(file)

        return BenchmarkDataset(
            name=dataset_path.stem,
            records=records,
        )