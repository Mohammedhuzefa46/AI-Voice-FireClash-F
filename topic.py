def detect_topic(text):
    text = text.lower()

    if "charge" in text or "transaction" in text:
        return "duplicate transaction"

    elif "card" in text:
        return "credit card charges"

    elif "cancel" in text:
        return "subscription cancellation"

    elif "login" in text or "access" in text:
        return "account access issue"

    else:
        return "general inquiry" 