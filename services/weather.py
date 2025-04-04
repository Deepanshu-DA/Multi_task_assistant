import os
import requests

class WeatherAPI:
    def __init__(self):
        self.api_key = os.getenv("WEATHER_API_KEY")
        self.base_url = "https://api.openweathermap.org/data/2.5/weather"

    def get_weather_by_coords(self, lat, lon):
        params = {"lat": lat, "lon": lon, "appid": self.api_key, "units": "metric"}
        response = requests.get(self.base_url, params=params).json()

        if response.get("main"):
            weather_desc = response["weather"][0]["description"]
            temperature = response["main"]["temp"]
            return f"Weather: {weather_desc}, Temperature: {temperature}°C"
        return "Could not retrieve weather data."