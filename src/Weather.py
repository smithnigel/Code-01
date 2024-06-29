import typer
import subprocess
import time
import requests
from PyInquirer import prompt, print_json, Separator
from rich import print as rprint
from art import *
from rich.console import Console
from main import *

console = Console()

API_KEY = "08e75e70d529654e3d7dcf8f23d50c84"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
WEATHER_ICONS = {
    # day icons
    "01d": "☀️",
    "02d": "⛅️",
    "03d": "☁️",
    "04d": "☁️",
    "09d": "🌧",
    "10d": "🌦",
    "11d": "⛈",
    "13d": "🌨",
    "50d": "🌫",
    # night icons
    "01n": "🌙",
    "02n": "☁️",
    "03n": "☁️",
    "04n": "☁️",
    "09n": "🌧",
    "10n": "🌦",
    "11n": "⛈",
    "13n": "🌨",
    "50n": "🌫",
}


def url_Func(city):
    #Constructs our API
    url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=imperial"
    response = requests.get(url)
    Menu(city)
    if (response.status_code != 200):
        print("City isn't found... try again: ")
        city = input()
        url_Func(city)
    else:   
        print(f"this is the city: {city}")
        weatherRun(city, response)

def weatherRun(city, response):
    #Makes this a json file so we can grab information from our APIs database
    data = response.json()
    
    '''
    if (response.status_code == 200):
        if (city != data['name']):
            print("City isn't found... try again", time.sleep(2))
    '''

    temperature = data["main"]["temp"]
    feels_like = data["main"]["feels_like"]
    description = data["weather"][0]["description"]
    icon = data["weather"][0]["icon"]
    city = data["name"]
    country = data["sys"]["country"]
    wind = data["wind"]["speed"]

    # Construct output with weather icon
    weather_icon = WEATHER_ICONS.get(icon, "")
    output = text2art(f"\n\n\n{city}\n\n", font="big")
    output += f"{city}, {country}\n\n"
    output += f"{weather_icon} {description}\n"
    output += f"Temperature: {temperature}°F\n"
    output += f"Feels like: {feels_like}°F\n\n"
    output += f"Wind speed: {wind}mph\n\n"
    
    print(output)
    print("Enter in another city: ", end='')
    newCity= input()
    Menu(newCity)
    url_Func(newCity)