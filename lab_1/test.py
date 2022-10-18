import main
import unittest
from fractions import Fraction


class Test_TestSum(unittest.TestCase):
    def test_sum_integer_integer(self):
        self.assertEqual(main.sum(2, 2), 4)

    def test_sum_integer_float(self):
        self.assertEqual(main.sum(2, 1.5), 3.5)

    def test_sum_integer_string(self):
       self.assertEqual(main.sum(2, '2'), 4)

    def test_sum_string_string(self):
        self.assertEqual(main.sum('2.1', '2.0'), 4.1)

    def test_sum_complex_complex(self):
        self.assertEqual(main.sum(2 + 3j, 2 + 5j), 4 + 8j)

    def test_sum_fraction_fraction(self):
        self.assertEqual(main.sum(Fraction(10, 18), Fraction(2, 18)), Fraction(12, 18))

    def test_sum_integer_wrong_number_in_string(self):
        self.assertEqual(main.sum(2, 'Ala ma kota123'), 2)

#  tu wyrzuca błąd a nie powinno >> ala.. >> na 0 powinno

    def test_sum_not_int_not_string(self):
        # self.assertEqual(main.sum(2, [1,2]), 2)
        with self.assertRaises(TypeError):
            main.sum(1, [2,3])


if __name__ == '__main__':
    unittest.main()

# main.sum >> bo importuje funkcje sumy z poprzedniego pliku