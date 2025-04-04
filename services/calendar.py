from datetime import datetime
from services.speech import speak

class CalendarService:
    def __init__(self):
        self.events = []  # Simple list; can be extended to Google Calendar

    def add_event(self, title, time_str):
        try:
            time_obj = datetime.strptime(time_str, "%Y-%m-%d %H:%M")
            self.events.append((title, time_obj))
            speak(f"Event '{title}' added for {time_obj.strftime('%B %d at %H:%M')}.")
        except ValueError:
            speak("Invalid date and time format. Use YYYY-MM-DD HH:MM")

    def list_events(self):
        if not self.events:
            speak("You have no events scheduled.")
        else:
            for title, time_obj in sorted(self.events, key=lambda x: x[1]):
                speak(f"{title} at {time_obj.strftime('%Y-%m-%d %H:%M')}")
