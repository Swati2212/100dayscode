import requests
import lxml
from bs4 import BeautifulSoup
import smtplib

SMTP_ADDRESS = "smtp.gmail.com"
EMAIL = YOUR EMAIL ID
PASSWORD = YOUR PASSWORD

URL = "https://www.amazon.in/New-Apple-iPhone-12-128GB/dp/B08L5TNJHG/ref=sr_1_1_sspa?dchild=1&keywords=iphone+12&qid=1625120577&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExR1oxTDI5S0swWFZFJmVuY3J5cHRlZElkPUEwNjU3MTU3M0lQQUIxQTVPWTRBNyZlbmNyeXB0ZWRBZElkPUEwMzI0NDAwMUZXTThSRlVWWEZBUyZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU="
header = {
    'Accept-Language' : 'en-US,en;q=0.9',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'

}
response = requests.get(url=URL, headers = header)

soup = BeautifulSoup(response.content, 'lxml')
# print(soup.prettify())

price = soup.find(id="priceblock_ourprice").getText()
price_without_currency = price.split("₹")[1]
price_without_comma = price_without_currency.replace(",", '')
price_as_float = float(price_without_comma)
print(price_as_float)

title = soup.find(id = "productTitle").getText().strip()
print(title)

BUY_PRICE = 85000

if price_as_float < BUY_PRICE:
    message = f"{title} is now {price}"
    # print(message)

    with smtplib.SMTP(SMTP_ADDRESS,port=587) as connection:
        connection.starttls()
        result = connection.login(EMAIL, PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=EMAIL,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{URL}".encode("utf-8")
        )
