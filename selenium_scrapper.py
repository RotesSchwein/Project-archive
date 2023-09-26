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

# driver = webdriver.Chrome()
# driver.maximize_window()  # Maximize the chromedriver window
# driver.get(url = url)  # Move to said link
# driver.implicitly_wait(220)  # Maximum time to load the link
# all_page_list_elements = driver.find_elements(By.XPATH, '/html/body/div[2]/div[3]/article/div/nav/ul/li')
# number_of_pages = int(all_page_list_elements[-2].text)

# Defining browser + adding " - headless" argument
PATH = 'C:\Windows\chromedriver.exe'

options = Options()
options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options = options)
driver.implicitly_wait(10)


class SeleniumScrapper:
    def __init__(self):
        pass

    # Incomplete
    def get_page_info_selenium(self):
        pass

    @staticmethod
    def click_to_next_page():
        driver.get('https://arca.live/b/gaijin/')

        link = driver.find_element(By.LINK_TEXT, '개념글')
        link.click()
