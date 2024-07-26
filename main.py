import requests
from bs4 import BeautifulSoup

def get_nvidia_stock(nvidia_stock):
    nvidia_page = requests.get(nvidia_stock).content
    nvidia_soup = BeautifulSoup(nvidia_page, 'html.parser')
    nvidia_stock_price = nvidia_soup.find('div', class_="YMlKec fxKbKc").text.strip()[1:]
    f_nvidia_stock_price = float(nvidia_stock_price)
    print(f"NVIDIA STOCK PRICE: ${f_nvidia_stock_price}")
    return f_nvidia_stock_price

def get_amd_stock(amd_stock):
    amd_page = requests.get(amd_stock).content
    amd_soup = BeautifulSoup(amd_page, 'html.parser')
    amd_stock_price = amd_soup.find('div', class_="YMlKec fxKbKc").text.strip()[1:]
    f_amd_stock_price = float(amd_stock_price)
    print(f"AMD STOCK PRICE: $ {f_amd_stock_price}")
    return f_amd_stock_price

def compare_prices(f_get_nvidia_stock, f_get_amd_stock):
    if f_get_nvidia_stock < f_get_amd_stock:
        print("LIVE Status: AMD STOCKS' is valuable than NVIDIA STOCKS'.")
    elif f_get_nvidia_stock > f_get_amd_stock:
        print("Live Status: NVIDIA STOCKS' valuable than AMD STOCKS'.")
    elif f_get_nvidia_stock == f_get_amd_stock:
        print("Live Status: NVIDIA STOCKS' and AMD STOCKS' are same valued.")
    else:
        print("Not updated yet.")


def main():
    pass

# URLs' of stock market
nvidia = get_nvidia_stock("https://www.google.com/finance/quote/NVDA:NASDAQ?hl=en")
amd = get_amd_stock("https://www.google.com/finance/quote/AMD:NASDAQ?hl=en")
compare_prices(nvidia, amd)