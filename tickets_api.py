import requests
from datetime import datetime

url = "https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/browsequotes/v1.0/US/USD/en-US/SFO-sky/JFK-sky/2020-09-27"

querystring = {"inboundpartialdate":"2020-10"}

file_read = open("api-key.txt", 'r')
api_key = str(file_read.readline())
file_read.close()

headers = {
    'x-rapidapi-host': "skyscanner-skyscanner-flight-search-v1.p.rapidapi.com",
    'x-rapidapi-key': api_key
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)