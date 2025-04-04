import threading
from listener import listen
from command_parser import CommandParser
from services.speech import speak

WAKE_WORD = "hey assistant"

parser = CommandParser()

def handle_command(command):
    try:
        parser.handle_command(command)
    except Exception as e:
        speak(f"Error handling command: {e}")

if __name__ == "__main__":
    speak("Assistant is ready. Say 'Hey Assistant' to activate.")
    while True:
        query = listen()
        if query and WAKE_WORD in query:
            speak("I'm listening...")
            command = listen()
            if command:
                command_list = parser.split_commands(command)
                for cmd in command_list:
                    threading.Thread(target=handle_command, args=(cmd.strip(),)).start()
