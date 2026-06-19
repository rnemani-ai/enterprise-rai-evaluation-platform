from dataclasses import dataclass, field

from core.evaluation_result import EvaluationResult


@dataclass
class EnterpriseEvaluationReport:
    """
    Represents the complete evaluation report generated after
    running all evaluators.

    This report aggregates individual evaluation results and
    provides an overall enterprise recommendation.
    """

    application_name: str

    evaluation_type: str

    total_evaluators: int

    passed: int

    failed: int

    overall_score: float

    overall_risk: str

    recommendation: str

    results: list[EvaluationResult] = field(default_factory=list)