import requests
import json

api_key = "d1b85a0024a2a5a7e6489e6b761b3ef8"
base_url = "https://api.openweathermap.org/data/2.5/weather"

def get_city_weather(city_name: str) -> dict:
    """
    Retrieve weather data from an external API for a given city.

    Args:
    - city_name (str): The name of the city to retrieve weather data for.

    Returns:
    - dict: A dictionary containing weather information for the city, including:
            -temperature
            -feels like temperature
            -last updated time
    """
    completed_url = base_url + "?q=" + city_name + "&appid=" + api_key
    API_response = requests.get(completed_url)
    api = API_response.json()
    return api

def start_server() -> None:
    """
    Start the weather server.
    """
    pass

city_name = input("Enter a city name: ")
