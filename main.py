import requests
from twilio.rest import Client
import json

with open ("credentials.json", mode= "r") as file :
    data = json.load(file)

account_sid = data["account_sid"]
auth_token = data["auth_token"]
api_key = data["api_key"]

parameters = {
    "lat" : 55.755825,
    "lon" : 37.617298,
    "appid" : api_key,
    "cnt" : 4 ,
}
response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params= parameters )
response.raise_for_status()
weather_data = response.json()
weather_ids = [dict['weather'][0]['id'] for dict in weather_data['list']]

rainy = False

for id in weather_ids :
    if int(id) < 700 :
        rainy = True
if rainy :
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today, Remember to bring an ☔",
        from_= data["sender"],
        to= data["receiver"],
    )

    print(message.status)

