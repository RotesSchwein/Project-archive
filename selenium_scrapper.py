from dataclasses import dataclass

import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

'''
    What I have to do.
    1. 셀레니움을 통해 크롬 드라이버를 오픈
    2. 셀레니움을 통해 스크랩을 시작할 시간대를 설정
    3. 페이지를 넘어가면서 시간대 조건에 맞는 글을 스크랩
'''

option = Options()
# option.add_argument("--headless=new")

# option.add_experimental_option('detach', True)

@dataclass
class ArticleContent:
    Title: str
    Date: str


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
    def go_to_page_of_a_certain_time_period(time_period):
        driver = webdriver.Chrome(options = option)
        driver.implicitly_wait(10)

        driver.get(f'https://arca.live/b/gaijin?near={time_period}T00%3A00&tz=%2B0900')

    """
    This method is to scrap the content from a time period
    that had been set from the method above
    """
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


def scrap_content_in_said_time_period(time_period):
    driver = webdriver.Chrome(options = option)
    driver.implicitly_wait(10)

    driver.get(f'https://arca.live/b/gaijin?near={time_period}T00%3A00&tz=%2B0900')
    _bs = BeautifulSoup("html.parser", driver.page_source)
    _bs
    vrow_column = driver.find_elements(By.CSS_SELECTOR, 'a:nth-child(10)')

    for _element in driver.find_elements(By.CSS_SELECTOR, 'div .vrow-inner'):
        print(_element)


    # title_table = list_table.find_element(By.CSS_SELECTOR, 'span.title')

    info_list = []

    for i in range(1, 46):
        for info in vrow_column:
            article_info_list = ArticleContent(
                Title = info.find_element(By.XPATH, f'/html/body/div[2]/div[3]/article/div/div[6]/div[2]/a[{i}]/div[1]/div[1]/span[2]/span[2]').text.strip('\n'),
                Date = info.find_element(By.XPATH, f'/html/body/div[2]/div[3]/article/div/div[6]/div[2]/a[{i}]/div/div[2]/span[2]/time').text.strip('\n')
            )
            info_list.append(article_info_list)

    title_dataframe = pd.DataFrame(info_list)
    title_dataframe.to_csv('selenium_info_list.csv')


if __name__ == '__main__':
    date_time = SeleniumScrapper.get_time_period()
    # SeleniumScrapper.go_to_page_of_a_certain_time_period(date_time)
    scrap_content_in_said_time_period(date_time)
    # SeleniumScrapper.click_to_next_page()
