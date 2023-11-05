import threading

# from scraper import BasicScrapper
from scraper import get_page_info

import mysql.connector
import pymysql

if __name__ == '__main__':
    # date_time = BasicScrapper.get_time_period()
    bs_info = get_page_info("2023-10-25")
