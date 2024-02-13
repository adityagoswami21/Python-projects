import smtplib
import datetime as dt
import random

import pandas as pd

birthday = pd.read_csv("birthdays.csv")
today_month = dt.datetime.today().month
today_day = dt.datetime.today().day
# 2. Check if today matches a birthday in the birthdays.csv
for index, row in birthday.iterrows():
    name = row["name"]
    if today_month == row["month"] and today_day == row["day"]:
        with open("letter_templates/letter_1.txt") as body:
            content_read = body.read()
            content_edit = content_read.replace("[NAME]", name)
            print(content_edit)


# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.




