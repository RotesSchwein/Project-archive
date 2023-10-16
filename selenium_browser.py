from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def option():
    option = Options()
    option.add_experimental_option('detach', True)


def browser_driver():
    driver = webdriver.Chrome(options = option())
    driver.implicitly_wait(10)

    action = webdriver.ActionChains(driver = driver)
