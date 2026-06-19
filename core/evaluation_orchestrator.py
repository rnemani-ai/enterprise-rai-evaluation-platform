"""
evaluation_orchestrator.py

Coordinates the execution of one or more evaluators within the
Enterprise Responsible AI Evaluation Platform.

The orchestrator provides a single entry point for running
multiple evaluators against the same evaluation request and
collecting their standardized results.
"""

from typing import List

from core.base_evaluator import BaseEvaluator
from core.evaluation_request import EvaluationRequest
from core.evaluation_result import EvaluationResult


class EvaluationOrchestrator:
    """
    Coordinates execution of multiple evaluators.

    The orchestrator does not contain evaluation logic itself.
    Its responsibility is to invoke registered evaluators and
    collect their results.
    """

    def __init__(self):

        self.evaluators: List[BaseEvaluator] = []

    def register(self, evaluator: BaseEvaluator) -> None:
        """
        Register an evaluator with the orchestrator.
        """
        self.evaluators.append(evaluator)

    def evaluate(
        self,
        request: EvaluationRequest,
    ) -> List[EvaluationResult]:
        """
        Execute all registered evaluators.
        """

        results = []

        for evaluator in self.evaluators:
            result = evaluator.evaluate(request)
            results.append(result)

        return results