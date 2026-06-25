"""
evaluation_result.py

Defines the standardized output returned by every evaluator
within the Enterprise Responsible AI Evaluation Platform.
"""

from dataclasses import dataclass, field
from typing import Any

from core.risk_level import RiskLevel


@dataclass
class EvaluationResult:
    """
    Standard result returned by every evaluator.
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

    def __str__(self) -> str:
        return (
            f"{self.evaluator_name} | "
            f"Score={self.score:.3f} | "
            f"Risk={self.risk_level.value} | "
            f"Passed={self.passed}"
        )