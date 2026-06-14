from evaluators.base_evaluator import BaseEvaluator
from evaluators.evaluation_result import EvaluationResult


class GroundednessEvaluator(BaseEvaluator):
    """
    Evaluates whether a response is supported by the provided context.
    This is a placeholder implementation for Phase 1.
    """

    def evaluate(self, input_data):
        """
        Expected input format:

        {
            "question": "...",
            "context": "...",
            "response": "..."
        }
        """

        return EvaluationResult(
            evaluator_name="groundedness",
            domain="truthfulness",
            score=0.90,
            risk_level="low",
            explanation="Placeholder groundedness evaluation."
        )