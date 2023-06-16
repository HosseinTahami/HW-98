import requests

def url_request(url):
    response = requests.get(url)
    return response.json()

url_users = "https://jsonplaceholder.typicode.com/users"

def process_json(response):
    users = []
    for i,user in enumerate(response):
        users.append(user.get('username'))
        print(i+1,"-",user.get('username'))

process_json(url_request(url_users))
