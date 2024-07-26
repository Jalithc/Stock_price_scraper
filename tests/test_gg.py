import requests
from bs4 import BeautifulSoup

# Test NVIDIA CORP stock price
URL = "https://www.google.com/finance/quote/NVDA:NASDAQ?hl=en"
page = requests.get(URL).content

soup = BeautifulSoup(page, 'html.parser')
price = soup.find('div', class_="YMlKec fxKbKc").text.strip()[1:]
print(float(price))
