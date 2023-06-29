import pytest
from datetime import datetime, timedelta
import sys
sys.path.insert(0, '/home/hossein/MaktabSharif/HW-98/HW12/weather_project/')
from database import WeatherDatabase

@pytest.fixture
def test():
    db = WeatherDatabase('weather_test_db')
    yield db
    db.cur.execute("delete from responses")
    db.cur.execute("delete from requests")
    db.conn.commit()
 

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
    test.cur.execute("select count(*) from responses")
    assert test.cur.fetchone()[0] == 1
    
    testing_data_invalid = {'message' : 'City not found'}
    test.save_response_data('Invalid City', testing_data_invalid)
    test.cur.execute("select count(*) from responses")
    assert test.cur.fetchone()[0] == 2
    

def test_get_request_count(test):
    #test.save_request_data('Madrid', '2020-09-11 11:42:00')
    test.cur.execute(f"""INSERT INTO requests (city_name, request_id, request_time) 
                        VALUES {"madrid", 1, '2023-01-01 00:00:00'} """)
    test.conn.commit()
    assert test.get_request_count() == 1

def test_get_successful_request_count(test):
    test.cur.execute(f"""INSERT INTO responses 
                        (request_id, city_name, temperature, feels_like, success_code, last_updated) 
                        VALUES {1, "madrid", 22.22, 22.33, True, '2023-01-01 00:00:00'}""" )
    test.conn.commit()
    assert test.get_successful_request_count() == 1

def test_get_city_request_count(test):
    valid_result = [("invalid city", 1), ("madrid", 1)]
    test.cur.execute(f"""INSERT INTO requests (city_name, request_id, request_time) 
                        VALUES {"madrid", 1, '2023-01-01 00:00:00'} """)
    test.conn.commit()
    test.cur.execute(f"""INSERT INTO requests (city_name, request_id, request_time) 
                        VALUES {"invalid city", 2, '2023-01-01 00:00:00'} """)
    test.conn.commit()
    assert test.get_city_request_count() == valid_result
    
def test_get_last_hour_requests(test):
    now = datetime.now()
    last_hour = now - timedelta( hours = 2 )
    test.cur.execute(f"""INSERT INTO requests (city_name, request_id, request_time) 
                        VALUES {"paris", 1, str(last_hour)} """)
    test.conn.commit()
    test.cur.execute(f"""INSERT INTO requests (city_name, request_id, request_time) 
                        VALUES {"madrid", 2, str(now)} """)
    test.conn.commit()
    valid_result = [("madrid", 2,str(now))]
    assert test.get_last_hour_requests() == valid_result
        
