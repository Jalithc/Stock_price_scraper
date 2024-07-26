import requests
from bs4 import BeautifulSoup
import schedule
import time

# Test NVIDIA CORP stock price
URL = "https://www.google.com/finance/quote/AMD:NASDAQ?hl=en"
page = requests.get(URL).content

def get_amd_price():
    soup = BeautifulSoup(page, 'html.parser')
    price = soup.find('div', class_="YMlKec fxKbKc").text.strip()[1:]
    print(float(price))

schedule.every(5).seconds.do(get_amd_price)

while True:
    schedule.run_pending()
    time.sleep(1)
