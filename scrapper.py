import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://arca.live/b/gaijin'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/116.0.0.0 Safari/537.36"}
res = requests.get(url = url, headers = headers)
soup = BeautifulSoup(res.text, 'html.parser')


class BasicScrapper:
    @staticmethod
    def get_page_info():
        info_list = []
        list_table = soup.find_all('a', {'class': 'vrow column'})

        # Save scrapped info in list
        for info in list_table:
            _info = {
                'title': info.find('span', {'class': 'title'}).text.strip('\n'),
                'date': info.find('span', {'class': 'vcol col-time'}).text.strip('\n'),
                'url': info.attrs.get('href')
            }
            info_list.append(_info)

        info_dataframe = pd.DataFrame(info_list)
        info_dataframe.to_csv('gaijin_info.csv')

        return info_dataframe
