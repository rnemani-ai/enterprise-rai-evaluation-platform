"""
run_groundedness.py

Runs the Groundedness Evaluator against a sample dataset.

Purpose:
    Demonstrate an end-to-end evaluation workflow using the
    Enterprise Responsible AI Evaluation Platform.
"""

import json
from pathlib import Path

from core.evaluation_request import EvaluationRequest
from evaluators.truthfulness.groundedness import GroundednessEvaluator


def main():

    dataset_path = Path("datasets/sample/groundedness_dataset.json")

    with open(dataset_path, "r", encoding="utf-8") as file:
        dataset = json.load(file)

    evaluator = GroundednessEvaluator()

    print("\n")
    print("=" * 70)
    print("Enterprise Responsible AI Evaluation Platform")
    print("Groundedness Evaluation - Version 1")
    print("=" * 70)

    for sample in dataset:

        request = EvaluationRequest(
            question=sample["question"],
            answer=sample["answer"],
            context=sample["context"],
        )

        result = evaluator.evaluate(request)

        print("\n")
        print("-" * 70)
        print(f"Example        : {sample['id']}")
        print(f"Question       : {sample['question']}")
        print(f"Expected Risk  : {sample['expected_risk']}")
        print("-" * 70)

        print(f"Score          : {result.score:.3f}")
        print(f"Risk Level     : {result.risk_level.value}")
        print(f"Passed         : {result.passed}")
        print(f"Confidence     : {result.confidence:.2f}")
        print(f"Execution Time : {result.execution_time_ms:.2f} ms")

        print("\nExplanation")
        print("-----------")
        print(result.explanation)

        print("\nEvidence")
        print("--------")
        for evidence in result.evidence:
            print(f"- {evidence}")

        print("\nMetadata")
        print("--------")
        for key, value in result.metadata.items():
            print(f"{key}: {value}")

    print("\n")
    print("=" * 70)
    print("Evaluation Completed")
    print("=" * 70)


if __name__ == "__main__":
    main()