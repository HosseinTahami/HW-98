import requests

url = 'https://my-json-server.typicode.com/horizon-code-academy/fake-movies-api/movies'
response = requests.get(url)
print(response.status_code)
movies = response.json()
for i,movie in enumerate(movies):
    i+=1
    print(str(i)+"-",movie)
    
title = input("\nEnter title of the movie: ")
year = input("Enter year of recording: ")
genre = input("Enter genre of the movie: ")
summary = input("Enter summary of the movie: ")
new_movie = {"id": 0, "Title": title, "Year": year, "Genre": genre, "Summary": summary}

response = requests.post(url,new_movie)
print(response.status_code)
print(response.content)
print(response.headers)

#https://stackoverflow.com/questions/52030845/json-server-getting-error-after-post-request