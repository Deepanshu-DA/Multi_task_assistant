import os
from services.speech import speak

class AppLauncher:
    def open_application(self, app_name):
        try:
            if os.name == "nt":
                os.system(f"start {app_name}")
            elif os.uname().sysname == "Darwin":
                os.system(f"open -a {app_name}")
            else:
                os.system(f"xdg-open {app_name}")
            speak(f"Opening {app_name}.")
        except Exception as e:
            speak(f"Error opening application: {e}")
