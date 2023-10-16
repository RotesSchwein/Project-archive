from scrapper import BasicScrapper
from selenium_scrapper import SeleniumScrapper


if __name__ == '__main__':
    date_time = SeleniumScrapper.get_time_period()
    SeleniumScrapper.go_to_page_of_a_certain_period(date_time)
    # SeleniumScrapper.click_to_next_page()