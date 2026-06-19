from benchmarks.benchmark_dataset import BenchmarkDataset

from core.base_evaluator import BaseEvaluator
from core.evaluation_request import EvaluationRequest


class BenchmarkRunner:

    def __init__(
        self,
        evaluator: BaseEvaluator,
        dataset: BenchmarkDataset,
    ):
        self.evaluator = evaluator
        self.dataset = dataset

    def run(self):

        results = []

        print("\n")
        print("=" * 70)
        print(f"Running Benchmark : {self.dataset.name}")
        print(f"Evaluator          : {self.evaluator.name}")
        print("=" * 70)

        for record in self.dataset:

            request = EvaluationRequest(
                question=record.get("question", ""),
                answer=record.get("answer", ""),
                context=record.get("context", "")
            )

            result = self.evaluator.evaluate(request)

            results.append(
                {
                    "id": record.get("id"),
                    "scenario": record.get("scenario", ""),
                    "expected_risk": record.get("expected_risk"),
                    "actual_risk": result.risk_level.value,
                    "score": result.score,
                    "passed": result.passed,
                }
            )

        self._print_summary(results)

        return results

    def _print_summary(self, results):

        total = len(results)

        passed = sum(r["passed"] for r in results)

        failed = total - passed

        accuracy = (passed / total * 100) if total else 0

        average_score = (
            sum(r["score"] for r in results) / total
            if total
            else 0
        )

        print("\n")
        print("=" * 70)
        print("Benchmark Summary")
        print("=" * 70)
        print(f"Dataset Size  : {total}")
        print(f"Passed        : {passed}")
        print(f"Failed        : {failed}")
        print(f"Accuracy      : {accuracy:.1f}%")
        print(f"Average Score : {average_score:.3f}")

        print("\nFailed Cases")
        print("-" * 70)

        failures = [r for r in results if not r["passed"]]

        if not failures:
            print("None")
        else:
            for item in failures:

                print(
                    f"ID {item['id']} | "
                    f"Expected: {item['expected_risk']} | "
                    f"Actual: {item['actual_risk']} | "
                    f"Score: {item['score']:.3f}"
                )

        print("=" * 70)