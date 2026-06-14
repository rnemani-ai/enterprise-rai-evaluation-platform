from typing import List

from evaluators.base_evaluator import BaseEvaluator


class EvaluationOrchestrator:
    """
    Responsible for executing all registered evaluators
    and collecting their results.
    """

    def __init__(self, evaluators: List[BaseEvaluator]):
        self.evaluators = evaluators

    def run(self, input_data):
        """
        Execute all evaluators and return results.
        """

        results = []

        for evaluator in self.evaluators:
            result = evaluator.evaluate(input_data)
            results.append(result)

        return results