import skrypt_2
import unittest
from fractions import Fraction




class Test_TestStringCheck(unittest.TestCase):
    def test_string_int(self):
        self.assertEqual(skrypt_2.digit('3ff4'), ('34', 'ff')) 

    def test_string(self): 
        self.assertEqual(skrypt_2.digit('ada'), ('', 'ada')) 

    def test_int(self): 
        self.assertEqual(skrypt_2.digit('7675'), ('7675', '')) 

    def test_list(self): 
        self.assertEqual(skrypt_2.digit('[1,2,3]'), ('123', '[,,]'))                             



if __name__ == '__main__':
    unittest.main()