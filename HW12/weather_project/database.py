from typing import List, Tuple
import psycopg2 as psy
from datetime import datetime, timedelta


class WeatherDatabase:
    def __init__(self,db_name):

        self.conn = psy.connect(database = db_name,
                                user = 'postgres',
                                password = 'iran1379',
                                host = 'localhost',
                                port = '5432'
                                )
        self.cur = self.conn.cursor()
    
    def save_request_data(self, city_name: str, request_time: str) -> None:
        
        self.cur.execute(""" SELECT COUNT(request_id)
                             FROM requests""")
        
        id_number = self.cur.fetchone()[0] + 1
        self.cur.execute(f"""INSERT INTO requests (city_name, request_id, request_time) 
                            VALUES {city_name, id_number, request_time} """)
        
        self.conn.commit()
    
    def save_response_data(self, city_name: str, response_data: dict) -> None:
        
        self.cur.execute(""" SELECT COUNT(request_id)
                             FROM responses""")
        id_number = self.cur.fetchone()[0] + 1
        
        if 'message' in response_data:
            temperature_deg = None
            feels_like = None
            last_updated = None
            success_code = False
            self.cur.execute(f"""INSERT INTO responses 
                                (request_id, city_name, temperature, feels_like, success_code, last_updated) 
                                VALUES (%s, %s, %s, %s, %s, %s)""",
                                (id_number, city_name, temperature_deg, feels_like, success_code, last_updated))
        else:
            temperature = response_data['temperature']
            feels_like = response_data['feels_like']
            last_updated = response_data['last_updated']
            success_code = True
            self.cur.execute(f"""INSERT INTO responses 
                                (request_id, city_name, temperature, feels_like, success_code, last_updated) 
                                VALUES {id_number, city_name, temperature, feels_like, success_code, last_updated}""" )
        

        self.conn.commit()
        
    def get_request_count(self) -> int:
        self.cur.execute("""SELECT COUNT(*) AS row_count 
                            FROM requests
                        """)
        return self.cur.fetchone()[0]
        
    def get_successful_request_count(self) -> int:
        self.cur.execute("""SELECT COUNT(*) AS row_count
                            FROM responses 
                            WHERE success_code = True
                        """)
        return self.cur.fetchone()[0]
    
    
    def get_city_request_count(self) -> List[Tuple[str, int]]:
        self.cur.execute("""SELECT city_name, COUNT(*) AS request_count
                            FROM requests
                            GROUP BY city_name 
                            ORDER BY city_name ASC
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

        
