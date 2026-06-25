"""
Groundedness Evaluator

Version:
    V1 - Rule-Based Baseline

Purpose:
    Evaluates whether an AI-generated answer is supported
    by the supplied context.
"""

from difflib import SequenceMatcher
import re
import time

from core.base_evaluator import BaseEvaluator
from core.evaluation_request import EvaluationRequest
from core.evaluation_result import EvaluationResult
from core.risk_level import RiskLevel


class GroundednessEvaluator(BaseEvaluator):
    """
    Rule-based groundedness evaluator.

    V1 combines:
    - Lexical similarity
    - Keyword overlap
    - Missing context detection

    Future versions may replace the scoring logic with
    embedding similarity or LLM-as-a-Judge without changing
    the evaluator interface.
    """

    def __init__(self):
        super().__init__("Groundedness Evaluator")

    def evaluate(
        self,
        request: EvaluationRequest,
    ) -> EvaluationResult:

        start_time = time.perf_counter()

        self._validate_request(request)

        score = self._compute_score(request)

        risk = self._classify_risk(score)

        execution_time = (
            time.perf_counter() - start_time
        ) * 1000

        return self._build_result(
            score=score,
            risk=risk,
            execution_time_ms=execution_time,
        )

    def _validate_request(
        self,
        request: EvaluationRequest,
    ) -> None:

        if not request.question.strip():
            raise ValueError("Question cannot be empty.")

        if not request.answer.strip():
            raise ValueError("Answer cannot be empty.")

    def _compute_score(
        self,
        request: EvaluationRequest,
    ) -> float:

        context = (request.context or "").strip()

        if not context:

            answer = request.answer.lower()

            refusal_phrases = [
                "don't know",
                "do not know",
                "not enough information",
                "insufficient information",
                "cannot answer",
                "unable to answer",
                "provided context",
            ]

            if any(
                phrase in answer
                for phrase in refusal_phrases
            ):
                return 1.0

            return 0.0

        lexical_score = SequenceMatcher(
            None,
            request.answer.lower(),
            context.lower(),
        ).ratio()

        answer_words = set(
            re.findall(r"\w+", request.answer.lower())
        )

        context_words = set(
            re.findall(r"\w+", context.lower())
        )

        if answer_words:
            keyword_score = (
                len(answer_words & context_words)
                / len(answer_words)
            )
        else:
            keyword_score = 0.0

        score = (
            lexical_score * 0.7
            + keyword_score * 0.3
        )

        return round(score, 3)

    def _classify_risk(
        self,
        score: float,
    ) -> RiskLevel:

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

        passed = score >= 0.70

        if risk == RiskLevel.LOW:
            explanation = (
                "The generated answer is strongly supported "
                "by the provided context."
            )

        elif risk == RiskLevel.MEDIUM:
            explanation = (
                "The generated answer is partially supported "
                "by the provided context."
            )

        else:
            explanation = (
                "The generated answer is weakly supported "
                "or contains unsupported information."
            )

        return EvaluationResult(
            evaluator_name=self.name,
            score=score,
            passed=passed,
            risk_level=risk,
            explanation=explanation,
            evidence=[
                f"Groundedness Score = {score:.3f}"
            ],
            confidence=1.0,
            metadata={
                "evaluation_version": "V1",
                "algorithm": "Hybrid Rule-Based",
                "components": [
                    "Lexical Similarity",
                    "Keyword Overlap",
                ],
            },
            execution_time_ms=round(
                execution_time_ms,
                2,
            ),
        )