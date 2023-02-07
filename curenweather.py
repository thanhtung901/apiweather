import tkinter as tk
import requests

def getWeather(city):
    apiUrl = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=c55cad7bdd0e7d82b0b958fdfd7ceeae"

    json_data = requests.get(apiUrl).json()

    condition = json_data['weather'][0]['main']
    temp = int(json_data['main']['temp'] - 273.15)
    min_temp = int(json_data['main']['temp_min'] - 273.15)
    max_temp = int(json_data['main']['temp_max'] - 273.15)
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']
    return condition, temp, min_temp, max_temp, pressure,   humidity,   wind

