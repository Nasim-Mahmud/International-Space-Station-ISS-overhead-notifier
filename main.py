import requests
from datetime import datetime as dt

MY_LAT = 23.810331
MY_LONG = 90.412521

# Importing API endpoint
response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()

data = response.json()
iss_longitude = float(data["iss_position"]["longitude"])
iss_latitude = float(data["iss_position"]["latitude"])

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
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

# Optional: Sunrise and sunset time based on my location (Which is Dhaka, Bangladesh: GMT +6)
sunrise_in_my_country = -24 + int(sunrise) + 6
sunset_in_my_country = int(sunset) + 6
# print(sunrise_in_my_country)
# print(sunset_in_my_country)
time_now = dt.now()
# print(time_now.hour)

# If the ISS is close to my current position
if (MY_LAT-5) <= iss_latitude <= (MY_LAT+5) and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
    print("Yes")
else:
    print("No")

# And it is dark
# Then send me an email to tell me to look up.
# Run the code in every 60 seconds.
