import os
import smtplib
import datetime as dt
import random

import pandas as pd

birthday = pd.read_csv("birthdays.csv")
today_month = dt.datetime.today().month
today_day = dt.datetime.today().day
letters_dir = "letter_templates"
letters = os.listdir("letter_templates")
random_letter = random.choice(letters)
# 2. Check if today matches a birthday in the birthdays.csv
for index, row in birthday.iterrows():
    name = row["name"]
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with
# the person's actual name from birthdays.csv
    if today_month == row["month"] and today_day == row["day"]:
        with open(os.path.join(letters_dir, random_letter)) as body:
            content_read = body.read()
            content_edit = content_read.replace("[NAME]", name)
            print(content_edit)

# 4. Send the letter generated in step 3 to that person's email address.

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()



