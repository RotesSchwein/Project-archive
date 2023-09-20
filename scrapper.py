import time
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://arca.live/b/gaijin'
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"}
res = requests.get(url = url, headers = headers)
soup = BeautifulSoup(res.text, 'html.parser')

def get_page_info():
    info_list = []
    # base_url = 'https://arca.live'
    list_table = soup.find_all('a', {'class': 'vrow column'})

    for info in list_table:
        _info = {
            'title': info.find('span', {'class': 'title'}).text.strip('\n'),
            'date': info.find('span', {'class': 'vcol col-time'}).text,
            'url': info.attrs.get('href')
        }
        info_list.append(_info)

    info_dataframe = pd.DataFrame(info_list)
    info_dataframe.to_csv('gaijin_info.csv')

    return info_dataframe


def temp():
    # Defining browser + adding " - headless" argument
    option = Options()
    option.add_argument(' - headless')
    driver = webdriver.Chrome(options = option)

    # URL and opening it with webdriver
    driver.maximize_window()    # Maximize the chromedriver window
    driver.get(url = url)       # Move to said link
    driver.implicitly_wait(220)    # Maximum time to load the link




print(get_page_info())
# temp()
