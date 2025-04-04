from services.weather import WeatherAPI
from services.location import Geolocation
from services.email_service import EmailService
from services.app_launcher import AppLauncher
from services.reminder import Reminder
from services.media_player import MediaPlayer
from services.speech import speak, listen
import re

class CommandParser:
    def __init__(self):
        self.weather_api = WeatherAPI()
        self.geolocation = Geolocation()
        self.email_service = EmailService()
        self.app_launcher = AppLauncher()
        self.reminder = Reminder()
        self.media_player = MediaPlayer()

    def split_commands(self, command: str):
        return [c.strip() for c in re.split(r"\band\b", command)]

    def handle_command(self, command: str):
        command = command.lower()

        if "weather" in command:
            location = self.geolocation.get_location()
            if location:
                info = self.weather_api.get_weather_by_coords(*location)
                speak(info)
            else:
                speak("Could not determine your location.")

        elif "open" in command:
            app = command.replace("open", "").strip()
            self.app_launcher.open_application(app)

        elif "set reminder" in command:
            speak("What should I remind you about?")
            reminder_msg = listen()
            speak("At what time? (Format HH:MM)")
            reminder_time = listen()
            if reminder_msg and reminder_time:
                self.reminder.set_reminder(reminder_time, reminder_msg)

        elif "play music" in command:
            speak("What song would you like to play?")
            song = listen()
            self.media_player.play_music_video(song)

        elif "send email" in command:
            speak("Recipient's email address?")
            recipient = listen()
            speak("Subject?")
            subject = listen()
            speak("Email body?")
            body = listen()
            if recipient and subject and body:
                self.email_service.send_email(recipient, subject, body)

        elif "stop" in command:
            speak("Goodbye!")
            exit(0)

        else:
            speak("I didn't understand that command.")
