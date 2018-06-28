'''
Test unnecessary_math with unittest
To run tests:
    python test_unnecessary_math_unittest.py
'''

import unittest
from unnecessary_math import multiply

class TestUM(unittest.TestCase):

    def setUp(self):
        pass

    def test_numbers_3_5(self):
        self.assertEqual( multiply(3,5), 15)

    def test_strings_a_4(self):
        self.assertEqual( multiply('a',4), 'aaaa')

if __name__ == '__main__':
    unittest.main()

