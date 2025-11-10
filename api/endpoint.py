import os
import sys

from fastapi import Depends, FastAPI

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from services.usecase import WeatherUsecase

app = FastAPI()


@app.get("/weather/")
async def root(city: str, wether_provider=Depends(WeatherUsecase)):
    result = wether_provider.get_weather_data(city)
    context = {
        "message": f"successfully received info about {city}",
        "data": result,
    }
    return context
