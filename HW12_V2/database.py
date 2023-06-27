from typing import List, Tuple
import psycopg2 as psy


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

        self.cur.execute("INSERT INTO requests (city_name, request_time) VALUES (%s, %s)",
                        (city_name, request_time)
                        )
        self.cur.commit()
    
    def save_response_data(self, city_name: str, response_data: dict) -> None:

        temperature = response_data['temperature']
        feels_like = response_data['feels_like']
        last_updated = response_data['last_updated']
        
        self.cur.execute("INSERT INTO responses (city_name, temperature, feels_like, last_updated, response_time ) VALUES (%s, %i, %i, %s)",
                        (city_name, temperature, feels_like, last_updated)
                        )
        self.cur.commit()
        
    def get_request_count(self) -> int:
        """
        Get the total number of requests made to the server.

        Returns:
        - int: The total number of requests made to the server.
        """
        pass
    
    def get_successful_request_count(self) -> int:
        """
        Get the total number of successful requests made to the server.

        Returns:
        - int: The total number of successful requests made to the server.
        """
        pass
    
    
    def get_city_request_count(self) -> List[Tuple[str, int]]:
        """
        Get a count of requests made for each city.

        Returns:
        - List[Tuple[str, int]]: A list of tuples containing the name of the city and the number of requests made for that city.
        """
        pass