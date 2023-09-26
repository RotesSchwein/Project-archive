from selenium import webdriver
from selenium.webdriver.chrome.service import service as Chromeservice
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from pathlib import Path
import pandas as pd
import os

# driver = webdriver.Chrome()
# driver.maximize_window()  # Maximize the chromedriver window
# driver.get(url = url)  # Move to said link
# driver.implicitly_wait(220)  # Maximum time to load the link
# all_page_list_elements = driver.find_elements(By.XPATH, '/html/body/div[2]/div[3]/article/div/nav/ul/li')
# number_of_pages = int(all_page_list_elements[-2].text)

class SeleniumScrapper:
    def __init__(self):
        pass

    # Incomplete
    def get_page_info_selenium(driver):
        _info_list = []
        _list_table = driver.find_elements(By.XPATH,
                                           '//*[@class="vrow column"]/html/body/div[2]/div[3]/article/div/div[6]/div[2]/a')

        for __info in _list_table:
            ___info = {
                'title': __info.find_element(By.XPATH,
                                             '//*[@class="title"]/html/body/div[2]/div[3]/article/div/div[6]/div[2]/a[10]/div/div[1]/span[2]/span[2]').text().strip(
                    '\n')
            }
            _info_list.append(___info)

            info_dataframe = pd.DataFrame(_info_list)
            info_dataframe.to_csv('gaijin_info_alt.csv')

    @staticmethod
    def temp():
        # Defining browser + adding " - headless" argument
        driver = webdriver.Chrome()

        # URL and opening it with webdriver
        driver.maximize_window()  # Maximize the chromedriver window
        driver.get(url = url)  # Move to said link
        driver.implicitly_wait(220)  # Maximum time to load the link

        next_page = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/article/div/nav/ul/li[2]/a').click()

