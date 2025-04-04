import os
from services.speech import speak

NOTES_FILE = "notes.txt"

class NotesManager:
    def save_note(self, note):
        with open(NOTES_FILE, "a") as f:
            f.write(note + "\n")
        speak("Note saved.")

    def read_notes(self):
        if os.path.exists(NOTES_FILE):
            with open(NOTES_FILE, "r") as f:
                notes = f.readlines()
                for line in notes:
                    speak(line.strip())
        else:
            speak("No notes found.")

    def clear_notes(self):
        if os.path.exists(NOTES_FILE):
            os.remove(NOTES_FILE)
            speak("All notes cleared.")
