LLM-Assisted COREP Own Funds Prototype
Overview

This project presents a prototype of an LLM-assisted regulatory reporting system for COREP Own Funds reporting under the Prudential Regulation Authority (PRA) / Capital Requirements Regulation (CRR).

COREP reporting is highly manual and error-prone due to complex regulatory definitions and validation rules. This prototype demonstrates how LLM-style extraction, regulatory knowledge retrieval, validation logic, and explainable audit trails can be combined to support analysts in preparing accurate regulatory returns.

The focus of the prototype is regulatory validation and explainability, not full automation.

Scope of the Prototype

The scope is intentionally limited to ensure clarity and correctness.

Included:

COREP Own Funds template (C 01.00)

Capital components:

Common Equity Tier 1 (CET1)

Additional Tier 1 (AT1)

Tier 2

Total Capital

One COREP validation rule:

Total Capital = CET1 + AT1 + Tier 2

Explainable regulatory references (CRR Articles)

Out of scope:

Full PRA Rulebook ingestion

Real NLP text parsing

XBRL / taxonomy processing

Multiple validation rules

End-to-End Pipeline

The prototype follows the pipeline below:

Unstructured Input
        ↓
LLM-Assisted Extraction (Simulated)
        ↓
COREP Template Mapping
        ↓
Regulatory Rule Retrieval
        ↓
Validation Engine
        ↓
Explainable COREP Output & Audit Trail

Architecture Overview

app.py

Streamlit user interface

Simulated LLM extraction

Displays COREP output, validation results, and audit trail

mapping.py

Maps capital components to COREP cells

Retrieves relevant regulatory rules from a curated dataset

validator.py

Implements COREP validation logic for Own Funds consistency

rules.json

Curated mini regulatory dataset derived from CRR articles

Enables regulatory explainability without indexing the full rulebook

Regulatory Knowledge Dataset

Instead of indexing the entire PRA Rulebook, the prototype uses a manually curated mini regulatory dataset containing only the most relevant CRR provisions:

CRR Article 26 — CET1 definition

CRR Article 51 — AT1 definition

CRR Article 62 — Tier 2 definition

CRR Article 71 — Total Capital definition

This design choice improves transparency and reduces system complexity while remaining regulator-aligned.

Validation Logic

The prototype enforces the following COREP validation rule:

CRR Article 71

Total Capital = CET1 + AT1 + Tier 2


This rule is implemented in the validation engine and checked automatically during report generation.

Test Cases
Test Case 1 — Correct Reporting (PASS)

Input:

{
  "CET1": 5000000,
  "AT1": 1000000,
  "Tier2": 2000000,
  "TotalCapital": 8000000
}


Expected Outcome:

✔ Total Capital is valid (8000000).

Test Case 2 — Incorrect Reporting (FAIL)

Input:

{
  "CET1": 5000000,
  "AT1": 1000000,
  "Tier2": 2000000,
  "TotalCapital": 7500000
}


Expected Outcome:

Validation error: Expected 8000000, but reported 7500000.

Explainability & Audit Trail

For each reported capital component, the system:

Displays the mapped COREP cell

Cites the applicable CRR article

Provides a plain-English regulatory explanation

This ensures auditability and regulatory transparency, which are critical for supervisory reporting.

Assumptions and Limitations

LLM extraction from unstructured text is simulated to focus on regulatory logic.

Only one COREP validation rule is implemented.

The prototype is not intended for production use.

Future Enhancements

Potential future improvements include:

Real LLM-based text extraction

Vector search over full PRA Rulebook

Additional COREP validation rules

XBRL / taxonomy-aware reporting

Automated submission readiness checks

Conclusion

This prototype demonstrates how LLM-assisted systems can improve COREP reporting by combining structured validation logic with regulatory explainability. Even with limited scope, the system highlights clear opportunities to reduce reporting errors, improve auditability, and support regulatory compliance.
