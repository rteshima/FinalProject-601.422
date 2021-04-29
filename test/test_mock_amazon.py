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


    def test_navigate_pages_signin(self):
        print("[INITIALIZING TEST]: test_navigate_pages_signin")
        with self.assertLogs(logger='fairgame', level='DEBUG') as self.cm:
            self.am.amazon_config = {"SIGN_IN_TITLES": ["Amazon.com: Online Shopping for Electronics, Apparel, Computers, Books, DVDs & more"]}
            self.am.get_page(url="https://"+self.am.amazon_website)
            self.am.navigate_pages(True)
        self.assertIn(
            "DEBUG:fairgame:'navigate_pages' returned None",
            self.cm.output
        )

    def test_navigate_pages_shoppingcart(self):
        print("[INITIALIZING TEST]: test_navigate_pages_shoppingcart")
        with self.assertLogs(logger='fairgame', level='DEBUG') as self.cm:
            self.am.amazon_config = {"SHOPPING_CART_TITLES": ["Amazon.com: Online Shopping for Electronics, Apparel, Computers, Books, DVDs & more"]}
            self.am.get_page(url="https://"+self.am.amazon_website)
            self.am.navigate_pages(True)
        self.assertIn(
            "DEBUG:fairgame:'navigate_pages' returned None",
            self.cm.output
        )

    def test_navigate_pages_checkout(self):
        print("[INITIALIZING TEST]: test_navigate_pages_checkout")
        with self.assertLogs(logger='fairgame', level='DEBUG') as self.cm:
            self.am.amazon_config = {"CHECKOUT_TITLES": ["Amazon.com: Online Shopping for Electronics, Apparel, Computers, Books, DVDs & more"]}
            self.am.get_page(url="https://"+self.am.amazon_website)
            self.am.navigate_pages(True)
        self.assertIn(
            "DEBUG:fairgame:'navigate_pages' returned None",
            self.cm.output
        )

    def test_navigate_pages_ordercomplete(self):
        print("[INITIALIZING TEST]: test_navigate_pages_ordercomplete")
        with self.assertLogs(logger='fairgame', level='DEBUG') as self.cm:
            self.am.amazon_config = {"ORDER_COMPLETE_TITLES": ["Amazon.com: Online Shopping for Electronics, Apparel, Computers, Books, DVDs & more"]}
            self.am.get_page(url="https://"+self.am.amazon_website)
            self.am.navigate_pages(True)
        self.assertIn(
            "DEBUG:fairgame:'navigate_pages' returned None",
            self.cm.output
        )

    def test_navigate_pages_prime_titles(self):
        print("[INITIALIZING TEST]: test_navigate_pages_prime_titles")
        with self.assertLogs(logger='fairgame', level='DEBUG') as self.cm:
            self.am.amazon_config = {"PRIME_TITLES": ["Amazon.com: Online Shopping for Electronics, Apparel, Computers, Books, DVDs & more"]}
            self.am.get_page(url="https://"+self.am.amazon_website)
            self.am.navigate_pages(True)
        self.assertIn(
            "DEBUG:fairgame:'navigate_pages' returned None",
            self.cm.output
        )

    def test_navigate_pages_homepage(self):
        print("[INITIALIZING TEST]: test_navigate_pages_homepage")
        with self.assertLogs(logger='fairgame', level='DEBUG') as self.cm:
            self.am.amazon_config = {"HOME_PAGE_TITLES": ["Amazon.com: Online Shopping for Electronics, Apparel, Computers, Books, DVDs & more"]}
            self.am.get_page(url="https://"+self.am.amazon_website)
            self.am.navigate_pages(True)
        self.assertIn(
            "DEBUG:fairgame:'navigate_pages' returned None",
            self.cm.output
        )

    def test_navigate_pages_doggo(self):
        print("[INITIALIZING TEST]: test_navigate_pages_doggo")
        with self.assertLogs(logger='fairgame', level='DEBUG') as self.cm:
            self.am.amazon_config = {"DOGGO_TITLES": ["Amazon.com: Online Shopping for Electronics, Apparel, Computers, Books, DVDs & more"]}
            self.am.get_page(url="https://"+self.am.amazon_website)
            self.am.navigate_pages(True)
        self.assertIn(
            "DEBUG:fairgame:'navigate_pages' returned None",
            self.cm.output
        )

    def test_navigate_pages_outofstock(self):
        print("[INITIALIZING TEST]: test_navigate_pages_outofstock")
        with self.assertLogs(logger='fairgame', level='DEBUG') as self.cm:
            self.am.amazon_config = {"OUT_OF_STOCK": ["Amazon.com: Online Shopping for Electronics, Apparel, Computers, Books, DVDs & more"]}
            self.am.get_page(url="https://"+self.am.amazon_website)
            self.am.navigate_pages(True)
        self.assertIn(
            "DEBUG:fairgame:'navigate_pages' returned None",
            self.cm.output
        )

    def test_navigate_pages_business_po(self):
        print("[INITIALIZING TEST]: test_navigate_pages_business_po")
        with self.assertLogs(logger='fairgame', level='DEBUG') as self.cm:
            self.am.amazon_config = {"BUSINESS_PO_TITLES": ["Amazon.com: Online Shopping for Electronics, Apparel, Computers, Books, DVDs & more"]}
            self.am.get_page(url="https://"+self.am.amazon_website)
            self.am.navigate_pages(True)
        self.assertIn(
            "DEBUG:fairgame:'navigate_pages' returned None",
            self.cm.output
        )

    def test_navigate_pages_address_select(self):
        print("[INITIALIZING TEST]: test_navigate_pages_address_select")
        with self.assertLogs(logger='fairgame', level='DEBUG') as self.cm:
            self.am.amazon_config = {"ADDRESS_SELECT": ["Amazon.com: Online Shopping for Electronics, Apparel, Computers, Books, DVDs & more"]}
            self.am.get_page(url="https://"+self.am.amazon_website)
            self.am.navigate_pages(True)
        self.assertIn(
            "DEBUG:fairgame:'navigate_pages' returned None",
            self.cm.output
        )



if __name__ == '__main__':
    unittest.main()

