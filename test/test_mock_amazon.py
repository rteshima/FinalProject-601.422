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


    def test_cart_count(self):
        self.am.get_page(url="https://"+self.am.amazon_website)
        initial_cart = self.am.get_cart_count()
        print(initial_cart)
        print("[INITIALIZING TEST]: test_cart_count")
        test_offeringID = "RiIYaL1Mjc6UD55v0XDmYPqHO%2BzVhFJpPokoeoGeE1lO1FRbjUkHjEhT%2FevBwzpOANKChTvZnmKTsNsG5IMXE6sGF5r6fSvHnZXXbejw6udcdeeoV2GAJgufLzLEM%2F1Kb7zf%2FE62mb1EkhExQQ7bVw%3D%3D"
        self.am.attempt_atc(test_offeringID)
        self.assertEqual(initial_cart+1, self.am.get_cart_count())



if __name__ == '__main__':
    unittest.main()

