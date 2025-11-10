from typing import List

from pydantic import BaseModel


class WeatherResponse(BaseModel):
    name: str
    main: "Main"
    weather: List["Weather"]
    wind: "Wind"

    class Main(BaseModel):
        temp: float
        feels_like: float
        humidity: int
        pressure: int

    class Weather(BaseModel):
        description: str
        main: str

    class Wind(BaseModel):
        speed: float

    def kelvin_to_celsius(self, kelvin: float) -> float:
        return kelvin - 273.15

    def __str__(self):
        return f"""

    ПОГОДА В {self.name.upper()}

    Температура: {self.kelvin_to_celsius(self.main.temp):.1f}°C
    Ощущается как: {self.kelvin_to_celsius(self.main.feels_like):.1f}°C
    Влажность: {self.main.humidity}%
    Ветер: {self.wind.speed} м/с
    Давление: {self.main.pressure} hPa
        """.strip()
