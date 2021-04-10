import unittest

from aliexpress_platform_integration_lib import formatlib
from aliexpress_platform_integration_lib import itemlib
from test.configs import STANDARD_TEST_URL


class TestItemLib(unittest.TestCase):
    def test_process_url(self):
        url = STANDARD_TEST_URL
        item_id, standard_item_detail_url = formatlib.process_url(url)
        item = itemlib.get_item(item_id)
        self.assertIsNotNone(item['title'])
        self.assertGreater(item['rating_average'], 0)
        self.assertGreater(item['price_usd_min'], 0)
        self.assertGreater(item['price_usd_max'], 0)
        self.assertIsNotNone(item['description_html'])
        self.assertGreater(len(item['images']), 0)


if __name__ == '__main__':
    unittest.main()
