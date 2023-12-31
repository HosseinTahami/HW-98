from http.server import BaseHTTPRequestHandler , HTTPServer
import requests
import json
from datetime import datetime
import urllib

api_key = "d1b85a0024a2a5a7e6489e6b761b3ef8"
base_url = "https://api.openweathermap.org/data/2.5/weather"
HOST = "localhost"
PORT = 9997

def get_city_weather(city_name) -> dict:
    
    completed_url = base_url + "?q=" + city_name + "&appid=" + api_key
    response = requests.get(completed_url)
    api = response.json()
    #print(API_response.content)
    
    if response.status_code == 200 :    
        weather_dict = {
            'temperature': "{:.2f}".format(api["main"]["temp"] - 273.15),
            'feels_like' : "{:.2f}".format(api["main"]["feels_like"] - 273.15),
            'last_updated' : datetime.fromtimestamp(api['dt']).strftime('%Y-%m-%d %H:%M:%S')
        }
        return weather_dict

    if 'message' in api:
        return api

class WeatherRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        city = urllib.parse.unquote(self.path[1:])
        weather_dict = get_city_weather(city)
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(weather_dict).encode())
        
   
def start_server() -> None :
    server = HTTPServer((HOST, PORT), WeatherRequestHandler)
    print(f"Starting server on {HOST}:{PORT}...")
    server.serve_forever()

if __name__ == "__main__":
    print(f"Starting server on {HOST}:{PORT}...")
    start_server()