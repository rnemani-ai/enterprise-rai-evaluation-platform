import json

from core.evaluation_request import EvaluationRequest
from evaluators.safety.bias import BiasEvaluator


def main():

    with open("datasets/sample/bias_dataset.json", "r") as f:
        dataset = json.load(f)

    evaluator = BiasEvaluator()

    print("=" * 70)
    print("Bias Evaluation")
    print("=" * 70)

    for sample in dataset:

        request = EvaluationRequest(
            question=sample["question"],
            answer=sample["answer"],
        )

        result = evaluator.evaluate(request)

        print(f"\nSample #{sample['id']}")
        print("-" * 70)
        print(f"Question        : {sample['question']}")
        print(f"Answer          : {sample['answer']}")
        print(f"Expected Risk   : {sample['expected_risk']}")
        print(f"Score           : {result.score}")
        print(f"Passed          : {result.passed}")
        print(f"Risk Level      : {result.risk_level.value}")
        print(f"Explanation     : {result.explanation}")

        print("\nEvidence")
        for evidence in result.evidence:
            print(f"  • {evidence}")

        print("\nMetadata")
        for key, value in result.metadata.items():
            print(f"  {key}: {value}")

    print("\n" + "=" * 70)
    print("Bias Evaluation Complete")
    print("=" * 70)


if __name__ == "__main__":
    main()