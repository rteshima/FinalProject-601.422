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

    # # again, use this format
    # def test_amazon_NOT_logged_in(self):
    #     print("[INITIALIZING TEST]: test_amazon_NOT_logged_in")
    #     self.am.get_page(url="https://"+self.am.amazon_website)
    #     time.sleep(2)
    #     self.assertFalse(self.am.is_logged_in())

    # def test_amazon_logged_in(self):
    #     print("[INITIALIZING TEST]: test_amazon_logged_in")
    #     with self.assertLogs(logger='fairgame', level='INFO') as self.cm:
    #         self.am.get_page(url="https://"+self.am.amazon_website)
    #         self.am.handle_startup()
    #         self.am.login()
    #         time.sleep(2)
    #         self.assertTrue(self.am.is_logged_in())
    #     self.assertIn(
    #         "INFO:fairgame:Already logged in",
    #         self.cm.output
    #     )

    # def test_save_screenshot(self):
    #     print("[INITIALIZING TEST]: test_save_screenshot")
    #     self.am.get_page(url="https://"+self.am.amazon_website)
    #     self.am.save_screenshot("home_page")
    #     self.assertEquals(len(os.listdir('./screenshots/')), 1)

    # def test_save_page_source(self):
    #     self.am.get_page(url="https://"+self.am.amazon_website)
    #     self.am.save_page_source("home_page")
    #     self.assertEquals(len(os.listdir('./html_saves/')), 1)
        
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
    
    def test_attempt_atc_valid_offeringID(self):
        print("[INITIALIZING TEST]: test_attempt_atc_valid_offeringID")

        # offeringID of a DJI gimbal
        test_offeringID = "RiIYaL1Mjc6UD55v0XDmYPqHO%2BzVhFJpPokoeoGeE1lO1FRbjUkHjEhT%2FevBwzpOANKChTvZnmKTsNsG5IMXE6sGF5r6fSvHnZXXbejw6udcdeeoV2GAJgufLzLEM%2F1Kb7zf%2FE62mb1EkhExQQ7bVw%3D%3D"
        test_offerListingID = "qZsmGu54hxpPyYOq%2Bf1%2FEvjC943vygHxah%2FF5kE%2B7RgtmMD7SI5oyeBvM75QqckQOnh8YaRLoykeEFMuzTWUx%2FjtpzjAqZTZmvoWXKMbB8fbDmUQ5TGGB0fjgyNXWivOvkdhGLqbRziIbFdYD1vfWA%3D%3D"

        result = self.am.attempt_atc(test_offeringID)
        self.assertTrue(result)

    # # THIS METHOD FAILS BECAUSE THERE IS NO CHECK FOR AN INVALID OFFERING ID
    # # Realistically, they should check for robustness
    # def test_attempt_atc_invalid_offeringID(self):
    #     print("[INITIALIZING TEST]: test_attempt_atc_invalid_offeringID")

    #     # random offeringID
    #     test_offeringID = "2BzVh33FJpPokoeoGeE1lO1FRbjUkHjEhT424%2F1Kb7zf%2FE62mb1EkhExQQ7bVw%3D%3D"
    #     test_offerListingID = "qZsmGu54hxpPyYOq%2Bf1%2FEvjC943vygHxah%2FF5kE%2B7RgtmMD7SI5oyeBvM75QqckQOnh8YaRLoykeEFMuzTWUx%2FjtpzjAqZTZmvoWXKMbB8fbDmUQ5TGGB0fjgyNXWivOvkdhGLqbRziIbFdYD1vfWA%3D%3D"

    #     result = self.am.attempt_atc(test_offeringID)
    #     self.assertFalse(result)

        
    def test_remove_asin_list_regular_asin(self):
        print("[INITIALIZING TEST]: test_remove_asin_list_regular_asin")
        asin_to_remove = "B07K7NLDGT"
        self.am.remove_asin_list(asin_to_remove)
        self.assertEquals(0, len(self.am.asin_list))
    
    def test_remove_asin_list_nonexistent_asin(self):
        print("[INITIALIZING TEST]: test_remove_asin_list_nonexistent_asin")
        asin_to_remove = "JDSO9D"
        self.am.remove_asin_list(asin_to_remove)

        #should equal 1 since nothing removed
        self.assertEquals(1, len(self.am.asin_list)) 
    

    def test_handle_unknown_title_random_title(self):
        with self.assertLogs(logger='fairgame', level='WARNING') as self.cm:
            print("[INITIALIZING TEST]: test_handle_unknown_title_random_title")
            test_title = "Johns Hopkins"
            self.am.handle_unknown_title(test_title)
        
        print(self.cm.output)
        self.assertIn(
            "WARNING:fairgame:20...", #asserting countdown is reported to log
            self.cm.output
        )

    
    
    def test_handle_doggos(self):
        print("[INITIALIZING TEST]: test_handle_doggos")
        self.am.handle_doggos()
        self.assertFalse(self.am.try_to_checkout)
    
    def test_handle_out_of_stock(self):
        print("[INITIALIZING TEST]: test_handle_out_of_stock")
        self.am.handle_out_of_stock()
        self.assertFalse(self.am.try_to_checkout)
    
    # WILL FAIL BECUASE CAPTCHA DOESNT SHOW UP
    def test_handle_captcha_pass(self):
        print("[INITIALIZING TEST]: test_handle_captcha_pass")
        result = self.am.handle_captcha()
        self.assertTrue(result)
    
    def test_handle_captcha_fail(self):
        print("[INITIALIZING TEST]: test_handle_captcha_fail")
        result = self.am.handle_captcha()
        self.assertFalse(result)

    def test_wait_for_page_content_change(self):
        print("[INITIALIZING TEST]: test_wait_for_page_content_change")
        
        self.am.wait_for_page_content_change()

    def test_send_notification_screenshot(self):
        print("[INITIALIZING TEST]: test_send_notification_screenshot")
        self.am.send_notification("Hello, test notif", "testingPage")

    def test_send_notification_no_screenshot(self):
        print("[INITIALIZING TEST]: test_send_notification_no_screenshot")
        self.am.send_notification("Hello, test notif", "testingPage", False)

    def test_get_timeout(self):
        print("[INITIALIZING TEST]: test_get_timeout")
        expected_after = time.time() + 10

        result = self.am.get_timeout()
        self.assertGreater(result, expected_after)
    
    def test_get_timestamp_filename_dot(self):
        print("[INITIALIZING TEST]: test_get_timestamp_filename_dot")
        test_filename = "johns_tests"
        test_extension = ".txt"

        result = amazon.get_timestamp_filename(test_filename, test_extension)
        self.assertIn(test_filename, result)
        self.assertIn(test_extension, result)

    def test_get_timestamp_filename_no_dot(self):
        print("[INITIALIZING TEST]: test_get_timestamp_filename_no_dot")
        test_filename = "johns_tests"
        test_extension = "txt"

        result = amazon.get_timestamp_filename(test_filename, test_extension)
        self.assertIn(test_filename, result)
        self.assertIn(test_extension, result)

    def test_navigate_pages(self):
        print("testing navigate pages with test = true")
        self.am.get_page(url="https://"+self.am.amazon_website)
        with self.assertLogs(logger='fairgame', level='DEBUG') as self.cm:
            self.am.navigate_pages(True)
        
        self.assertIn(
            "DEBUG:fairgame:'navigate_pages' returned None",
            self.cm.output
        )

if __name__ == '__main__':
    unittest.main()