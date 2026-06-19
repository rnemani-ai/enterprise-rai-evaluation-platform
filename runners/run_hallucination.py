import json

from evaluators.truthfulness.hallucination import HallucinationEvaluator


def main():

    evaluator = HallucinationEvaluator()

    with open(
        "datasets/sample/hallucination_dataset.json",
        "r",
        encoding="utf-8",
    ) as f:
        dataset = json.load(f)

    print("=" * 70)
    print("Hallucination Evaluation")
    print("=" * 70)

    for sample in dataset:

        result = evaluator.evaluate(
            question=sample["question"],
            context=sample["context"],
            answer=sample["answer"],
        )

        print(f"\nSample #{sample['id']}")
        print("-" * 70)
        print(f"Question       : {sample['question']}")
        print(f"Answer         : {sample['answer']}")
        print(f"Expected Risk  : {sample['expected_risk']}")
        print(f"Score          : {result.score}")
        print(f"Passed         : {result.passed}")
        print(f"Risk Level     : {result.risk_level.value}")
        print(f"Explanation    : {result.explanation}")

        print("\nEvidence")
        for evidence in result.evidence:
            print(f"  • {evidence}")

        print("\nMetadata")
        for key, value in result.metadata.items():
            print(f"  {key}: {value}")

    print("\n" + "=" * 70)
    print("Hallucination Evaluation Complete")
    print("=" * 70)


if __name__ == "__main__":
    main()