from collections import Counter

from benchmarks.benchmark_dataset import BenchmarkDataset

from core.base_evaluator import BaseEvaluator
from core.evaluation_request import EvaluationRequest


class BenchmarkRunner:
    """
    Executes an evaluator against every record in a benchmark dataset.
    """

    def __init__(
        self,
        evaluator: BaseEvaluator,
        dataset: BenchmarkDataset,
    ):
        self.evaluator = evaluator
        self.dataset = dataset

    def _print_summary(self, results):

        passed = sum(result.passed for result in results)
        failed = len(results) - passed

        average_score = (
            sum(result.score for result in results) / len(results)
            if results
            else 0.0
        )

        pass_rate = (
            (passed / len(results)) * 100
            if results
            else 0.0
        )

        risk_counts = Counter(
            getattr(result.risk, "value", result.risk)
            for result in results
        )

        print("\n")
        print("=" * 80)
        print("Benchmark Summary")
        print("=" * 80)

        print(f"{'Dataset':25} {self.dataset.name}")
        print(f"{'Evaluator':25} {self.evaluator.name}")
        print(f"{'Total Records':25} {len(results)}")
        print(f"{'Passed':25} {passed}")
        print(f"{'Failed':25} {failed}")
        print(f"{'Pass Rate':25} {pass_rate:.1f}%")
        print(f"{'Average Score':25} {average_score:.3f}")

        print("\nRisk Distribution")
        print("-" * 80)

        for risk, count in sorted(risk_counts.items()):
            print(f"{risk:20} {count}")

        print("=" * 80)

    def run(self):

        print("=" * 80)
        print(f"Running Benchmark : {self.dataset.name}")
        print(f"Evaluator         : {self.evaluator.name}")
        print(f"Total Records     : {len(self.dataset)}")
        print("=" * 80)

        results = []

        for index, record in enumerate(self.dataset, start=1):

            request = EvaluationRequest(
                question=record.get("question", ""),
                answer=record.get("answer", ""),
                context=record.get("context", ""),
            )

            result = self.evaluator.evaluate(request)

            results.append(result)

            status = "PASS" if result.passed else "FAIL"

            print("\n" + "=" * 80)
            print(f"Record {index} / {len(self.dataset)}")
            print("=" * 80)

            print("\nQuestion")
            print("-" * 40)
            print(record.get("question", "N/A"))

            print("\nContext")
            print("-" * 40)
            print(record.get("context", "N/A"))

            print("\nAnswer")
            print("-" * 40)
            print(record.get("answer", "N/A"))

            print("\nExpected Risk")
            print("-" * 40)
            print(record.get("expected_risk", "N/A"))

            print("\nPredicted Risk")
            print("-" * 40)
            print(getattr(result.risk, "value", result.risk))

            print("\nScore")
            print("-" * 40)
            print(f"{result.score:.3f}")

            print("\nReason")
            print("-" * 40)
            print(result.reason or "N/A")

            print("\nResult")
            print("-" * 40)
            print(status)

        self._print_summary(results)

        return results