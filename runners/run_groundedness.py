"""
run_groundedness.py

Runs the Groundedness benchmark.
"""

from benchmarks.benchmark_runner import BenchmarkRunner
from benchmarks.dataset_loader import DatasetLoader

from evaluators.truthfulness.groundedness import GroundednessEvaluator


def main():

    dataset = DatasetLoader.load(
        "datasets/sample/groundedness_dataset.json"
    )

    evaluator = GroundednessEvaluator()

    runner = BenchmarkRunner(
        evaluator=evaluator,
        dataset=dataset,
    )

    runner.run()


if __name__ == "__main__":
    main()