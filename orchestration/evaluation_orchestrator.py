from datetime import datetime

from core.evaluation_request import EvaluationRequest
from core.risk_engine import RiskEngine
from core.report import EnterpriseEvaluationReport
from core.report_generator import ReportGenerator

from evaluators.truthfulness.groundedness import GroundednessEvaluator
from evaluators.truthfulness.hallucination import HallucinationEvaluator
from evaluators.truthfulness.answer_relevance import AnswerRelevanceEvaluator
from evaluators.truthfulness.citation_accuracy import CitationAccuracyEvaluator

from evaluators.reliability.completeness import CompletenessEvaluator

from evaluators.safety.toxicity import ToxicityEvaluator
from evaluators.safety.pii import PIIEvaluator
from evaluators.safety.prompt_injection import PromptInjectionEvaluator

from evaluators.fairness.bias import BiasEvaluator


class EvaluationOrchestrator:

    def __init__(self):
        print("\nInitializing Enterprise Evaluation Pipeline...\n")

    def run(self):

        print("=" * 80)
        print("Enterprise Responsible AI Evaluation Platform")
        print("=" * 80)
        print("Application     : Document Intelligence Demo")
        print("Evaluation Type : Offline Evaluation")
        print(
            f"Execution Time  : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        )
        print("=" * 80)

        request = EvaluationRequest(
            question="Who wrote Harry Potter?",
            answer="The Harry Potter books were written by J.K. Rowling.",
            context="Harry Potter was written by J.K. Rowling.",
        )

        print("\nEvaluation Request")
        print("-" * 80)
        print(f"Question : {request.question}")
        print(f"Answer   : {request.answer}")
        print(f"Context  : {request.context}")

        truthfulness_evaluators = [
            GroundednessEvaluator(),
            HallucinationEvaluator(),
            AnswerRelevanceEvaluator(),
            CitationAccuracyEvaluator(),
        ]

        reliability_evaluators = [
            CompletenessEvaluator(),
        ]

        safety_evaluators = [
            ToxicityEvaluator(),
            PIIEvaluator(),
            PromptInjectionEvaluator(),
        ]

        fairness_evaluators = [
            BiasEvaluator(),
        ]

        evaluation_layers = {
            "Truthfulness": truthfulness_evaluators,
            "Reliability": reliability_evaluators,
            "Safety": safety_evaluators,
            "Fairness": fairness_evaluators,
        }

        print("\nLoading Evaluators...")
        print("Executing Evaluation Pipeline...")

        results = []

        for layer_name, evaluators in evaluation_layers.items():

            print()
            print("=" * 80)
            print(f"{layer_name} Evaluation")
            print("=" * 80)

            for evaluator in evaluators:

                result = evaluator.evaluate(request)

                results.append(result)

                status = "PASS" if result.passed else "FAIL"

                print(f"\n{result.evaluator_name}")
                print(f"Status       : {status}")
                print(f"Score        : {result.score:.3f}")
                print(f"Risk Level   : {result.risk_level.value}")
                print(f"Explanation  : {result.explanation}")

        passed = sum(result.passed for result in results)
        failed = len(results) - passed

        overall_score = RiskEngine.calculate_overall_score(
            results
        )

        overall_risk = RiskEngine.calculate_overall_risk(
            overall_score
        )

        recommendation = RiskEngine.recommendation(
            overall_risk
        )

        report = EnterpriseEvaluationReport(
            application_name="Document Intelligence Demo",
            evaluation_type="Offline Evaluation",
            total_evaluators=len(results),
            passed=passed,
            failed=failed,
            overall_score=overall_score,
            overall_risk=overall_risk,
            recommendation=recommendation,
            results=results,
        )

        ReportGenerator.generate_console_report(report)

        ReportGenerator.generate_markdown_report(report)