from api.dependencies import get_api_key


class WeatherUsecase:
    def get_weather_data(self, city: str = "Minsk"):
        own_client = get_api_key()
        data = own_client.get_weather_by_city(city)
        return data
