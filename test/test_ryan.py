from stores import amazon
from notifications import notifications
import unittest

class AmazonRyanTestCase(unittest.TestCase):
    # setUp function where we'll initialize objects

    def setUp(self):
        notif_handler = notifications.NotificationHandler()
        self.am = amazon.Amazon(notif_handler)

    def tearDown(self):
        self.am = None

    # def test_check_stock_in_stock(self):
    #     test_asin = "B07RKPP1YL" # ASIN number for dji mavic drone
    #     test_reserve_min = 400.00
    #     test_reserve_max = 600.00
        
    #     result = self.am.check_stock(test_asin, test_reserve_min, test_reserve_max)
        
    #     self.assertTrue(result)
    
    # def test_check_stock_out_of_stock(self):
    #     test_asin = "B08FC5L3RG" # ASIN number for PS5 (currently unavail as of 4/28)
    #     test_reserve_min = 400.00
    #     test_reserve_max = 600.00
        
    #     result = self.am.check_stock(test_asin, test_reserve_min, test_reserve_max)
        
    #     self.assertFalse(result)

    # def test_check_stock_out_of_stock_specific_size(self):
    #     test_asin = "B06W55ND13" # ASIN number for Nike men's tennis shoes (currently unavail as of 4/28)
    #     test_reserve_min = 50.00
    #     test_reserve_max = 200.00
        
    #     result = self.am.check_stock(test_asin, test_reserve_min, test_reserve_max)
        
    #     self.assertFalse(result)

    # def test_check_stock_too_many_atk(self):
    #     test_asin = "B06W55ND13" # ASIN number for Nike men's tennis shoes (currently unavail as of 4/28)
    #     test_reserve_min = 50.00
    #     test_reserve_max = 200.00
    #     # Input parameter for atk will exceed the DEFAULT_MAX_ATC_TRIES
    #     result = self.am.check_stock(test_asin, test_reserve_min, test_reserve_max, 5)
        
    #     self.assertFalse(result)

    # def test_run_asins_standard_case(self):
    #     expected_asin = "B07K7NLDGT"
    #     result = self.am.run_asins(3)
    #     self.assertEquals(expected_asin, result)




if __name__ == '__main__':
    unittest.main()