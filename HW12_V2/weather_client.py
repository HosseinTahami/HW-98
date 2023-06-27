import requests
import weather_server
import database as db
import datetime


def start_client(city):

    response = requests.get("http://"+f"{weather_server.HOST}:{weather_server.PORT}/{city}")
    data = response.json()
    print(data)
    return data

            


if __name__ == '__main__' :
    
    wdb = db.WeatherDatabase()
    while True:
        
        main_menu = """
Main Menu:
              
    1- Enter city name
    2- Work With database
              
"""
        database_menu = """
                    
Database Menu:
                    
    1- Total Number of Requests
    2- Number of successful requests
    3- Last hour requests
    4- Number of Specific City Requests
    5 - Back to Main Menu
                    
                    """
        print(main_menu)
        option = int(input("    Option: "))
        if option == 1:
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
        
            
        elif option == 2 :
            while True:
                print()
                option = int(input("    Option: "))
                if option == 1 :
                    print("Number of total requests: ", wdb.get_request_count())
                elif option ==  2 :
                    pass
                elif option == 3 :
                    pass
                elif option == 4 :
                    pass
                elif option == 5 :
                    break;
                else :
                    print(" Wrong Option Choose Again !")
                
        else :
            print(" Wrong option Choose Again !")
    