import os
import shutil
import psutil
from services.speech import speak

class SystemTools:
    def clean_temp_files(self):
        temp_path = os.getenv('TEMP') or '/tmp'
        try:
            files = os.listdir(temp_path)
            for file in files:
                try:
                    file_path = os.path.join(temp_path, file)
                    if os.path.isfile(file_path) or os.path.islink(file_path):
                        os.unlink(file_path)
                    elif os.path.isdir(file_path):
                        shutil.rmtree(file_path)
                except Exception:
                    pass
            speak("Temporary files cleaned.")
        except Exception as e:
            speak(f"Failed to clean temp files: {e}")

    def check_disk_usage(self):
        usage = psutil.disk_usage('/')
        speak(f"Disk usage: {usage.percent} percent full.")
