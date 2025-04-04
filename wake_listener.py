import speech_recognition as sr
from services.speech import listen, speak

recognizer = sr.Recognizer()

WAKE_WORDS = ["hey assistant", "okay assistant"]

def listen_with_wake_word():
    with sr.Microphone() as source:
        print("Listening for wake word...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        query = recognizer.recognize_google(audio).lower()
        print(f"Wake check: {query}")

        if any(wake in query for wake in WAKE_WORDS):
            speak("Yes?")
            with sr.Microphone() as source:
                recognizer.adjust_for_ambient_noise(source)
                audio = recognizer.listen(source)
            try:
                command = recognizer.recognize_google(audio).lower()
                return command
            except sr.UnknownValueError:
                speak("Sorry, I didn't catch that.")
            except sr.RequestError:
                speak("Speech service is down.")

    except sr.UnknownValueError:
        pass
    except sr.RequestError:
        speak("Network error.")

    return None