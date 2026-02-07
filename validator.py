def calculate_total_capital(cet1, at1, tier2):
    return cet1 + at1 + tier2


def validate_total_capital(extracted):
    cet1 = extracted["CET1"]
    at1 = extracted["AT1"]
    tier2 = extracted["Tier2"]
    reported_total = extracted["TotalCapital"]

    expected = calculate_total_capital(cet1, at1, tier2)

    if expected == reported_total:
        return True, f"Total Capital is valid ({expected})."
    else:
        return False, (
            f"Validation error: Expected {expected}, "
            f"but reported {reported_total}."
        )
