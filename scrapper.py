from dataclasses import dataclass

import pandas as pd
import requests
import re
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


url = 'https://arca.live/b/gaijin'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/116.0.0.0 Safari/537.36"}


@dataclass
class ArticleContent:
    Title: str
    Date: str
    URL: str


class BasicScrapper:
    @staticmethod
    def get_time_period():
        time_period = input("Select a time period to scrap: ")
        return time_period

    def get_page_info(time_period):

        option = Options()
        # option.add_argument("--headless=new")
        # option.add_experimental_option('detach', True)

        driver = webdriver.Chrome(options = option)
        driver.implicitly_wait(10)

        driver.get(f'https://arca.live/b/gaijin?near={time_period}T00%3A00&tz=%2B0900')

        _requests = requests.get(url = url, headers = headers)
        _soup = BeautifulSoup(driver.page_source, 'html.parser') # Import HTML code via selenium driver, then use parse html code from BS for better speed
        info_list = []
        list_table = _soup.find_all('a', {'class': 'vrow column'})
        next_page = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/article/div/nav/ul/li[6]/a')

        # Save scrapped info in list
        for info in list_table:
            written_date = info.find('span', {'class': 'vcol col-time'}).text.strip('\n')
            r_written_date = re.sub(r'[^0-9]', '', written_date)
            r_time_period = re.sub(r'[^0-9]', '', time_period)

            # If there is an article that has been written on a different date in the same page
            # exclude it
            if r_written_date != r_time_period:
                continue
            elif r_written_date == r_time_period:
                article_info_list = ArticleContent(
                    Title = info.find('span', {'class': 'title'}).text.strip('\n'),
                    Date = info.find('span', {'class': 'vcol col-time'}).text.strip('\n'),
                    URL = 'https://arca.live' + info.attrs.get('href')
                )
                info_list.append(article_info_list)

            next_page.click()

        info_dataframe = pd.DataFrame(info_list)
        info_dataframe.to_csv(f'gaijin_channel_{time_period}_info.csv')

        print(info_dataframe)

    def go_through_pages(time_period):
        option = Options()

        driver = webdriver.Chrome(options = option)
        driver.implicitly_wait(10)

        driver.get(f'https://arca.live/b/gaijin?near={time_period}T00%3A00&tz=%2B0900')

        page_info_table = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/article/div/nav/ul/li[6]/a')

        page_info_table.click()
