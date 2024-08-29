import requests
from config import Config

def get_weather_info():
    response = requests.get(
        f"{Config.WEATHER_API_URL}?key={Config.WEATHER_API_KEY}&q=London"
    )
    data = response.json()
    return {
        "temperature": data['current']['temp_c'],
        "condition": data['current']['condition']['text']
    }
