import requests
from datetime import datetime as dt

MY_LAT = 23.810331
MY_LONG = 90.412521

# # Importing API endpoint
# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
#
# data = response.json()
# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]
#
# iss_position = (latitude, longitude)
# print(iss_position)

# Sunset time

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()

# Time will be shown as UTC time zone
data = response.json()
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]

print(sunrise)
print(sunrise.split("T")[1].split(":"))
# time_now = dt.now()
# print(time_now)