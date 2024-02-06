import smtplib
import datetime as dt
import random
with open("details.txt", 'r') as mail:
    info = mail.readlines()
    user = info[0].rstrip("\n")
    psw = info[1]
    fnd = info[2]

MY_EMAIL = f"{user}"
PASSWORD = f"{psw}"
FRIEND = fnd

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=MY_EMAIL, password=PASSWORD)
    if dt.datetime.today().weekday() == 0:
        quotes = open("quotes.txt")
        quote = quotes.readlines()
        motivation = random.choice(quote)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=FRIEND, msg=f"Subject:Monday Motivation!\n\n{motivation}")
