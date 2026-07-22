def test_calculate_priority_score(customer_types: str, severity: int) -> str:
    if severity <1 or severity >5:
        raise ValueError("Severity must be between 1 and 5")

    if customer_types == "premium" and severity >= 4:
        return "High"

    if severity == 5:
        return "High"

    if severity == 1:
        return "Low"

    if customer_types == "standard" and severity < 4:
        return "Medium"

    return "normal"
