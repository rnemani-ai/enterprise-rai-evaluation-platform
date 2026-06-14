from dataclasses import dataclass


@dataclass
class EvaluationResult:
    """
    Standard output format returned by all evaluators.
    """

    evaluator_name: str
    domain: str
    score: float
    risk_level: str
    explanation: str