from twilio.rest import Client
import requests
import os
from dotenv import load_dotenv
account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
load_dotenv()
params = {
    "lat": 13.756331,
    "lon": 100.501762,
    "appid": os.getenv('api_key'),
    "cnt": 4
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=params)
weather_data = response.json()
# print(weather_data)
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
    client = Client(account_sid, auth_token)

    message = client.messages \
                    .create(
                        body="It's going to rain today, Bring an umbrella!☔",
                        from_=os.getenv("from_no"),
                        to=os.getenv("to_no")
                    )

    print(message.status)