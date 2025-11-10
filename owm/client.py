import requests

from owm.models import WeatherResponse


class OWMClient:
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

    def __init__(self, api_key: str):
        self.api_key = api_key

    def get_weather_by_city(self, city: str):
        url = f"{self.BASE_URL}?q={city}&appid={self.api_key}"
        r = requests.get(url)
        data = r.json()
        return WeatherResponse(**data)
