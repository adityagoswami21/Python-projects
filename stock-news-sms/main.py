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

data_list = [value for (key,value) in data.items()]

yesterday_close_price = float(data_list[0]["4. close"])

day_before_yesterday_price = float(data_list[1]["4. close"])

difference = day_before_yesterday_price - yesterday_close_price

indicator = None
if difference > 0:
    indicator = "🔺"
else:
    indicator = "🔻"


difference_percentage = round((abs(difference)/yesterday_close_price)*100)


if difference_percentage > 1:
    response = requests.get(NEWS_ENDPOINT, news_params)
    news_data = response.json()['articles'][:3]
    
    msg_body =[f"{STOCK} {indicator} {difference_percentage}% \nHeadline: {article['title']}. \nBrief: {article['description']}" for article in news_data]

    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']
    client = Client(account_sid, auth_token)
    
    for article in msg_body:
        message = client.messages \
                        .create(
                            body=article,
                            from_=os.environ['FROM_NUM'],
                            to=os.environ['TO_NUM']
                        )

        print(message.sid)


