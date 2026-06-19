import json

from evaluators.truthfulness.answer_relevance import AnswerRelevanceEvaluator


def main():

    evaluator = AnswerRelevanceEvaluator()

    with open(
        "datasets/sample/answer_relevance_dataset.json",
        "r",
        encoding="utf-8",
    ) as f:
        dataset = json.load(f)

    print("=" * 70)
    print("Answer Relevance Evaluation")
    print("=" * 70)

    for sample in dataset:

        result = evaluator.evaluate(
            question=sample["question"],
            answer=sample["answer"],
            context=sample["context"],
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
    print("Answer Relevance Evaluation Complete")
    print("=" * 70)


if __name__ == "__main__":
    main()