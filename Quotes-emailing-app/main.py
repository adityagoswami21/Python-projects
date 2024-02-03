import smtplib
import datetime as dt
import random
my_email = ""
password = ""

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
