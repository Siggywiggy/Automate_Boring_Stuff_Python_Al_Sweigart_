#! python3
# Prints the weather for a location from the command line

import json
import requests
import sys
import pprint
from datetime import datetime

app_ID = '9aea7ae09310844c230420c39a528cf4'

# generate location from command line arguments
if len(sys.argv) < 2:
    print('Enter city name!')
    sys.exit()


location = sys.argv[1]
units = 'metric'


# get the latitude and longitude from Geocoding API
geocoding_url = f'http://api.openweathermap.org/geo/1.0/direct?q={location}&limit=1&appid={app_ID}'
response = requests.get(geocoding_url)
response.raise_for_status()
json_data = json.loads(response.text)

latitude = json_data[0]['lat']
longitude = json_data[0]['lon']

# get the weather data
weather_request_url = f'https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&units={units}&appid={app_ID}'


response = requests.get(weather_request_url)
response.raise_for_status()

# load JSON data and print weather

weather_data = json.loads(response.text)
#pprint.pprint(weather_data)

sunrise = datetime.fromtimestamp(weather_data['sys']['sunrise']).strftime("%A, %B %d, %Y %I:%M:%S")
sunset = datetime.fromtimestamp(weather_data['sys']['sunset']).strftime("%A, %B %d, %Y %I:%M:%S")


print(f"Current weather in {weather_data['name']}")
print(f"Current temperature is {round(weather_data['main']['temp'], 2)} Celsius")
print(f"Current humidity is {weather_data['main']['humidity']} % Rh")
print(f"Current air pressure is {weather_data['main']['pressure']} hPa")
print(f'The sun rises on {sunrise} am')
print(f'The sun sets on {sunset} pm')

