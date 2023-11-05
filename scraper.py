"""import re
import time
from dataclasses import dataclass

import mysql.connector
import pandas as pd
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

url = 'https://arca.live/b/gaijin'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/116.0.0.0 Safari/537.36"}


@dataclass
class ArticleContent:
    # ID: str
    Title: str
    Date: str
    URL: str


class BasicScrapper:
    @staticmethod
    def get_time_period():
        time_period = input("Select a time period to scrap: ")
        return time_period

    # def insert_data_to_db(self, data):
    #     try:
    #         connection = mysql.connector.connect(
    #             host = '',
    #             user = 'admin',
    #             password = '',
    #             database = 'scraperDB',
    #             port = 3306
    #         )
    #         cursor = connection.cursor()
    #
    #         for item in data:
    #             sql = 'INSERT INTO gaijin_channel_article_info (article_title, article_written_time, article_url) VALUES (%s, %s, %s)'
    #             values = (item.Title, item.Date, item.URL)
    #             cursor.execute(sql, values)
    #
    #         connection.commit()
    #         cursor.close()
    #         connection.close()
    #     except mysql.connector.Error as error:
    #         print(f"Error : {error}")

    def get_page_info(time_period):
        option = Options()
        # option.add_argument("--headless=new")
        # option.add_experimental_option('detach', True)

        driver = webdriver.Chrome(options = option)
        driver.implicitly_wait(10)
        driver.get(f'https://arca.live/b/gaijin?near={time_period}T00%3A00&tz=%2B0900')

        while True:
            _requests = requests.get(url = url, headers = headers)
            _soup = BeautifulSoup(driver.page_source,
                                  'html.parser')  # Import HTML code via selenium driver, then use parse html code from BS for better speed

            driver.get(str('https://arca.live' + _soup.find('li', {'class': 'page-item active'}).find("a", {
                "class": "page-link"}).attrs.get('href')))

            info_list = []
            list_table = _soup.find_all('a', {'class': 'vrow column'})
            next_page = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/article/div/nav/ul/li[6]/a')
            # Save scrapped info in list
            for info in list_table:

                written_date = info.find('span', {'class': 'vcol col-time'}).text.strip('\n')
                r_written_date = re.sub(r'[^0-9]', '', written_date)
                r_time_period = re.sub(r'[^0-9]', '', time_period)

                # If an article has been written prior to the set time period
                # exclude it
                if int(r_written_date) < int(r_time_period):
                    continue
                # If an article has been written after to the set time period
                # end the cycle
                elif int(r_written_date) > int(r_time_period):
                    break
                elif r_written_date == r_time_period:
                    article_info_list = ArticleContent(  # 아카라이브 글 아이디도 포함할것(만일의 상황에서 같은 데이터가 중복되는 상황을 방지)
                        # ID = info.find('span', {'class': 'vcol col-id'}).text.strip('\n'),
                        Title = info.find('span', {'class': 'title'}).text.strip('\n'),
                        Date = info.find('span', {'class': 'vcol col-time'}).text.strip('\n'),
                        URL = info.attrs.get('href')
                    )
                    info_list.append(article_info_list)
                    # insert_data_to_db(info_list)
                    info_dataframe = pd.DataFrame(info_list)
                    info_dataframe.to_csv(f"{time_period}.csv")
                    print(info_dataframe)

                # insert_data_to_db(info_list)
            else:
                # Scroll down to the bottom in order to access next page
                time.sleep(2)
                driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
                # Click to the next page section
                time.sleep(2)
                next_page.click()
                continue
            break"""  # 플래그를 세워서 제동을 걸것(코드유지보수 면에서 우월)

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import pandas as pd
from bs4 import BeautifulSoup
import re
import requests
from collections import namedtuple

ArticleContent = namedtuple('ArticleContent', ['Title', 'Date', 'URL'])

def get_page_info(time_period):
    option = Options()
    # option.add_argument("--headless=new")
    # option.add_experimental_option('detach', True)
    driver = webdriver.Chrome(options = option)
    driver.implicitly_wait(10)
    driver.get(f'https://arca.live/b/gaijin?near={time_period}T00%3A00&tz=%2B0900')
    while True:
        _soup = BeautifulSoup(driver.page_source, 'html.parser')
        info_list = []
        list_table = _soup.find_all('a', {'class': 'vrow column'})
        for info in list_table:
            written_date = info.find('span', {'class': 'vcol col-time'}).text.strip('\n')
            r_written_date = re.sub(r'[^0-9]', '', written_date)
            r_time_period = re.sub(r'[^0-9]', '', time_period)
            if int(r_written_date) < int(r_time_period):
                continue
            elif int(r_written_date) > int(r_time_period):
                break
            elif r_written_date == r_time_period:
                article_info_list = ArticleContent(
                    Title = info.find('span', {'class': 'title'}).text.strip('\n'),
                    Date = info.find('span', {'class': 'vcol col-time'}).text.strip('\n'),
                    URL = info.attrs.get('href')
                )
                info_list.append(article_info_list)
        if info_list:
            info_dataframe = pd.DataFrame(info_list)
            info_dataframe.to_csv(f"{time_period}.csv", mode = 'a', header = False)  # Append data to the CSV file
            print(info_dataframe)
        try:
            next_page = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/article/div/nav/ul/li[6]/a')
            time.sleep(2)
            driver.execute_script('arguments[0].scrollIntoView(true);', next_page)
            time.sleep(2)
            next_page.click()
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            break
    driver.quit()

