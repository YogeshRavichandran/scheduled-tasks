import requests
import os
import twilio
from twilio.rest import Client
api_key = os.environ.get("OWM_API_KEY")
CHENNAI_LAT = 13.082680
CHENNAI_LONG = 80.270721
parameters = {
    "lat":CHENNAI_LAT,
    "lon":CHENNAI_LONG,
    "appid":api_key,
    "cnt": 4
}

account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")

response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
weather_data = response.json()
# all_weather_id = []
# for intervals in range(0, 3):
#     weather_id = int(data["list"][intervals]["weather"][0]["id"])
#     all_weather_id.append(weather_id)
# print(all_weather_id)
#
# for weather in all_weather_id:
#     if weather < 700:
#         print("Bring an umbrella")

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body="It's gonna rain. Remember to bring your ☔️",
        from_="+19313913995",
        to="+918667865824",
    )

    print(message.status)
