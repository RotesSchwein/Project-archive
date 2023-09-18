import requests
from bs4 import BeautifulSoup
import pandas as pd

# Global variable
base_url = 'https://arca.live/b/gaijin'
url_list = [base_url, ]
pages = []
soup_list = []
not_last_page = True


# Pull requests
def pullUrl(func):
    def inner(*args, **kwargs):
        _pages = requests.get(url_list[-1])
        if _pages.status_code == 200:
            pages.append(pages)
            func(*args, **kwargs)
        else:
            print(f"The url {url} returned a status of Page.status.code")

    return inner


# Make some soup
def makeSoup(func):
    def inner(*args, **kwargs):
        soup = BeautifulSoup(pages[-1].content, 'html.parser')
        soup_list.append(soup)
        func(*args, **kwargs)

    return inner


# Parse url
@pullUrl
@makeSoup
def getURLs():
    global not_last_page
    try:
        next_page = url + soup_list[-1].find('li', {'class': 'page-item'}).find('a')['href']
        print(next_page)
        url_list.append(next_page)
    except:
        not_last_page = False


while not_last_page:
    getURLs()
