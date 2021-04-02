import os

from selenium import webdriver

from definitions import ROOT_DIR


def get_driver(headless=True):
    options = webdriver.ChromeOptions()
    if headless:
        options.add_argument('--headless')
    driver = webdriver.Chrome(os.path.join(ROOT_DIR, 'bin', 'chromedriver'),
                              options=options,
                              service_args=['--verbose', '--log-path=/tmp/chromedriver.log'])
    return driver
