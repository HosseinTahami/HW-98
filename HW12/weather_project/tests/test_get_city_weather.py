import requests
from datetime import datetime


def test_get_city_weather():
    city_name = 'Madrid'
    valid_data = {
        'temperature' : 12.34,
        'feels_like' : 43.33,
        'last_updated' : '1998-09-09 12:09:00'
    }

