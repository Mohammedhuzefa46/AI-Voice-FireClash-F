def detect_intent(text):
    text = text.lower()

    if "hello" in text or "hi" in text:
        return "greeting"

    elif "help" in text:
        return "help"

    elif "time" in text:
        return "question"

    else:
        return "unknown"