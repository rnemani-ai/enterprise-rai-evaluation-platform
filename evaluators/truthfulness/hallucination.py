from difflib import SequenceMatcher

from core.base_evaluator import BaseEvaluator
from core.evaluation_result import EvaluationResult
from core.risk_level import RiskLevel


class HallucinationEvaluator(BaseEvaluator):

    def __init__(self):
        super().__init__("Hallucination Evaluator")

    def evaluate(
        self,
        question: str,
        answer: str,
        context: str | None = None,
        **kwargs,
    ) -> EvaluationResult:

        if context is None:
            similarity = 0.0
        else:
            similarity = SequenceMatcher(
                None,
                context.lower(),
                answer.lower(),
            ).ratio()

        passed = similarity >= 0.75

        if similarity >= 0.90:
            risk = RiskLevel.LOW
        elif similarity >= 0.75:
            risk = RiskLevel.MEDIUM
        else:
            risk = RiskLevel.HIGH

        explanation = (
            "Answer is supported by the provided context."
            if passed
            else "Potential hallucination detected."
        )

        return EvaluationResult(
            evaluator_name=self.name,
            score=round(similarity, 3),
            passed=passed,
            risk_level=risk,
            explanation=explanation,
            evidence=[
                f"Similarity Score = {round(similarity,3)}"
            ],
            confidence=0.90,
            metadata={
                "evaluation_version": "V1",
                "algorithm": "SequenceMatcher",
                "evaluation_type": "Rule-Based",
            },
            execution_time_ms=1.0,
        )