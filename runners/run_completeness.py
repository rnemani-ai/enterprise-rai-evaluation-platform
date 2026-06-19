import json

from core.evaluation_request import EvaluationRequest
from evaluators.reliability.completeness import CompletenessEvaluator


def main():

    with open("datasets/sample/completeness_dataset.json", "r") as f:
        dataset = json.load(f)

    evaluator = CompletenessEvaluator()

    print("=" * 70)
    print("Completeness Evaluation")
    print("=" * 70)

    for sample in dataset:

        request = EvaluationRequest(
            question=sample["question"],
            answer=sample["answer"],
            context=sample["context"],
            metadata={
                "expected_items": sample["expected_items"]
            },
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
    print("Completeness Evaluation Complete")
    print("=" * 70)


if __name__ == "__main__":
    main()