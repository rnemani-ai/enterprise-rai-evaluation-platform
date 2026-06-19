"""
Groundedness Evaluator

Version:
    V1 - Rule-Based Baseline

Purpose:
    Evaluates whether an AI-generated answer is supported
    by the supplied context.
"""

from difflib import SequenceMatcher
import time

from core.base_evaluator import BaseEvaluator
from core.evaluation_request import EvaluationRequest
from core.evaluation_result import EvaluationResult
from core.risk_level import RiskLevel


class GroundednessEvaluator(BaseEvaluator):
    """
    Rule-based groundedness evaluator.

    This evaluator provides the baseline implementation for
    measuring whether a generated response is supported by
    the retrieved context.

    Future versions will evolve through the Evaluator
    Maturity Model.
    """

    def __init__(self):
        super().__init__("Groundedness Evaluator")

    def evaluate(
        self,
        request: EvaluationRequest,
    ) -> EvaluationResult:
        """
        Execute groundedness evaluation.
        """

        start_time = time.perf_counter()

        # Step 1
        self._validate_request(request)

        # Step 2
        score = self._compute_score(request)

        # Step 3
        risk = self._classify_risk(score)

        # Step 4
        result = self._build_result(
            score=score,
            risk=risk,
            execution_time_ms=(time.perf_counter() - start_time) * 1000,
        )

        return result

    def _validate_request(
        self,
        request: EvaluationRequest,
    ) -> None:
        """
        Validate the evaluation request before processing.
        """

        if not request.question.strip():
            raise ValueError("Question cannot be empty.")

        if not request.answer.strip():
            raise ValueError("Answer cannot be empty.")

        if not request.context.strip():
            raise ValueError("Context cannot be empty.")
        

    def _compute_score(
        self,
        request: EvaluationRequest,
    ) -> float:
        """
        Compute a groundedness score using lexical similarity
        between the generated answer and the retrieved context.

        Returns
        -------
        float
            Similarity score between 0.0 and 1.0.
        """

        similarity = SequenceMatcher(
            None,
            request.answer.lower(),
            request.context.lower(),
        ).ratio()

        return round(similarity, 3)

    def _classify_risk(
        self,
        score: float,
    ) -> RiskLevel:
        """
        Classify the groundedness score into an enterprise
        risk level.
        """

        if score >= 0.85:
            return RiskLevel.LOW

        if score >= 0.70:
            return RiskLevel.MEDIUM

        return RiskLevel.HIGH

    def _build_result(
        self,
        score: float,
        risk: RiskLevel,
        execution_time_ms: float,
    ) -> EvaluationResult:
        """
        Build the standardized evaluation result.
        """

        passed = score >= 0.70

        if risk == RiskLevel.LOW:
            explanation = (
                "The generated response is well supported by the "
                "retrieved context."
            )
        elif risk == RiskLevel.MEDIUM:
            explanation = (
                "The generated response is partially supported by the "
                "retrieved context and may require human review."
            )
        else:
            explanation = (
                "The generated response has limited support from the "
                "retrieved context and may contain unsupported claims."
            )

        return EvaluationResult(
            evaluator_name=self.name,
            score=score,
            passed=passed,
            risk_level=risk,
            explanation=explanation,
            evidence=[
                f"Groundedness similarity score: {score:.3f}"
            ],
            confidence=1.0,
            metadata={
                "evaluation_version": "V1",
                "algorithm": "SequenceMatcher",
                "evaluation_type": "Rule-Based",
            },
            execution_time_ms=round(execution_time_ms, 2),
        )