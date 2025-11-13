import requests
from datetime import datetime
import smtplib

MY_LAT = -26.507351 # Your latitude
MY_LONG = -100.127758 # Your Longitude
EMAIL="sivakumarviswaa19@gmail.com"
def is_iss_overhead():
    global MY_LAT, MY_LONG
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if (((MY_LAT - 5) <= iss_latitude <= (MY_LAT + 5)) and ((MY_LONG - 5) <= iss_longitude <= (MY_LONG + 5))):
        return True


def night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour
    if time_now>=sunset or time_now<=sunrise:
        return True

if night() and is_iss_overhead():
    with smtplib.SMTP("smtp.gmail.com",587) as connection:
        connection.starttls()
        connection.login(user=EMAIL,password="uimb yigr iqst rmrr")
        connection.sendmail(from_addr=EMAIL,to_addrs=EMAIL,msg="Subject:ISS ALERT\n\nLook above you right this instant")




