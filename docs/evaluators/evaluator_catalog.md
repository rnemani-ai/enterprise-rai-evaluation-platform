# Evaluator Catalog

## Overview

The Enterprise Responsible AI Evaluation Platform is organized around reusable risk domains rather than application-specific evaluation logic.

This approach enables consistent evaluation across multiple Generative AI applications including:

* Retrieval-Augmented Generation (RAG) Assistants
* Customer Support Chatbots
* Document Intelligence Systems
* Knowledge Assistants
* Future Agentic AI Systems

Each evaluator is designed to assess a specific Responsible AI risk and produce standardized outputs that can be aggregated into an overall risk assessment.

---

# Truthfulness

Truthfulness evaluators assess whether generated responses are factually supported, relevant, and grounded in available information.

---

## Groundedness

### Business Risk

Generative AI systems may produce responses that are not supported by the provided source material.

This can result in misinformation, incorrect recommendations, reduced trust, and business risk.

### Evaluation Goal

Determine whether generated content is supported by the available context.

### Inputs

* User Question
* Retrieved Context
* Generated Response

### Outputs

* Groundedness Score
* Risk Classification
* Supporting Explanation

### Example Failure

Context:

```text
Refunds are allowed within 30 days.
```

Response:

```text
Refunds are allowed within 90 days.
```

---

## Hallucination Detection

### Business Risk

AI systems may fabricate facts, policies, entities, references, or recommendations that do not exist.

### Evaluation Goal

Identify unsupported or fabricated claims.

### Inputs

* Retrieved Context
* Generated Response

### Outputs

* Hallucination Score
* Unsupported Claim Count
* Risk Classification

### Example Failure

The response references information that does not appear in any available source material.

---

## Answer Relevance

### Business Risk

Responses may be technically correct but fail to answer the user's actual question.

### Evaluation Goal

Measure how effectively the response addresses the intended question.

### Inputs

* User Question
* Generated Response

### Outputs

* Relevance Score
* Risk Classification

### Example Failure

Question:

```text
What is the deductible amount?
```

Response:

```text
The policy was updated in 2024.
```

---

## Citation Accuracy

### Business Risk

AI systems may cite incorrect or unrelated sources.

### Evaluation Goal

Verify whether cited evidence supports the generated response.

### Inputs

* Retrieved Sources
* Generated Response
* Citations

### Outputs

* Citation Accuracy Score
* Evidence Validation Result

### Example Failure

Response cites Policy A while the supporting information actually exists in Policy B.

---

# Reliability

Reliability evaluators assess whether the system behaves consistently and predictably.

---

## Consistency

### Business Risk

Users may receive different answers to the same question, reducing trust and predictability.

### Evaluation Goal

Measure response stability across repeated executions.

### Inputs

* Prompt
* Multiple Responses

### Outputs

* Consistency Score
* Variability Assessment

### Example Failure

Run 1:

```text
Approved
```

Run 2:

```text
Rejected
```

for the same scenario.

---

## Robustness

### Business Risk

Small wording changes may produce significantly different behavior.

### Evaluation Goal

Measure resilience to prompt variations.

### Inputs

* Original Prompt
* Modified Prompts
* Generated Responses

### Outputs

* Robustness Score
* Prompt Sensitivity Analysis

### Example Failure

Three semantically equivalent prompts produce significantly different responses.

---

## Completeness

### Business Risk

Responses may omit critical information even when they are factually correct.

### Evaluation Goal

Determine whether required information is present.

### Inputs

* Question
* Expected Information
* Response

### Outputs

* Completeness Score
* Missing Information Analysis

### Example Failure

Question asks for all required onboarding documents.

Response provides only one required document.

---

# Fairness

Fairness evaluators assess whether AI systems produce equitable outcomes across demographic groups.

---

## Demographic Bias

### Business Risk

AI systems may generate different outcomes based on protected demographic attributes.

### Evaluation Goal

Detect disparate treatment across demographic groups.

### Inputs

* Paired Prompts
* Generated Responses

### Outputs

* Bias Score
* Group Comparison Analysis
* Risk Classification

### Example Failure

Equivalent candidates receive different hiring recommendations based solely on gender.

---

## Fairness Consistency

### Business Risk

Decision criteria may not be applied consistently across demographic groups.

### Evaluation Goal

Measure consistency of outcomes under controlled demographic changes.

### Inputs

* Scenario Variations
* Generated Responses

### Outputs

* Fairness Consistency Score
* Outcome Variability Assessment

### Example Failure

Equivalent customer profiles receive different decisions despite identical qualifications.

---

# Safety

Safety evaluators assess potentially harmful, toxic, or sensitive outputs.

---

## Toxicity Detection

### Business Risk

AI systems may generate offensive, abusive, discriminatory, or harmful content.

### Evaluation Goal

Identify toxic outputs.

### Inputs

* Prompt
* Generated Response

### Outputs

* Toxicity Score
* Risk Classification

### Example Failure

Response contains abusive language, hate speech, or harmful content.

---

## PII Leakage Detection

### Business Risk

Exposure of personally identifiable information (PII) may create privacy, legal, compliance, and reputational risks.

### Evaluation Goal

Identify sensitive information contained within generated outputs.

### Inputs

* Generated Response

### Outputs

* PII Detection Result
* Sensitive Entity Types
* Risk Classification

### Example Failure

Response contains:

* Social Security Numbers
* Phone Numbers
* Email Addresses
* Credit Card Information
* Account Numbers

---

# Evaluation Output Standard

All evaluators should produce standardized outputs to support aggregation and reporting.

Example:

```json
{
  "evaluator": "groundedness",
  "domain": "truthfulness",
  "score": 0.87,
  "risk_level": "low",
  "explanation": "Response is largely supported by provided context."
}
```

---

# Future Evaluators

Future releases may expand into additional Responsible AI domains.

## Security

* Prompt Injection Detection
* Jailbreak Detection
* Secrets Exposure Detection
* Data Leakage Analysis

## Agent Evaluation

* Tool Selection Accuracy
* Task Completion Validation
* Multi-Step Workflow Verification
* Agent Reliability Assessment

## Governance

* Risk Classification Framework
* Audit Reporting
* Approval Workflows
* Model Registry Integration

## Monitoring

* Continuous Evaluation
* Drift Detection
* Risk Trend Analysis
* Alerting and Monitoring
