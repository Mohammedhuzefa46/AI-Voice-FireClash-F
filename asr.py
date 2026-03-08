import speech_recognition as sr

recognizer = sr.Recognizer()

def listen():

    with sr.Microphone() as source:

        print("Listening...")

        audio = recognizer.listen(source)


        try:
            text = recognizer.recognize_google(audio)
            return text.lower()

        except Exception as e:
            print("ASR Error:", e)
            return ""