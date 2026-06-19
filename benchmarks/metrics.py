class BenchmarkMetrics:
    """
    Computes benchmark statistics for evaluator results.
    """

    @staticmethod
    def compute(results: list[dict]) -> dict:

        total = len(results)

        if total == 0:
            return {}

        passed = sum(result["passed"] for result in results)
        failed = total - passed

        average_score = (
            sum(result["score"] for result in results) / total
        )

        risk_distribution = {
            "LOW": 0,
            "MEDIUM": 0,
            "HIGH": 0,
        }

        for result in results:
            risk_distribution[result["actual_risk"]] += 1

        accuracy = passed / total

        return {
            "total": total,
            "passed": passed,
            "failed": failed,
            "accuracy": accuracy,
            "average_score": average_score,
            "risk_distribution": risk_distribution,
        }