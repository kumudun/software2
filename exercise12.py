# Question 1

import requests

import json


server = "https://api.chucknorris.io"
request = server + "/jokes/random"

try:
    response = requests.get(request).json()
    #print(json.dumps(response, indent=2))
    print(response["value"])
except requests.exceptions.RequestException as e:
    print("Request could not be completed", e)



# Question 2
from datetime import datetime
import requests

from Ex12_apikey import open_weather_key

def open_weathermap(city):
    server = "https://api.openweathermap.org"
    request = server + "/date/2.5/weather"+ "?q=" + city + "&appid" +open_weather_key()
    response = requests.get(request)
    return response.status_code,requests.get(request).json()

def temp_in_celsius(kelvin):
    return kelvin - 273.15

city = input("Which city do you want to check the weather?")

try:
    (result,data) = open_weathermap(city)
    if result == 200:
        print(f"Current weather:{data['weather'][0]['description']},"
             f"Temperature:{temp_in_celsius(data['main']['temp']):.1f},")
    elif result == 401:
        print("Not valid API key")
    elif result == 404:
        print("No weather information for" + city)
    else:
        print("Unknown response code" + str(result))

except requests.exceptions.RequestException as e:
    print("Request could not be completed")









