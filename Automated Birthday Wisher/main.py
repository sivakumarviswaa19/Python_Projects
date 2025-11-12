##################### Hard Starting Project ######################

# 1. Update the birthdays.csv with your friends & family's details. 
# HINT: Make sure one of the entries matches today's date for testing purposes. 

# 2. Check if today matches a birthday in the birthdays.csv
# HINT 1: Only the month and day matter. 
# HINT 2: You could create a dictionary from birthdays.csv that looks like this:
# birthdays_dict = {
#     (month, day): data_row
# }
#HINT 3: Then you could compare and see if today's month/day matches one of the keys in birthday_dict like this:
# if (today_month, today_day) in birthdays_dict:

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# HINT: https://www.w3schools.com/python/ref_string_replace.asp

# 4. Send the letter generated in step 3 to that person's email address.
# HINT: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)

import smtplib
import datetime as dt
import pandas as pd
import random
import os
os.chdir("/home/Viswaa/Birthday_Wisher")

details = {}
data1 = pd.read_csv("/home/Viswaa/Birthday_Wisher/birthdays.csv")
for index,row in data1.iterrows():
    key = (row["month"],row["day"])
    details[key] = {
        "name":row["name"],
        "email":row["email"]
    }

d = dt.datetime.now()
tdy = d.day
tdm = d.month

no = random.randint(1,3)

if (tdm,tdy) in details:
    with open(f"letter_{no}.txt","r") as f:
        x = f.read()
        y = x.replace("[NAME]",details[(tdm,tdy)]["name"])

    with smtplib.SMTP("smtp.gmail.com",587) as connection:
        connection.starttls()
        connection.login(user="sivakumarviswaa19@gmail.com",password="uimb yigr iqst rmrr")
        connection.sendmail(from_addr="sivakumarviswaa19@gmail.com",to_addrs=details[(tdm,tdy)]["email"],msg=f"Subject: Happy Birthday!\n\n{y}")
print("Script Completed!")


