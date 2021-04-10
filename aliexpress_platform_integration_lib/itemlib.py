import requests

from aliexpress_platform_integration_lib.driverlib import get_driver
from aliexpress_platform_integration_lib.formatlib import get_standard_item_detail_url


def get_title(driver):
    data = driver.execute_script('return window.runParams')
    return data['data']['titleModule']['subject']


def get_rating_average(driver):
    data = driver.execute_script('return window.runParams')
    return float(data['data']['titleModule']['feedbackRating']['averageStarRage'])


def get_order_count(driver):
    data = driver.execute_script('return window.runParams')
    return int(data['data']['titleModule']['tradeCount'])


def get_price(driver):
    data = driver.execute_script('return window.runParams')
    return float(data['data']['priceModule']['minAmount']['value']), float(
        data['data']['priceModule']['maxAmount']['value'])


def get_description_html(driver):
    data = driver.execute_script('return window.runParams')
    r = requests.get(data['data']['descriptionModule']['descriptionUrl'])
    return r.content


def get_images(driver):
    data = driver.execute_script('return window.runParams')
    return data['data']['imageModule']['imagePathList']


def get_item(item_id):
    item = {
        'title': None,
        'rating_average': -1,
        'price_usd_min': -1,
        'price_usd_max': -1,
        'description': None,
        'images': [],
    }

    url = get_standard_item_detail_url(item_id)
    driver = get_driver(headless=True)
    driver.get(url)

    item['title'] = get_title(driver)
    item['rating_average'] = get_rating_average(driver)
    item['order_count'] = get_order_count(driver)
    item['price_usd_min'], item['price_usd_max'] = get_price(driver)
    item['description_html'] = get_description_html(driver)
    item['images'] = get_images(driver)

    return item
