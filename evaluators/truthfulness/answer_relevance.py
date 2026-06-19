from difflib import SequenceMatcher

from core.base_evaluator import BaseEvaluator
from core.evaluation_result import EvaluationResult
from core.risk_level import RiskLevel


class AnswerRelevanceEvaluator(BaseEvaluator):

    def __init__(self):
        super().__init__("Answer Relevance Evaluator")

    def evaluate(
        self,
        question: str,
        answer: str,
        context: str | None = None,
        **kwargs,
    ) -> EvaluationResult:

        similarity = SequenceMatcher(
            None,
            question.lower(),
            answer.lower(),
        ).ratio()

        passed = similarity >= 0.40

        if similarity >= 0.70:
            risk = RiskLevel.LOW
        elif similarity >= 0.40:
            risk = RiskLevel.MEDIUM
        else:
            risk = RiskLevel.HIGH

        explanation = (
            "Answer is relevant to the question."
            if passed
            else "Answer is not relevant to the user's question."
        )

        return EvaluationResult(
            evaluator_name=self.name,
            score=round(similarity, 3),
            passed=passed,
            risk_level=risk,
            explanation=explanation,
            evidence=[
                f"Question-Answer Similarity = {round(similarity,3)}"
            ],
            confidence=0.90,
            metadata={
                "evaluation_version": "V1",
                "algorithm": "SequenceMatcher",
                "evaluation_type": "Rule-Based",
            },
            execution_time_ms=1.0,
        )