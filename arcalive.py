import requests
import datetime
from bs4 import BeautifulSoup
from selenium import webdriver

base_url = 'https://arca.live'
url = 'https://arca.live/b/gaijin'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
}


def get_Page(pages, date):
    for page in range(pages):
        _url = url + '?p=' + str(page)
        response = requests.get(url = _url, headers = headers)
        soup = BeautifulSoup(response.text, 'html.parser')

        # 글 제목을 추출
        for tag in soup.select('span.vcol.col-title > span.title'):
            _title = tag.text
            return _title

        # 글 링크를 추출
        for href in soup.select('a.vrow.column'):
            _url = href.attrs.get('href')

            if _url is None:
                continue
            else:
                return base_url + _url

        # 글 작성일을 추출
        for _element in soup.select('span.vcol.col-time'):
            if _element.text == '작성일':
                continue
            _time_element = _element.select_one("time").text
            return _time_element


def input_Pages():
    _input = input("Type in the number pages you want to scrap: ")
    return int(_input)


get_Page(input_Pages())
