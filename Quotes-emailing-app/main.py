import smtplib
import datetime as dt
import random
with open("details.txt", 'r') as mail:
    info = mail.readlines()
    user = info[0].rstrip("\n")
    psw = info[1]

my_email = f"{user}"
password = f"{psw}"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
