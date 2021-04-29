from stores import amazon
from notifications import notifications
import unittest
import time
import os, os.path
from unittest.mock import Mock, patch

class DemoTestCase(unittest.TestCase):
    # setUp function where we'll initialize objects

    def setUp(self):
        notif_handler = notifications.NotificationHandler()
        self.am = amazon.Amazon(notif_handler)

    def tearDown(self):
        self.am = None

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

        
    def test_remove_asin_list_regular_asin(self):
        print("[INITIALIZING TEST]: test_remove_asin_list_regular_asin")
        asin_to_remove = "B07K7NLDGT"
        self.am.remove_asin_list(asin_to_remove)
        self.assertEquals(0, len(self.am.asin_list))



if __name__ == '__main__':
    unittest.main()