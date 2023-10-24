from scrapper import BasicScrapper
from selenium_scrapper import SeleniumScrapper


if __name__ == '__main__':
    date_time = BasicScrapper().get_time_period()
    BasicScrapper.get_page_info(date_time)
    # BasicScrapper.go_through_pages(date_time)