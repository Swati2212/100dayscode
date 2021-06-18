import requests
from twilio.rest import Client


STOCK_NAME = "AAPL"
COMPANY_NAME = "Apple Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = 'https://newsapi.org/v2/everything'

STOCK_API_key = 'R8RU8BTFDOI4SSMN'
NEWS_API_KEY = 'b4f4019d6ef443d0997a6e49c71905f5'

TWILIO_API = 'AC2b1b3c6eb241675f13f6ef3d7edacd82'
TWILIO_AUTH_TOKEN = '97c92eb730f872124c799550d51515dc'

stock_params = {
    'function': 'TIME_SERIES_DAILY',
    'symbol': STOCK_NAME,
    'apikey': STOCK_API_key
}
response = requests.get(STOCK_ENDPOINT, params=stock_params)
response.raise_for_status()

data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data['4. close']

day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data['4. close']

difference = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)

up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

diff_percent = round((difference / float(yesterday_closing_price)) * 100)

if abs(diff_percent) >= 1:
    news_params = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME,
    }
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()["articles"]
    print(articles)

    # slicing over first 3 articles
    three_articles = articles[:3]
    print(three_articles)

    formatted_article = [f"{STOCK_NAME} : {up_down}{diff_percent}%\n Headline:{article['title']}. \n Brief:{article['description']}" for article in three_articles]
    print(formatted_article)

    client = Client(TWILIO_API, TWILIO_AUTH_TOKEN)
    for article in formatted_article:
        message = client.messages.create(
            body=article,
            from_='+14805269315',
            to=''
        )
