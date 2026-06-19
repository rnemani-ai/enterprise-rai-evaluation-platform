from benchmarks.dataset_loader import DatasetLoader
from benchmarks.benchmark_runner import BenchmarkRunner
from benchmarks.metrics import BenchmarkMetrics

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

    results = runner.run()

    metrics = BenchmarkMetrics.compute(results)

    print()
    print("=" * 70)
    print("Groundedness Benchmark Report")
    print("=" * 70)

    print(f"Dataset              : {dataset.name}")
    print(f"Dataset Size         : {metrics['total']}")
    print(f"Passed               : {metrics['passed']}")
    print(f"Failed               : {metrics['failed']}")
    print(f"Accuracy             : {metrics['accuracy']:.2%}")
    print(f"Average Score        : {metrics['average_score']:.3f}")

    print("\nRisk Distribution")

    for risk, count in metrics["risk_distribution"].items():
        print(f"{risk:<10}: {count}")

    print("=" * 70)


if __name__ == "__main__":
    main()