import re
import webbrowser
from urllib.request import urlopen
from bs4 import BeautifulSoup
from services.speech import speak

class MediaPlayer:
    def play_music_video(self, song):
        query = song.replace(' ', '+')
        url = f"https://www.youtube.com/results?search_query={query}"
        html = urlopen(url)
        soup = BeautifulSoup(html, "html.parser")
        video_ids = re.findall(r'watch\?v=(\S{11})', str(soup))
        if video_ids:
            webbrowser.open(f"https://www.youtube.com/watch?v={video_ids[0]}")
            speak(f"Playing {song}.")
        else:
            speak("No video found.")
