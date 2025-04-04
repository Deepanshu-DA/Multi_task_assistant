import webbrowser
from services.speech import speak

class BrowserControl:
    def search_google(self, query):
        url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
        webbrowser.open(url)
        speak(f"Searching Google for {query}.")

    def open_website(self, url):
        if not url.startswith("http"):
            url = f"https://{url}"
        webbrowser.open(url)
        speak(f"Opening {url}.")
