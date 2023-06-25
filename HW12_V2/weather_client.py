import requests
import json
import weather_server



def start_client(city):

    response = requests.get("http://"+f"{weather_server.HOST}:{weather_server.PORT}/{city}")
    data = response.json()
    if 'message' in data:
        print('Error: ',{data['message']})
    else:
        print(f'Temperature: {data["temperature"]}°C')
        print(f'Feels like: {data["feels_like"]}°C')
        print(f'Last updated: {data["last_updated"]}')
            


if __name__ == '__main__' :
    while True:
        city = input("Enter city name: ")
        start_client(city)
    