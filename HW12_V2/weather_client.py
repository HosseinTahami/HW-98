import requests
import json
import weather_server



def start_client(city):

    response = requests.get("http://"+f"{weather_server.HOST}:{weather_server.PORT}/{city}")
    data = response.json()
    print(data)
    if 'message' in data:
        print(f"Error: {data['message']}")
        print('---------------------------------------------------------------------------------')
    else:
        print(f'Temperature: {data["temperature"]}°C')
        print(f'Feels like: {data["feels_like"]}°C')
        print(f'Last updated: {data["last_updated"]}')
        print('---------------------------------------------------------------------------------')
            


if __name__ == '__main__' :
    while True:
        city = input("\nEnter city name: ")
        start_client(city)
    