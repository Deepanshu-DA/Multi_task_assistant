import pyautogui
import datetime
from services.speech import speak

class ScreenTools:
    def take_screenshot(self):
        filename = f"screenshot_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
        pyautogui.screenshot(filename)
        speak(f"Screenshot saved as {filename}.")
