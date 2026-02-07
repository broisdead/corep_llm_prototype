import json

# -------------------------------------------------
# COREP cell mapping (used by app.py)
# -------------------------------------------------
COREP_MAPPING = {
    "CET1": "C 01.00 / r010 / c010",
    "AT1": "C 01.00 / r020 / c010",
    "Tier2": "C 01.00 / r030 / c010",
    "TotalCapital": "C 01.00 / r040 / c010"
}

# -------------------------------------------------
# Load mini regulatory dataset
# -------------------------------------------------
def load_rules():
    with open("rules.json", "r") as f:
        return json.load(f)

# -------------------------------------------------
# Retrieve rule by CRR reference (used in app.py)
# -------------------------------------------------
def get_rule_by_reference(reference):
    rules = load_rules()
    for rule in rules:
        if rule["reference"] == reference:
            return rule
    return None
