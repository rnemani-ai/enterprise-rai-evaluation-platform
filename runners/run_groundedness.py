"""
run_groundedness.py

Runs the Groundedness benchmark.
"""

from benchmarks.benchmark_dataset import BenchmarkDataset
from benchmarks.benchmark_runner import BenchmarkRunner

from evaluators.truthfulness.groundedness import GroundednessEvaluator


def main():

    dataset = BenchmarkDataset(
        name="Groundedness Benchmark",
        dataset_path="datasets/sample/groundedness_dataset.json",
    )

    evaluator = GroundednessEvaluator()

    runner = BenchmarkRunner(
        evaluator=evaluator,
        dataset=dataset,
    )

    runner.run()


if __name__ == "__main__":
    main()