from services.speech import speak
import openai
import os

class ChatBot:
    def __init__(self):
        openai.api_key = os.getenv("OPENAI_API_KEY")

    def ask(self, prompt):
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}]
            )
            reply = response['choices'][0]['message']['content']
            speak(reply)
        except Exception as e:
            speak(f"Sorry, I couldn't get an answer. {e}")
