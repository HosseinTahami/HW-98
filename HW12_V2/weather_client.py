import requests
import weather_server
import database as db
import datetime


        
main_menu = """
Main Menu:
              
    1- Enter city name
    2- Work With database
              
"""

database_menu = """
                    
Database Menu:
                    
    1- Total Number of Requests
    2- Number of successful requests
    3- Number of Specific City Requests
    4- Last hour requests
    5- Back to Main Menu
                    
"""

def start_client(city):

    response = requests.get("http://"+f"{weather_server.HOST}:{weather_server.PORT}/{city}")
    data = response.json()
    #print(data)
    return data

            


if __name__ == '__main__' :
    
    wdb = db.WeatherDatabase()
    while True:
        print(main_menu)
        option = input("    Option: ")
        if option == '1':
            city = input("  \nEnter city name: ")
            data = start_client(city)
            wdb.save_request_data(city,datetime.datetime.now())
            wdb.save_response_data(city, data)
            if 'message' in data:
                print(f"Error: {data['message']}")
                print('---------------------------------------------------------------------------------')
            else:
                print(f'Temperature: {data["temperature"]}°C')
                print(f'Feels like: {data["feels_like"]}°C')
                print(f'Last updated: {data["last_updated"]}')
                print('---------------------------------------------------------------------------------')
        
            
        elif option == '2' :
            while True:
                print(database_menu)
                option = input("    Option: ")
                if option == '1' :
                    print("    Number of total requests: ", wdb.get_request_count())
                    print('---------------------------------------------------------------------------------')
                elif option ==  '2' :
                    print("    Number of successful requests: ", wdb.get_successful_request_count())
                    print('---------------------------------------------------------------------------------')
                elif option == '3' :
                    print("    Number of requests by city: \n")
                    requests_list = wdb.get_city_request_count()
                    for city in requests_list :
                        print("    ", city)
                    print('---------------------------------------------------------------------------------')
                elif option == '4' :
                    
                    wdb.get_last_hour_requests()             
                elif option == '5' :
                    break;
                else :
                    print(" Wrong Option Choose Again !")
                
        else :
            print(" Wrong option Choose Again !")
    