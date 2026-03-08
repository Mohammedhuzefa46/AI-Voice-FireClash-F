def generate_response(intent, emotion):

    if intent == "greeting":
        return "Hello! How can I assist you today?"

    elif intent == "help":
        if emotion == "sad":
            return "I am here for you. Please tell me what is troubling you."
        return "Sure, tell me how I can help."

    elif intent == "question":
        return "That is an interesting question."

    else:
        return "Sorry, I did not understand that."