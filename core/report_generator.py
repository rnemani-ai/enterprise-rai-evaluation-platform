"""
Enterprise Report Generator

Converts the EnterpriseEvaluationReport into a
human-readable report for the console or a Markdown file.
"""

from pathlib import Path

from core.report import EnterpriseEvaluationReport


class ReportGenerator:

    @staticmethod
    def generate_console_report(
        report: EnterpriseEvaluationReport,
    ) -> None:

        print()
        print("=" * 80)
        print("Enterprise Responsible AI Evaluation Report")
        print("=" * 80)

        print(f"Application        : {report.application_name}")
        print(f"Evaluation Type    : {report.evaluation_type}")

        print()
        print("-" * 80)
        print("Evaluation Summary")
        print("-" * 80)

        print(f"Total Evaluators   : {report.total_evaluators}")
        print(f"Passed             : {report.passed}")
        print(f"Failed             : {report.failed}")
        print(f"Overall Score      : {report.overall_score:.3f}")
        print(f"Overall Risk       : {report.overall_risk}")

        print()
        print("Recommendation")
        print("-" * 80)
        print(report.recommendation)

    @staticmethod
    def generate_markdown_report(
        report: EnterpriseEvaluationReport,
        output_path: str = "reports/evaluation_report.md",
    ) -> None:

        Path("reports").mkdir(exist_ok=True)

        lines = [
            "# Enterprise Responsible AI Evaluation Report",
            "",
            f"**Application:** {report.application_name}",
            f"**Evaluation Type:** {report.evaluation_type}",
            "",
            "## Summary",
            "",
            f"- Total Evaluators: {report.total_evaluators}",
            f"- Passed: {report.passed}",
            f"- Failed: {report.failed}",
            f"- Overall Score: {report.overall_score:.3f}",
            f"- Overall Risk: {report.overall_risk}",
            "",
            "## Recommendation",
            "",
            report.recommendation,
            "",
            "## Individual Evaluations",
            "",
        ]

        for result in report.results:

            lines.extend(
                [
                    f"### {result.evaluator_name}",
                    f"- Score: {result.score:.3f}",
                    f"- Passed: {result.passed}",
                    f"- Risk Level: {result.risk_level.value}",
                    f"- Explanation: {result.explanation}",
                    "",
                ]
            )

        Path(output_path).write_text("\n".join(lines))

        print(f"\nMarkdown report saved to {output_path}")