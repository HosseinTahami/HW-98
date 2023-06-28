from database import WeatherDatabase
import pytest
from datetime import datetime, timedelta


@pytest.fixture
def test():
    db = WeatherDatabase('weather_test_db')
    db.cur.execute("delete from requests")
    db.cur.execute("delete from responses")
    db.conn.commit()
    return db  

def test_save_request_data(test):
    test.save_request_data('Madrid', '2020-09-11 11:42:00')
    test.cur.execute("select count(*) from requests")
    assert test.cur.fetchone()[0] == 1
    
def test_save_response_data(test):
    testing_data_valid = {
        
        'temperature': 23.56,
        'feels_like' : 78.99,
        'last_updated' : '2023-01-01 00:00:00'
    }
    
    test.save_response_data("Madrid", testing_data_valid)
    test.cur.execute("select count(*) from requests")
    assert test.cur.fetchone()[0] == 1
    
    testing_data_invalid = {'message' : 'City not found'}
    test.save_response_data('Invalid City', testing_data_invalid)
    test.cur.execute("select count(*) from requests")
    assert test.cur.fetchone()[0] == 2
    

def test_get_request_count(test):
    assert test.get_request_count() == 1

def test_get_successful_request_count(test):
    test.cur.execute("select count(*) from requests")
    assert test.get_successful_request_count() == 1

def test_get_city_request_count(test):
    valid_result = [("Madrid", 1), ("Invalid City", 1)]
    assert test.get_city_request_count() == valid_result
    
def test_get_last_hour_requests(test):
    now = datetime.now()
    last_hour = now - timedelta( hours = 1 )
    test.save_request_data("New York", last_hour)
    test.save_request_data("Paris", last_hour)
    valid_result = [("New York", last_hour),("Paris", now)]
    assert test.get_last_hour_requests() == valid_result
        
