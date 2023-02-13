import datetime
import requests

class getWeather():

    condition = ''
    temperature = ''
    wind = ''
    city = ''
    time = ''
    def __init__(self, city):
        apiUrl = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=c55cad7bdd0e7d82b0b958fdfd7ceeae"
        json_data = requests.get(apiUrl).json()
        self.condition = json_data['weather'][0]['main']
        self.temperature = int(json_data['main']['temp'] - 273.15)
        self.wind = json_data['wind']['speed']
        self.city = city
        self.time = datetime.datetime.now()
    def get_condition(self):
        return self.condition
    def get_city(self):
        return self.city
    def get_wind(self):
        return self.wind
    def get_temperature(self):
        return self.temperature
    def get_time(self):
        return self.time
if __name__ == '__main__':
    api = getWeather('hanoi')
    print('wind: ',api.get_wind())
    print('temperature: ',api.get_temperature())
    print('city: ',api.get_city())
    print('condition: ',api.get_condition())
    print('time ', api.get_time())