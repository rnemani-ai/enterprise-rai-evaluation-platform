from difflib import SequenceMatcher

from core.base_evaluator import BaseEvaluator
from core.evaluation_request import EvaluationRequest
from core.evaluation_result import EvaluationResult
from core.risk_level import RiskLevel


class CitationAccuracyEvaluator(BaseEvaluator):

    def __init__(self):
        super().__init__("Citation Accuracy")

    def evaluate(self, request: EvaluationRequest) -> EvaluationResult:

        expected_citation = request.metadata.get("expected_citation", "")

        similarity = SequenceMatcher(
            None,
            expected_citation.lower(),
            request.answer.lower(),
        ).ratio()

        passed = similarity >= 0.40

        if similarity >= 0.80:
            risk = RiskLevel.LOW
            explanation = "Expected citation is present in the answer."
        elif similarity >= 0.40:
            risk = RiskLevel.MEDIUM
            explanation = "Citation is partially matched."
        else:
            risk = RiskLevel.HIGH
            explanation = "Expected citation was not found."

        return EvaluationResult(
            evaluator_name=self.name,
            score=round(similarity, 3),
            passed=passed,
            risk_level=risk,
            explanation=explanation,
            evidence=[
                f"Citation Similarity = {round(similarity, 3)}"
            ],
            metadata={
                "evaluation_version": "V1",
                "algorithm": "SequenceMatcher",
                "evaluation_type": "Rule-Based",
            },
        )