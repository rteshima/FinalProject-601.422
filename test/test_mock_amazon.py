import unittest
from unittest.mock import Mock, patch
from stores import amazon
from notifications import notifications
import time

    
class MockAmazonTestCase(unittest.TestCase):
    
    def setUp(self):
        notif_handler = notifications.NotificationHandler()
        self.am = amazon.Amazon(notif_handler)

    def tearDown(self):
        self.am = None


    def test_handle_home_page(self):
        self.am.get_page(url="https://"+self.am.amazon_website)
        with self.assertLogs(logger='fairgame', level='DEBUG') as self.cm:
            self.am.handle_home_page()

        
        self.assertIn(
            "WARNING:fairgame:On home page, trying to get back to checkout",
            self.cm.output
        )



if __name__ == '__main__':
    unittest.main()

