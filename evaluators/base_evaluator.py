from abc import ABC, abstractmethod


class BaseEvaluator(ABC):
    """
    Abstract base class for all Responsible AI evaluators.
    """

    @abstractmethod
    def evaluate(self, input_data):
        """
        Execute evaluation and return an EvaluationResult.
        """
        pass