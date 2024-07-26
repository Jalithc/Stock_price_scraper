import requests
from bs4 import BeautifulSoup

# Test AMD stock price
URL = "https://finance.yahoo.com/quote/AMD/"
page = requests.get(URL).content

soup = BeautifulSoup(page, 'html.parser')
price = soup.find('fin-streamer', class_="livePrice yf-mgkamr").text.strip()
print(f"${price}")
