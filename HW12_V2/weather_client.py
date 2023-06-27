import requests
import weather_server
import database as db
import datetime


def start_client(city):

    response = requests.get("http://"+f"{weather_server.HOST}:{weather_server.PORT}/{city}")
    data = response.json()
    print(data)
    if 'message' in data:
        print(f"Error: {data['message']}")
        print('---------------------------------------------------------------------------------')
    else:
        print(f'Temperature: {data["temperature"]}°C')
        print(f'Feels like: {data["feels_like"]}°C')
        print(f'Last updated: {data["last_updated"]}')
        print('---------------------------------------------------------------------------------')
            


if __name__ == '__main__' :
    while True:
        print("""
              Main Menu:
              
              1- Enter city name
              2- Work With database
              
              """)
        option = int(input("Option: "))
        if option == 1:
            city = input("\nEnter city name: ")
            start_client(city)
            db.WeatherDatabase.save_request_data(city,datetime.datetime.now())
        elif option == 2 :
            while True:
                print("""
                    
                    Database Menu:
                    
                    1- Total Number of Requests
                    2- Number of successful requests
                    3- Last hour requests
                    4- Number of Specific City Requests
                    
                    """)
                option = int(input("Option: "))
                if option == 1 :
                    pass
                elif option ==  2 :
                    pass
        else :
            print("Wrong option Choose Again !")
    