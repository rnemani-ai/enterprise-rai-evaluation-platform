from difflib import SequenceMatcher

from core.base_evaluator import BaseEvaluator
from core.evaluation_request import EvaluationRequest
from core.evaluation_result import EvaluationResult
from core.risk_level import RiskLevel


class AnswerRelevanceEvaluator(BaseEvaluator):

    def __init__(self):
        super().__init__("Answer Relevance Evaluator")

    def evaluate(
        self,
        request: EvaluationRequest,
    ) -> EvaluationResult:

        similarity = SequenceMatcher(
            None,
            request.question.lower(),
            request.answer.lower(),
        ).ratio()

        passed = similarity >= 0.60

        if similarity >= 0.85:
            risk = RiskLevel.LOW
        elif similarity >= 0.60:
            risk = RiskLevel.MEDIUM
        else:
            risk = RiskLevel.HIGH

        explanation = (
            "The generated answer is relevant to the user's question."
            if passed
            else "The generated answer is not sufficiently relevant to the user's question."
        )

        return EvaluationResult(
            evaluator_name=self.name,
            score=round(similarity, 3),
            passed=passed,
            risk_level=risk,
            explanation=explanation,
            evidence=[
                f"Question/Answer Similarity = {round(similarity, 3)}"
            ],
            confidence=0.90,
            metadata={
                "algorithm": "SequenceMatcher",
                "evaluation_type": "Rule-Based",
                "evaluation_version": "V1",
            },
            execution_time_ms=1.0,
        )