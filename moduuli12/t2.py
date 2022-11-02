import requests
from geopy.geocoders import Nominatim

APIKEY = "YOUR-API-KEY-HERE"

user_location = input("Enter a city, locality or district to get the current weather data: ")

geolocator = Nominatim(user_agent="geopyAPI", timeout=3)
location = geolocator.geocode(str(user_location))

req = "https://api.openweathermap.org/data/2.5/weather?lat=" + str(location.latitude) + "&lon=" \
      + str(location.longitude) + "&appid=" + APIKEY + "&units=metric"
ans = requests.get(req).json()

print(user_location.capitalize() + " weather data:\n")
print("Weather: " + ans["weather"][0]["main"] + "\nDescription: " + ans["weather"][0]["description"])
print("Temperature: " + str(ans["main"]["temp"]) + " °C, feels like " + str(ans["main"]["feels_like"]) + " °C")
print("Country: " + str(ans["sys"]["country"]))
