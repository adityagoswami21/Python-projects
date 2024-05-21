import requests
import os
from creds import api_key
from dotenv import load_dotenv
load_dotenv
params = {
    "lat": 13.756331,
    "lon": 100.501762,
    "appid": api_key,
    "cnt": 4
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=params)
weather_data = response.json()
will_rain = False
weather_ids = []
for ids in weather_data['list']:
    weather_id = ids['weather'][0]['id']
    # print(f"id: {weather_id}")
    weather_ids.append(int(weather_id))
    if int(weather_id) < 700:
        will_rain = True
if will_rain:
    print("Bring an umbrella!")
