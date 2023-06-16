import requests

api_key = "d1b85a0024a2a5a7e6489e6b761b3ef8"
base_url = "https://api.openweathermap.org/data/2.5/weather"
city_name = input("Enter city name: ")


def get_weather_data(city_name):
    completed_url = base_url + "?q=" + city_name + "&appid=" + api_key
    response = requests.get(completed_url)
    api = response.json()
    kelvin_temp = api["main"]["temp"]
    centigrade_temp = kelvin_temp - 273.15
    return "{:.2f}".format(centigrade_temp)
    


print(f"{city_name} temperature is {get_weather_data(city_name)} celsius")
