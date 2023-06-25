import requests
import json
import weather_server

city = input("Enter city name: ")

def start_client():
    while True:
        response = requests.get(f"http://{weather_server.HOST}:{weather_server.PORT}/{city}")
        data = response.json()
        if 'message' in data:
            print('Error: ',{data['message']})
        else:
            print(f'Temperature: {data["main"]["temp"]}°C')
            print(f'Feels like: {data["main"]["feels_like"]}°C')
            print(f'Last updated: {data["dt"]}')
            



start_client(city)
    