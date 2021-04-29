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

    def test_items_already_in_cart(self):
        with self.assertLogs(logger='fairgame', level='INFO') as self.cm:
            #self.am.asin_list = [["B08FC5L3RG"]]
            self.am.run(delay=1)
            self.am.run(delay=1)

        
        self.assertIn(
            "INFO:fairgame:Delete all item(s) in cart before starting bot.",
            self.cm.output
        )

    def test_fail_to_checkout_note(self):
        with self.assertLogs(logger='fairgame', level='INFO') as self.cm:
            #self.am.asin_list = [["B08FC5L3RG"]]
            self.am.fail_to_checkout_note()

        
        self.assertIn(
            "INFO:fairgame:It's likely that the product went out of stock before FairGame could checkout.",
            self.cm.output
        )
      
       

if __name__ == '__main__':
    unittest.main()

