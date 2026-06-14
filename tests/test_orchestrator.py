from evaluators.truthfulness.groundedness_evaluator import (
    GroundednessEvaluator,
)
from orchestration.evaluation_orchestrator import (
    EvaluationOrchestrator,
)


sample_input = {
    "question": "What is the refund policy?",
    "context": "Refunds are allowed within 30 days.",
    "response": "Refunds are allowed within 30 days.",
}


evaluators = [
    GroundednessEvaluator()
]

orchestrator = EvaluationOrchestrator(evaluators)

results = orchestrator.run(sample_input)

for result in results:
    print(result)