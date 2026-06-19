from core.base_evaluator import BaseEvaluator
from core.evaluation_request import EvaluationRequest
from core.evaluation_result import EvaluationResult
from core.risk_level import RiskLevel


class CompletenessEvaluator(BaseEvaluator):

    def __init__(self):
        super().__init__("Completeness")

    def evaluate(self, request: EvaluationRequest) -> EvaluationResult:

        expected_items = request.metadata.get("expected_items", [])

        found_items = []

        for item in expected_items:
            if item.lower() in request.answer.lower():
                found_items.append(item)

        coverage = len(found_items) / len(expected_items)

        passed = coverage >= 0.80

        if coverage >= 0.90:
            risk = RiskLevel.LOW
            explanation = "Answer contains all required information."
        elif coverage >= 0.60:
            risk = RiskLevel.MEDIUM
            explanation = "Answer is partially complete."
        else:
            risk = RiskLevel.HIGH
            explanation = "Important information is missing."

        missing_items = [
            item for item in expected_items
            if item not in found_items
        ]

        return EvaluationResult(
            evaluator_name=self.name,
            score=round(coverage, 3),
            passed=passed,
            risk_level=risk,
            explanation=explanation,
            evidence=[
                f"Coverage = {len(found_items)}/{len(expected_items)}",
                f"Missing Items = {missing_items}"
            ],
            metadata={
                "evaluation_version": "V1",
                "algorithm": "Keyword Coverage",
                "evaluation_type": "Rule-Based",
            },
        )