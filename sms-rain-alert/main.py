import requests
params = {
    "lat": 13.756331,
    "lon": 100.501762,
    "appid": "56ad33ad4a8d3d456e3487d814194254",
    "cnt": 4
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=params)

