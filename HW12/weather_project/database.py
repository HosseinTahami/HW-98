from typing import List, Tuple
import psycopg2 as psy
from datetime import datetime, timedelta


class WeatherDatabase:
    def __init__(self):

        self.conn = psy.connect(database = 'weather_db',
                                user = 'postgres',
                                password = 'iran1379',
                                host = 'localhost',
                                port = '5432'
                                )
        self.cur = self.conn.cursor()
    
    def save_request_data(self, city_name: str, request_time: str) -> None:

        self.cur.execute("""INSERT INTO requests 
                            (city_name, request_time) VALUES (%s, %s)""",
                            (city_name, request_time)
                        )
        self.conn.commit()
    
    def save_response_data(self, city_name: str, response_data: dict) -> None:
        
        
        if 'message' in response_data:
            temperature = None
            feels_like = None
            last_updated = None
            success_code = 0
        else:
            temperature = response_data['temperature']
            feels_like = response_data['feels_like']
            last_updated = response_data['last_updated']
            success_code = 1
        
        self.cur.execute("""INSERT INTO responses 
                            (city_name, success_code, temperature, feels_like, last_updated) 
                            VALUES ( %s, %s, %s, %s, %s)""", 
                            (city_name, success_code, temperature, feels_like, last_updated))
        self.conn.commit()
        
    def get_request_count(self) -> int:
        self.cur.execute("""SELECT COUNT(*) AS row_count 
                            FROM responses
                        """)
        return self.cur.fetchone()[0]
        
    def get_successful_request_count(self) -> int:
        self.cur.execute("""SELECT COUNT(*) AS row_count
                            FROM responses 
                            WHERE success_code = '1'
                        """)
        return self.cur.fetchone()[0]
    
    
    def get_city_request_count(self) -> List[Tuple[str, int]]:
        self.cur.execute("""SELECT city_name, COUNT(*) AS request_count
                            FROM responses
                            WHERE success_code = '1'
                            GROUP BY city_name
                        """)
        request_list = []
        for city in self.cur.fetchall():
            request_list.append(city)
        return request_list
    
    def get_last_hour_requests(self) -> List[Tuple[str, str]]:
        last_hour_date_time = datetime.now() - timedelta(hours = 1)
        now_date_time = datetime.now()
        self.cur.execute(f"""SELECT * 
                            FROM requests 
                            WHERE request_time BETWEEN '{last_hour_date_time}' AND '{now_date_time}' """
                            )

        request_list = []
        for city in self.cur.fetchall():
            request_list.append(city)
        return request_list

        
