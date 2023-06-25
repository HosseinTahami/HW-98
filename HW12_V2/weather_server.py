from http.server import BaseHTTPRequestHandler , HTTPServer
import requests
from datetime import datetime

api_key = "d1b85a0024a2a5a7e6489e6b761b3ef8"
base_url = "https://api.openweathermap.org/data/2.5/weather"
HOST = "localhost"
PORT = 9999

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

class WeatherRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        weather_dict = get_city_weather(city)
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(weather_dict)
        
   
def start_server() -> None :
    
    server = HTTPServer((HOST, PORT), WeatherRequestHandler)
    server.server_forever()
    server.server_close()
    
        