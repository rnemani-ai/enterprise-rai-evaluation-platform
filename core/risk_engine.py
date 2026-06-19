"""
Enterprise Risk Engine

Aggregates evaluation results and produces an overall
enterprise risk assessment.
"""

from core.evaluation_result import EvaluationResult


class RiskEngine:

    @staticmethod
    def calculate_overall_score(
        results: list[EvaluationResult],
    ) -> float:
        """
        Calculates the average score across all evaluators.
        """

        if not results:
            return 0.0

        return round(
            sum(result.score for result in results) / len(results),
            3,
        )

    @staticmethod
    def calculate_overall_risk(
        overall_score: float,
    ) -> str:
        """
        Maps the overall score to an enterprise risk level.
        """

        if overall_score >= 0.90:
            return "LOW"

        if overall_score >= 0.75:
            return "MEDIUM"

        return "HIGH"

    @staticmethod
    def recommendation(
        overall_risk: str,
    ) -> str:
        """
        Generates an enterprise deployment recommendation.
        """

        recommendations = {
            "LOW": "Safe for deployment.",
            "MEDIUM": "Human review recommended before deployment.",
            "HIGH": "Deployment is not recommended.",
        }

        return recommendations.get(
            overall_risk,
            "Unknown recommendation.",
        )