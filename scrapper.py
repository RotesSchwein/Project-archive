import requests
from bs4 import BeautifulSoup
from dataclasses import dataclass
import pandas as pd

url = 'https://arca.live/b/gaijin'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/116.0.0.0 Safari/537.36"}


@dataclass
class ArticleContent:
    Title: str
    Date: str
    URI: str


class BasicScrapper:
    def __init__(self, page):
        self.page = page


    @staticmethod
    def get_page_info():
        _requests = requests.get(url = url, headers = headers)
        _soup = BeautifulSoup(_requests.text, 'html.parser')

        info_list = []
        # Find article title, date, and uri in article preview page
        list_table = _soup.find_all('a', {'class': 'vrow column'})

        # Save scrapped info in list
        for info in list_table:
            article_info_list = ArticleContent(
                Title = info.find('span', {'class': 'title'}).text.strip('\n'),
                Date = info.find('span', {'class': 'vcol col-time'}).text.strip('\n'),
                URI = info.attrs.get('href')
            )
            info_list.append(article_info_list)

        info_dataframe = pd.DataFrame(info_list)
        info_dataframe.to_csv('gaijin_channel_info.csv')

        return info_dataframe

    def get_multiple_page_info(self):
        modified_uri = url + "?p=" + str(self.page)

        for _i in range(self.page):
            print(modified_uri)

