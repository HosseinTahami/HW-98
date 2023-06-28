from weather_server import get_city_weather

def test_get_city_weather():
    valid_name = 'Madrid'
    invalid_name = 'Invalid City'
    
    successful_result = {
        'temperature' : 12.34,
        'feels_like' : 43.33,
        'last_updated' : '1998-09-09 12:09:00'
    }
    
    valid_city_name_data = get_city_weather(valid_name)
    invalid_city_name_data = get_city_weather(invalid_name)
    
    assert get_city_weather(invalid_name) == invalid_city_name_data
    assert type(valid_city_name_data['temperature']) == type(successful_result['temperature'])
    assert type(valid_city_name_data['feels_like']) == type(successful_result['feels_like'])
    assert type(valid_city_name_data['last_updated']) == type(successful_result['last_updated'])