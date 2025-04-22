import requests
#
# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
#
# data = response.json()
# print(data)
#
# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]
#
# iss_position = (longitude, latitude)
#
# print(iss_position)
# # error code meanings:
# # 1XX: Hold on
# #  2XX: Here you go
# # 3XX: Go Away
# # 4XX: You Screwed up
# # 5XX: I Screwed Up

MY_LAT = 33.862770
MY_LONG = -118.002518
TIMEZONE = "America/Los_Angeles"
parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted" : 0,
    "tzid" : TIMEZONE
}

RESPONSE = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
RESPONSE.raise_for_status()
data = RESPONSE.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"]

print(sunrise.split("T"))