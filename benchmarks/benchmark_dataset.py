from dataclasses import dataclass
from typing import Any


@dataclass
class BenchmarkDataset:
    """
    Represents an evaluation benchmark dataset.
    """

    name: str

    records: list[dict[str, Any]]

    def __len__(self) -> int:
        return len(self.records)

    def __iter__(self):
        return iter(self.records)