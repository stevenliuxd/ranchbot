import requests
import json

def get_weather_by_city(location):

    geocoding_api_url = 'http://api.positionstack.com/v1/forward'
    params = {
        'access_key': '3325fb1031835a16dc5426f3ff326e14',
        'query': location
    }

    response = requests.get(geocoding_api_url, params=params)
    print(f'get geocoding response: {response.json()}')

    data = response.json()
    latitude = longitude = 0
    if 'data' in data and len(data['data']) > 0:
        latitude = data['data'][0]['latitude']
        longitude = data['data'][0]['longitude']
        print(f'Decoded lat/lon: {latitude}/{longitude} for city: {location}.')
    else:
        return 'DNE'
    
    current = ''

    weather_url = f'https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid=edba5fd777925d3c8bd56bed14996323'
    response = requests.get(weather_url)
    print(f'get weather response: {response.json()}')

    if response.status_code == 200:
        data_dict = json.loads(response.text)
        print(data_dict)
        city = data_dict["name"]
        weather = data_dict["weather"][0]["description"].lower()
        temp = str(int(data_dict["main"]["temp"] - 273.15))
        

        current = f'The current weather in {city} has {weather} with a temperature of {temp} degrees.\n'
        print(current)

    else:
        return 'DNE'

    return current