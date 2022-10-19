import skrypt_zajęcia
import unittest


class Test_TestSale(unittest.TestCase):
    def test_sale_too_much(self):
        self.assertEqual(skrypt_zajęcia.sale('T-shirt', 37, 'Nowak'), 'Za duża ilość')

    def test_sale_wrong_item(self):
        self.assertEqual(skrypt_zajęcia.sale('Brysiu', 1, 'Nowak'), 'Nieprawidłowy produkt')

    def test_sale_wrong_name(self):
        self.assertEqual(skrypt_zajęcia.sale('T-shirt', 1, 'Nowak12['), 'Niepoprawne nazwisko')

    def test_sale_lack_of__name(self):
        self.assertEqual(skrypt_zajęcia.sale('T-shirt', 1, ''), 'Brak nazwiska')

    def test_sale_wrong_quantity(self):
        self.assertEqual(skrypt_zajęcia.sale('T-shirt', '[aa]', 'Nowak'), 'Nieprawidłowa ilość')

    def test_sale_quantity_less_than_0(self):
        self.assertEqual(skrypt_zajęcia.sale('T-shirt', -3, 'Nowak'), 'Ilość mniejsza lub równa 0')


class Test_TestRefund(unittest.TestCase):

    def test_refund_wrong_item(self):
        self.assertEqual(skrypt_zajęcia.refund('Brysiu', 12, 'Nowak'), 'Nieprawidłowy produkt')

    def test_refund_wrong_name(self):
        self.assertEqual(skrypt_zajęcia.refund('T-shirt', 12, 'Nowak((1'), 'Niepoprawne nazwisko')

    def test_refundlack_of__name(self):
        self.assertEqual(skrypt_zajęcia.refund('T-shirt', 1, ''), 'Brak nazwiska')

    def test_refund_wrong_quantity(self):
        self.assertEqual(skrypt_zajęcia.refund('T-shirt', '[aa]', 'Nowak'), 'Nieprawidłowa ilość')

    def test_refund_quantity_less_than_0(self):
        self.assertEqual(skrypt_zajęcia.refund('T-shirt', -3, 'Nowak'), 'Ilość mniejsza lub równa 0')

if __name__ == '__main__':
    unittest.main()