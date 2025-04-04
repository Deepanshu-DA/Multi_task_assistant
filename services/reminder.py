import threading
import time
from datetime import datetime
from services.speech import speak

class Reminder:
    def set_reminder(self, time_str, message):
        reminder_time = datetime.strptime(time_str, "%H:%M").time()
        threading.Thread(target=self.check_reminder, args=(reminder_time, message)).start()

    def check_reminder(self, reminder_time, message):
        while True:
            now = datetime.now().time()
            if now.hour == reminder_time.hour and now.minute == reminder_time.minute:
                speak(f"Reminder: {message}")
                break
            time.sleep(30)
