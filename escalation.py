def detect_escalation(text):
    text = text.lower()

    if "manager" in text:
        return "high"

    elif "not resolved" in text or "complaint" in text:
        return "medium"

    elif "bad service" in text:
        return "medium"

    else:
        return "low"