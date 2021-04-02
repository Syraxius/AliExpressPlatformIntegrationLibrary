import re


def get_item_id_from_url(url):
    url_without_parameters = url.split('?')[0]
    m = re.search(r'(\d+)', url_without_parameters)
    return m.group(0)


def get_standard_item_detail_url(item_id):
    return 'https://www.aliexpress.com/item/%s.html' % item_id


def process_url(url):
    item_id = get_item_id_from_url(url)
    standard_item_detail_url = get_standard_item_detail_url(item_id)
    return item_id, standard_item_detail_url
