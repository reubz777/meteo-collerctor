from owm.client import OWMClient


def main(city: str = "Minsk"):
    api_key = "0a0785a7cbe7833d2b6497f58dd8c2dc"
    own_client = OWMClient(api_key)
    print(own_client.get_weather_by_city(city))


if __name__ == "__main__":
    main()
