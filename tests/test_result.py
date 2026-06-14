from evaluators.evaluation_result import EvaluationResult

result = EvaluationResult(
    evaluator_name="groundedness",
    domain="truthfulness",
    score=0.92,
    risk_level="low",
    explanation="Response supported by context."
)

print(result)