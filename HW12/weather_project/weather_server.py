import requests
import json
from http.server import HTTPServer, BaseHTTPRequestHandler
from datetime import datetime

api_key = "d1b85a0024a2a5a7e6489e6b761b3ef8"
base_url = "https://api.openweathermap.org/data/2.5/weather"

def get_city_weather(city_name: str) -> dict:
    
    completed_url = base_url + "?q=" + city_name + "&appid=" + api_key
    API_response = requests.get(completed_url)
    api = API_response.json()
    print(API_response.content)
    
    if API_response.status_code == 200 :    
        api_dict = {
            'temperature': "{:.2f}".format(api["main"]["temp"] - 273.15),
            'feels_like' : "{:.2f}".format(api["main"]["feels_like"] - 273.15),
            'last_updated' : datetime.fromtimestamp(api['dt']).strftime('%Y-%m-%d %H:%M:%S')
        }
        return api_dict

    if API_response.status_code == 404 :
        return "city not found"    
        
def start_server() -> None:
    """
    Start the weather server.
    """
    pass

city_name = input("Enter a city name: ")
get_city_weather(city_name)
'''
{
    "coord":{
        "lon":-3.7026,
        "lat":40.4165
            },
            
    "weather":[{"id":800,"main":"Clear","description":"clear sky","icon":"01d"}],
    
    "base":"stations",
    
    "main":{"temp":307.14,"feels_like":306.09,"temp_min":305.93,"temp_max":308.96,"pressure":1018,"humidity":28},
    
    "visibility":10000,
    
    "wind":{
        "speed":2.06,
        "deg":260},
    
    "clouds":{
        "all":0
        },
    
    "dt":1687621651,
    
    "sys":{
        "type":2,
        "id":2007545,
        "country":"ES",
        "sunrise":1687581923,
        "sunset":1687636128},
        "timezone":7200,
        "id":3117735,
        "name":"Madrid",
        "cod":200
        }
}
'''