"""
evaluation_result.py

Defines the standardized output returned by every evaluator
within the Enterprise Responsible AI Evaluation Platform.

Using a common result object ensures that all evaluators
produce consistent outputs, making aggregation, reporting,
and orchestration straightforward.
"""

from dataclasses import dataclass, field
from typing import Any

from core.risk_level import RiskLevel


@dataclass
class EvaluationResult:
    """
    Standard output returned by every evaluator.

    Attributes
    ----------
    evaluator_name : str
        Name of the evaluator.

    score : float
        Normalized evaluation score between 0 and 1.

    passed : bool
        Whether the evaluator passed its configured threshold.

    risk_level : RiskLevel
        Enterprise risk classification.

    explanation : str
        Human-readable explanation of the evaluation.

    evidence : list[str]
        Supporting evidence used during evaluation.

    confidence : float
        Confidence in the evaluation result (0–1).

    metadata : dict
        Additional evaluator-specific information.

    execution_time_ms : float
        Time taken to execute the evaluator.
    """

    evaluator_name: str

    score: float

    passed: bool

    risk_level: RiskLevel

    explanation: str

    evidence: list[str] = field(default_factory=list)

    confidence: float = 1.0

    metadata: dict[str, Any] = field(default_factory=dict)

    execution_time_ms: float = 0.0