import requests
params = {
    "lat": 13.756331,
    "lon": 100.501762,
    "appid": "56ad33ad4a8d3d456e3487d814194254",
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
