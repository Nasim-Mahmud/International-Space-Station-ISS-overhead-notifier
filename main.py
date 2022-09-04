import requests
from datetime import datetime as dt
from smtplib import *
import time

# The longitude and latitude of my current position.
MY_LAT = 23.810331
MY_LONG = 90.412521


def iss_overhear():
    # Importing API endpoint
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()

    data = response.json()
    iss_longitude = float(data["iss_position"]["longitude"])
    iss_latitude = float(data["iss_position"]["latitude"])
    # If the ISS is close to my current position
    if (MY_LAT - 5) <= iss_latitude <= (MY_LAT + 5) and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        return True



# Sunset time
parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}


# Detecting darkness outside.
def is_dark_outside():
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()

    # Time will be shown as UTC time zone
    data = response.json()
    sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
    sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

    # Optional: Sunrise and sunset time based on my location (Which is Dhaka, Bangladesh: GMT +6)
    sunrise_in_my_country = -24 + int(sunrise) + 6
    sunset_in_my_country = int(sunset) + 6
    time_now = dt.now().hour
    if time_now >= sunset_in_my_country or time_now <= sunrise_in_my_country:
        return True


while True:
    # Runs the code in every 60 seconds.
    time.sleep(60)

    if iss_overhear() and is_dark_outside():
        my_email = "tmailone01@gmail.com"
        my_pass = "rteqejuqqdhcgpzx"                        # Not the actual password.

        receivers_email = "tmailtwo02@yahoo.com"

        with SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_pass)
            connection.sendmail(from_addr=my_email, to_addrs=receivers_email,
                                msg="Subject: LOOK UP! IT's the ISS\n\n"
                                    "Hey Buddy, Go outside and look up into the sky. Can you see"
                                    "the International Space Station? Isn't that amazing!"
                                )
