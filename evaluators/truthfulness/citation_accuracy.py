from difflib import SequenceMatcher

from core.base_evaluator import BaseEvaluator
from core.evaluation_request import EvaluationRequest
from core.evaluation_result import EvaluationResult
from core.risk_level import RiskLevel


class CitationAccuracyEvaluator(BaseEvaluator):

    def __init__(self):
        super().__init__("Citation Accuracy Evaluator")

    def evaluate(
        self,
        request: EvaluationRequest,
    ) -> EvaluationResult:

        context = request.context or ""
        answer = request.answer

        similarity = SequenceMatcher(
            None,
            context.lower(),
            answer.lower(),
        ).ratio()

        passed = similarity >= 0.70

        if similarity >= 0.90:
            risk = RiskLevel.LOW
        elif similarity >= 0.70:
            risk = RiskLevel.MEDIUM
        else:
            risk = RiskLevel.HIGH

        explanation = (
            "The generated response appears to be supported by the provided context."
            if passed
            else "The response may contain unsupported or incorrectly cited information."
        )

        return EvaluationResult(
            evaluator_name=self.name,
            score=round(similarity, 3),
            passed=passed,
            risk_level=risk,
            explanation=explanation,
            evidence=[
                f"Context Similarity = {round(similarity, 3)}"
            ],
            confidence=0.90,
            metadata={
                "algorithm": "SequenceMatcher",
                "evaluation_type": "Rule-Based",
                "evaluation_version": "V1",
            },
            execution_time_ms=1.0,
        )