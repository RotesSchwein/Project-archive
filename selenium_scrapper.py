from selenium import webdriver
from selenium.webdriver.chrome.service import service as Chromeservice
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from pathlib import Path
from datetime import datetime
import time
import pandas as pd
import os
import re

from selenium_browser import browser_driver

'''
    What I have to do.
    1. 셀레니움을 통해 크롬 드라이버를 오픈
    2. 셀레니움을 통해 스크랩을 시작할 시간대를 설정
    3. 페이지를 넘어가면서 시간대 조건에 맞는 글을 스크랩
'''

option = Options()
option.add_experimental_option('detach', True)


class ArticleContent:
    Title: str
    Date: str
    URI: str


class SeleniumScrapper:

    """
    This method is for getting a wanted time period
    as a string type
    """
    @staticmethod
    def get_time_period():
        time_period = input("Select a time period to scrap: ")
        return time_period

    """
    This method is for moving to the page that has been
    set to a certain time period
    """
    @staticmethod
    def go_to_page_of_a_certain_time_period(time_period):
        driver = webdriver.Chrome(options = option)
        driver.implicitly_wait(10)

        driver.get(f'https://arca.live/b/gaijin?near={time_period}T00%3A00&tz=%2B0900')

    """
    This method is to scrap the content from a time period
    that had been set from the method above
    """
    def scrap_content_in_said_time_period(self):
        driver = webdriver.Chrome(options = option)
        info_list = []
        list_table = driver.find_elements(By.CLASS_NAME, 'vrow column')
        for info in list_table:
            article_info_list = ArticleContent(

            )
        print(list_table)

    # @staticmethod
    # def click_to_next_page():
    #     driver = webdriver.Chrome(options = option)
    #     driver.implicitly_wait(10)
    #


    #     action = webdriver.ActionChains(driver = driver)
    #
    #     driver.get('https://arca.live/b/gaijin/')
    #
    #     for _i in range(1, 10):
    #         link = driver.find_element(By.XPATH, f'/html/body/div[2]/div[3]/article/div/nav/ul/li[{_i}]/a')
    #         link.click()
    #         action.pause(1)
    #         action.perform()

if __name__ == '__main__':
    date_time = SeleniumScrapper.get_time_period()
    SeleniumScrapper.go_to_page_of_a_certain_time_period(date_time)
    # SeleniumScrapper.click_to_next_page()
