# International-Space-Station-ISS-overhead-notifier
A simple project that will send you an email anytime the International Space Station, also known as the ISS, passes directly overhead.

To run this app perfectly, first you need to change some code into the programmee.

<ol> Find out the latitude and longitude of the place you live in now. And then set those co-ordinates into following variables. </ol>

    MY_LAT = "Current latitude of your position"
    MY_LONG = "Current longitude of your position"

<ol> Based on the UTC, change the timezone you are currently in. For example: I live in Bangladesh, and the time zone here is UTC +6. Based on this, change the following code accordingly. </ol>
    
    sunrise_in_my_country = -24 + int(sunrise) + 6
    sunset_in_my_country = int(sunset) + 6
    
And hopefully, if you keep this code running in the IDE, you will get the mail. As the code runs in every 60 second, you won't get any immediate terminal output. Don't worry if it look stuck in the same place for hours, it's running in the background. 

And that's it. Happy coding :D
