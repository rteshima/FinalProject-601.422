from stores import amazon
import unittest

class AmazonTestCase(unittest.TestCase):
    # setUp function where we'll initialize objects
    def setUp(self):
        pass

    # again, use this format
    def test_amazon_function_number_1(self):
        self.assertEqual(2, 2)

if __name__ == '__main__':
    unittest.main()