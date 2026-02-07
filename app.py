import streamlit as st
import json
from mapping import COREP_MAPPING, get_rule_by_reference
from validator import validate_total_capital

# -------------------------------------------------
# Load regulatory rules (Mini PRA Dataset)
# -------------------------------------------------
with open("rules.json") as f:
    rules = json.load(f)

# -------------------------------------------------
# Streamlit UI
# -------------------------------------------------
st.title("LLM-Assisted COREP Own Funds Prototype")
st.caption("Prototype demonstrating regulatory explainability and validation")

user_input = st.text_area(
    "Enter capital information (unstructured input):",
    placeholder="Example: CET1 is 5 million, AT1 is 1 million, Tier 2 is 2 million"
)

if st.button("Generate COREP Output"):

    # -------------------------------------------------
    # Simulated LLM extraction (for demo)
    # -------------------------------------------------
    extracted = {
        "CET1": 5_000_000,
        "AT1": 1_000_000,
        "Tier2": 2_000_000
    }

    extracted["TotalCapital"] = sum(extracted.values())

    # -------------------------------------------------
    # COREP rule references
    # -------------------------------------------------
    rule_map = {
        "CET1": "CRR Article 26",
        "AT1": "CRR Article 51",
        "Tier2": "CRR Article 62",
        "TotalCapital": "CRR Article 71"
    }

    # -------------------------------------------------
    # Build structured COREP output
    # -------------------------------------------------
    fields = []
    for key, value in extracted.items():
        fields.append({
            "COREP Cell": COREP_MAPPING[key],
            "Reported Value": value,
            "Regulatory Reference": rule_map[key]
        })

    # -------------------------------------------------
    # Display COREP Output
    # -------------------------------------------------
    st.subheader("COREP Structured Output")
    st.table(fields)

    # -------------------------------------------------
    # Validation
    # -------------------------------------------------
    valid, msg = validate_total_capital(extracted)

    st.subheader("Validation Result")
    if valid:
        st.success("✔ " + msg)
    else:
        st.error(msg)

    # -------------------------------------------------
    # Regulatory Audit Trail (Step 2 in action)
    # -------------------------------------------------
    st.subheader("Regulatory Audit Log")

    for key in ["CET1", "AT1", "Tier2"]:
        rule = get_rule_by_reference(rule_map[key])
        if rule:
            st.write(
                f"**{key}** classified using **{rule['reference']}** — {rule['text']}"
            )

    st.write(
        "**Total Capital** derived as the sum of CET1, AT1, and Tier 2 "
        "in accordance with **CRR Article 71**."
    )
