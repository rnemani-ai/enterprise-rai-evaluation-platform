# Evaluation Workflow

## Workflow

```text
Input Dataset
      |
      V

Evaluation Orchestrator
      |
      V

Evaluator Execution
      |
      V

Individual Risk Scores
      |
      V

Risk Aggregation
      |
      V

Evaluation Report
      |
      V

Human Review
```

## Workflow Description

1. Evaluation data is submitted to the framework.
2. The orchestrator determines which evaluators should run.
3. Each evaluator produces a score and supporting rationale.
4. Results are aggregated into domain-level assessments.
5. A final evaluation report is generated.
6. Human reviewers interpret results and determine appropriate actions.
