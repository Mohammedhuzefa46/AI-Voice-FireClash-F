from asr import listen
from tts import speak 
from emotion import detect_emotion
from intent import detect_intent
from topic import detect_topic
from escalation import detect_escalation
from llm import generate_llm_response


import websocket
import json
import warnings
warnings.filterwarnings("ignore")


def fallback_response():
    return "I am here to help you."


def send_to_dashboard(intent, topic, sentiment, escalation):
    try:
        ws = websocket.create_connection("ws://127.0.0.1:8000/ws")

        data = {
            "intent": intent,
            "topic": topic,
            "sentiment": sentiment,
            "escalation_risk": escalation
        }

        ws.send(json.dumps(data))
        ws.close()

    except Exception as e:
        print("Dashboard connection failed:", e)


def main():

    while True:

        text = listen()

        if text is None:
            print("No speech detected. Listening again...")
            continue

        emotion = detect_emotion(text)
        intent = detect_intent(text)
        topic = detect_topic(text)
        escalation = detect_escalation(text)

        print("\n--- Conversation Analytics ---")
        print("Intent:", intent)
        print("Topic:", topic)
        print("Sentiment:", emotion)
        print("Escalation Risk:", escalation)

        send_to_dashboard(intent, topic, emotion, escalation)

        response = generate_llm_response(text, emotion)

        if response is None:
            response = fallback_response()

        speak(response)


if __name__ == "__main__":
    main()