from stores import amazon
from notifications import notifications
import unittest
import time

class AmazonTestCase(unittest.TestCase):
    # setUp function where we'll initialize objects

    def setUp(self):
        notif_handler = notifications.NotificationHandler()
        self.am = amazon.Amazon(notif_handler)

    def tearDown(self):
        self.am = None
    
    def test_get_page(self):
        self.am.get_page(url="https://"+self.am.amazon_website)
        self.assertEquals(self.am.driver.current_url, "https://smile.amazon.com/")

    # again, use this format
    def test_amazon_NOT_logged_in(self):
        self.am.get_page(url="https://"+self.am.amazon_website)
        time.sleep(2)
        self.assertFalse(self.am.is_logged_in())

    def test_amazon_logged_in(self):
        with self.assertLogs(logger='fairgame', level='INFO') as self.cm:
            self.am.get_page(url="https://"+self.am.amazon_website)
            self.am.handle_startup()
            self.am.login()
            time.sleep(2)
            self.assertTrue(self.am.is_logged_in())
        self.assertIn(
            "INFO:fairgame:Already logged in",
            self.cm.output
        )

    # RUNS IN AN INFINITE LOOP
    # def test_empty_asins(self):
    #     self.am.asin_list = None
    #     self.am.run_asins(delay=1)

    
if __name__ == '__main__':
    unittest.main()