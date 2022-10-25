import skrypt_zajecia
import unittest


class Test_TestSale(unittest.TestCase):
    def test_sale_too_much(self):
        self.assertEqual(skrypt_zajecia.sale('T-shirt', 37, 'Nowak'), 'Za duża ilość\n')

    def test_sale_wrong_item(self):
        self.assertEqual(skrypt_zajecia.sale('Brysiu', 1, 'Nowak'), 'Nieprawidłowy produkt\n')

    def test_sale_wrong_name(self):
        self.assertEqual(skrypt_zajecia.sale('T-shirt', 1, 'Nowak12['), 'Niepoprawne nazwisko\n')

    def test_sale_lack_of__name(self):
        self.assertEqual(skrypt_zajecia.sale('T-shirt', 1, ''), 'Brak nazwiska\n')

    def test_sale_wrong_quantity(self):
        self.assertEqual(skrypt_zajecia.sale('T-shirt', '[aa]', 'Nowak'), 'Nieprawidłowa ilość\n')

    def test_sale_quantity_less_than_0(self):
        self.assertEqual(skrypt_zajecia.sale('T-shirt', -3, 'Nowak'), 'Ilość mniejsza lub równa 0\n')


class Test_TestRefund(unittest.TestCase):

    def test_refund_wrong_item(self):
        self.assertEqual(skrypt_zajecia.refund('Brysiu', 12, 'Nowak'), 'Nieprawidłowy produkt\n')

    def test_refund_wrong_name(self):
        self.assertEqual(skrypt_zajecia.refund('T-shirt', 12, 'Nowak((1'), 'Niepoprawne nazwisko\n')

    def test_refundlack_of__name(self):
        self.assertEqual(skrypt_zajecia.refund('T-shirt', 1, ''), 'Brak nazwiska\n')

    def test_refund_wrong_quantity(self):
        self.assertEqual(skrypt_zajecia.refund('T-shirt', '[aa]', 'Nowak'), 'Nieprawidłowa ilość\n')

    def test_refund_quantity_less_than_0(self):
        self.assertEqual(skrypt_zajecia.refund('T-shirt', -3, 'Nowak'), 'Ilość mniejsza lub równa 0\n')

if __name__ == '__main__':
    unittest.main()