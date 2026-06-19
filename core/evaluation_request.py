"""
evaluation_request.py

Defines the standard input object used by all evaluators in the
Enterprise Responsible AI Evaluation Platform.

Instead of passing multiple parameters to each evaluator, all
evaluation inputs are encapsulated within a single request object.

This design keeps the evaluator interface clean, extensible,
and consistent across the framework.
"""

from dataclasses import dataclass, field
from typing import Any


@dataclass
class EvaluationRequest:
    """
    Standard input for all evaluators.

    Attributes
    ----------
    question : str
        Original user prompt or question.

    answer : str
        AI-generated response.

    context : str, optional
        Supporting context used to generate the answer
        (e.g., retrieved RAG documents).

    metadata : dict
        Optional application-specific metadata.
    """

    question: str
    answer: str
    context: str | None = None
    metadata: dict[str, Any] = field(default_factory=dict)