import unittest
from test.configs import STANDARD_TEST_URL
from lib import formatlib


class TestFormatLib(unittest.TestCase):
    def test_process_url(self):
        url = STANDARD_TEST_URL
        item_id, standard_item_detail_url = formatlib.process_url(url)
        self.assertEqual(item_id, '4001215143666')
        self.assertEqual(standard_item_detail_url, 'https://www.aliexpress.com/item/4001215143666.html')


if __name__ == '__main__':
    unittest.main()
