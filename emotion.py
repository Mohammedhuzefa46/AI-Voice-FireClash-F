def detect_emotion(text):

    if text is None:
        return "neutral"

    text = text.lower()

    if "happy" in text:
        return "positive"

    elif "sad" in text or "angry" in text:
        return "negative"

    return "neutral"