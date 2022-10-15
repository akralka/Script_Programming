import skrypt_2
import unittest
from fractions import Fraction




class Test_TestSum(unittest.TestCase):
    def test_sum_integer_integer(self):
        self.assertEqual(skrypt_2.digit('3ff4'), 'ff 34')   
                                                




if __name__ == '__main__':
    unittest.main()