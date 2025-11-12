import datetime as dt
import smtplib
import random

now = dt.datetime.now()
day = now.weekday()
EMAIL="sivakumarviswaa19@gmail.com"
import os
os.chdir("/home/Viswaa/Motivation")
if day==2: #monday to sunday are numbered as 0 to 6
    with open("/home/Viswaa/Motivation/quotes.txt", "r") as f:
        x=f.readlines()
        quote = random.choice(x)

    with smtplib.SMTP("smtp.gmail.com",587) as connection:
        connection.starttls()
        connection.login(user=EMAIL,password="uimb yigr iqst rmrr")
        connection.sendmail(from_addr=EMAIL,to_addrs=EMAIL,msg=f"Subject: Today's Quote\n\n{quote}")
print("Completed Successfully!")
        