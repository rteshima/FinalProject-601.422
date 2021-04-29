from stores import amazon
from notifications import notifications
import unittest
import time
import os, os.path
from unittest.mock import Mock, patch

class AmazonTestCase(unittest.TestCase):
    # setUp function where we'll initialize objects

    def setUp(self):
        notif_handler = notifications.NotificationHandler()
        self.am = amazon.Amazon(notif_handler)

    def tearDown(self):
        self.am = None
    
    def test_get_page(self):
        print("[INITIALIZING TEST]: test_get_page")
        self.am.get_page(url="https://"+self.am.amazon_website)
        self.assertEquals(self.am.driver.current_url, "https://smile.amazon.com/")

    # again, use this format
    def test_amazon_NOT_logged_in(self):
        print("[INITIALIZING TEST]: test_amazon_NOT_logged_in")
        self.am.get_page(url="https://"+self.am.amazon_website)
        time.sleep(2)
        self.assertFalse(self.am.is_logged_in())

    def test_amazon_logged_in(self):
        print("[INITIALIZING TEST]: test_amazon_logged_in")
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

    def test_save_screenshot(self):
        print("[INITIALIZING TEST]: test_save_screenshot")
        self.am.get_page(url="https://"+self.am.amazon_website)
        self.am.save_screenshot("home_page")
        self.assertEquals(len(os.listdir('./screenshots/')), 1)

    def test_save_page_source(self):
        print("[INITIALIZING TEST]: test_save_page_source")
        self.am.get_page(url="https://"+self.am.amazon_website)
        self.am.save_page_source("home_page")
        self.assertEquals(len(os.listdir('./html_saves/')), 1)
        
    # RUNS IN AN INFINITE LOOP
    # def test_run_asins_empty_asins(self):
        # print("[INITIALIZING TEST]: test_run_asins_empty_asins")
    #     self.am.asin_list = None
    #     self.am.run_asins(delay=1)

    def test_items_already_in_cart(self):
        print("[INITIALIZING TEST]: test_items_already_in_cart")
        with self.assertLogs(logger='fairgame', level='INFO') as self.cm:
            #self.am.asin_list = [["B08FC5L3RG"]]
            self.am.run(delay=1)
            self.am.run(delay=1)

        
        self.assertIn(
            "INFO:fairgame:Delete all item(s) in cart before starting bot.",
            self.cm.output
        )

    def test_fail_to_checkout_note(self):
        print("[INITIALIZING TEST]: test_fail_to_checkout_note")
        with self.assertLogs(logger='fairgame', level='INFO') as self.cm:
            #self.am.asin_list = [["B08FC5L3RG"]]
            self.am.fail_to_checkout_note()

        
        self.assertIn(
            "INFO:fairgame:It's likely that the product went out of stock before FairGame could checkout.",
            self.cm.output
        )


    def test_check_stock_in_stock(self):
        print("[INITIALIZING TEST]: test_check_stock_in_stock")
        test_asin = "B07RKPP1YL" # ASIN number for dji mavic drone
        test_reserve_min = 400.00
        test_reserve_max = 600.00
        
        result = self.am.check_stock(test_asin, test_reserve_min, test_reserve_max)
        
        self.assertTrue(result)
    
    def test_check_stock_out_of_stock(self):
        print("[INITIALIZING TEST]: test_check_stock_out_of_stock")
        test_asin = "B08FC5L3RG" # ASIN number for PS5 (currently unavail as of 4/28)
        test_reserve_min = 400.00
        test_reserve_max = 600.00
        
        result = self.am.check_stock(test_asin, test_reserve_min, test_reserve_max)
        
        self.assertFalse(result)

    def test_check_stock_out_of_stock_specific_size(self):
        print("[INITIALIZING TEST]: test_check_stock_out_of_stock_specific_size")
        test_asin = "B06W55ND13" # ASIN number for Nike men's tennis shoes (currently unavail as of 4/28)
        test_reserve_min = 50.00
        test_reserve_max = 200.00
        
        result = self.am.check_stock(test_asin, test_reserve_min, test_reserve_max)
        
        self.assertFalse(result)

    def test_check_stock_too_many_atk(self):
        print("[INITIALIZING TEST]: test_check_stock_too_many_atk")
        test_asin = "B06W55ND13" # ASIN number for Nike men's tennis shoes (currently unavail as of 4/28)
        test_reserve_min = 50.00
        test_reserve_max = 200.00
        # Input parameter for atk will exceed the DEFAULT_MAX_ATC_TRIES
        result = self.am.check_stock(test_asin, test_reserve_min, test_reserve_max, 5)
        
        self.assertFalse(result)

    def test_run_asins_standard_case(self):
        print("[INITIALIZING TEST]: test_run_asins_standard_case")
        expected_asin = "B07K7NLDGT"
        result = self.am.run_asins(3)
        self.assertEquals(expected_asin, result)

if __name__ == '__main__':
    unittest.main()