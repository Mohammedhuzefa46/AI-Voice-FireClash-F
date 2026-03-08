import pyttsx3

# Initialize TTS engine
engine = pyttsx3.init()

# Optional: adjust voice speed
engine.setProperty('rate', 170)

def speak(text):

    print("AI:", text)

    engine.say(text)
    engine.runAndWait()