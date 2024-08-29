import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "dev_secret")
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "postgresql+asyncpg://rakesh_reddy:mypassword@db:5432/women_safety")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    WEATHER_API_KEY = os.getenv("WEATHER_API_KEY", "6d5e7e357f3dae65d7e4fd7597d2c7d0")
    WEATHER_API_URL = os.getenv("WEATHER_API_URL", "http://api.weatherapi.com/v1/current.json")
