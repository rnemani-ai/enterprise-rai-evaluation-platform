"""
base_evaluator.py

Defines the abstract base class for all evaluators in the
Enterprise Responsible AI Evaluation Platform.

Every evaluator should inherit from BaseEvaluator and implement
the evaluate() method.
"""

from abc import ABC, abstractmethod
from typing import Any

from core.evaluation_request import EvaluationRequest
from core.evaluation_result import EvaluationResult


class BaseEvaluator(ABC):
    """
    Abstract base class for all evaluators.

    Every evaluator in the platform should inherit from this class
    to ensure a consistent interface and standardized output.

    Examples
    --------
    GroundednessEvaluator

    HallucinationEvaluator

    BiasEvaluator

    ToxicityEvaluator
    """

    def __init__(self, name: str):
        """
        Initialize the evaluator.

        Parameters
        ----------
        name : str
            Human-readable evaluator name.
        """
        self.name = name

    @abstractmethod
    def evaluate(
        self,
        request: EvaluationRequest,
        **kwargs: Any,
    ) -> EvaluationResult:
        """
        Evaluate an AI-generated response.

        Parameters
        ----------
        request : EvaluationRequest
            Standardized evaluation request containing the
            question, generated answer, supporting context,
            application information, model details, and
            additional metadata.

        Returns
        -------
        EvaluationResult
            Standardized evaluation result produced by
            the evaluator.
        """
        raise NotImplementedError

    def __str__(self) -> str:
        return f"{self.__class__.__name__}(name='{self.name}')"
