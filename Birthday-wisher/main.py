import smtplib
import datetime as dt
import random

import pandas as pd

birthday = pd.read_csv("birthdays.csv")
# 2. Check if today matches a birthday in the birthdays.csv
if dt.datetime.today().month == birthday.month.values:
    if dt.datetime.today().day == birthday.day.values:
        print("Happy birthday!")

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.




