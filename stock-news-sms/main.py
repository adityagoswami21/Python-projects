import requests
import os
from dotenv import load_dotenv
import os
from twilio.rest import Client

load_dotenv()
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol":STOCK,
    "apikey": os.getenv("STOCK_API"),
    "outputsize": 2

}

news_params = {
    "q":COMPANY_NAME,
    "apiKey":os.getenv("NEWS_API")
}

response = requests.get(STOCK_ENDPOINT, stock_params)
data = response.json()['Time Series (Daily)']
# print(data)
data_list = [value for (key,value) in data.items()]
# print(data_list)
yesterday_close_price = float(data_list[0]["4. close"])
# print(yesterday_close_price)
day_before_yesterday_price = float(data_list[1]["4. close"])
# print(day_before_yesterday_price)
difference = abs(day_before_yesterday_price - yesterday_close_price)
# print(difference)
difference_percentage = (difference/yesterday_close_price)*100
# print(difference_percentage)

if difference_percentage > 1:
    response = requests.get(NEWS_ENDPOINT, news_params)
    news_data = response.json()['articles'][:3]
    # print(news_data[0]['title'])




## STEP 3: Use twilio.com/docs/sms/quickstart/python
# Send a separate message with each article's title and description to your phone number. 
#HINT 1: Consider using a List Comprehension.
# Download the helper library from https://www.twilio.com/docs/python/install

    msg_body = news_data[0]['title']
    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']
    client = Client(account_sid, auth_token)

    message = client.messages \
                    .create(
                        body=msg_body,
                        from_=os.environ['FROM_NUM'],
                        to=os.environ['TO_NUM']
                    )

    print(message.sid)



#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

