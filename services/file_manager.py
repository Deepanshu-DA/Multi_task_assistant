import os
import shutil
from services.speech import speak

class FileManager:
    def list_files(self, directory="."):
        try:
            files = os.listdir(directory)
            speak(f"Files in {directory} are: {', '.join(files)}")
        except Exception as e:
            speak(f"Failed to list files: {e}")

    def delete_file(self, path):
        try:
            os.remove(path)
            speak("File deleted.")
        except Exception as e:
            speak(f"Error deleting file: {e}")

    def move_file(self, src, dst):
        try:
            shutil.move(src, dst)
            speak(f"Moved file from {src} to {dst}.")
        except Exception as e:
            speak(f"Could not move file: {e}")
