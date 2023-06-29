from weather_server import get_city_weather

def test_get_city_weather():
    valid_name = 'Madrid'
    invalid_name = 'Invalid City'

    valid_city_name_data = get_city_weather(valid_name)
    invalid_city_name_data = get_city_weather(invalid_name)
    
    assert get_city_weather(invalid_name) == invalid_city_name_data
    assert 'temperature' in valid_city_name_data.keys()
    assert 'feels_like' in valid_city_name_data.keys()
    assert 'last_updated' in valid_city_name_data.keys()