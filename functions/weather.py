import requests
import json
from decouple import config

GEO_API_TOKEN = config('GEO_API_KEY')
WEATHER_API_TOKEN = config('WEATHER_API_KEY')

def get_weather_by_city(location):

    geocoding_api_url = 'http://api.positionstack.com/v1/forward'
    params = {
        'access_key': GEO_API_TOKEN,
        'query': location
    }

    response = requests.get(geocoding_api_url, params=params)

    data = response.json()
    latitude = longitude = 0
    if 'data' in data and len(data['data']) > 0:
        latitude = data['data'][0]['latitude']
        longitude = data['data'][0]['longitude']
        print(f'Decoded lat/lon: {latitude}/{longitude} for city: {location}.')
    else:
        return f'Sorry, we ran into an error!\n{data}'
    
    current = ''

    weather_url = f'https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={WEATHER_API_TOKEN}'
    response = requests.get(weather_url)
    data = response.json()

    if response.status_code == 200:
        data_dict = json.loads(response.text)
        print(data_dict)
        city = data_dict["name"]
        weather = data_dict["weather"][0]["description"].lower()
        temp = str(int(data_dict["main"]["temp"] - 273.15))
        

        current = f'The current weather in {city} has {weather} with a temperature of {temp} degrees.\n'
        print(current)

    else:
        return f'Sorry, we ran into an error!\n{data}'

    return current