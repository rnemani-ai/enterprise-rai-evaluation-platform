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

        return results