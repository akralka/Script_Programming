import script
import unittest


class Test_TestBorrow(unittest.TestCase):
    def test_borrow_too_much(self):
        self.assertEqual(script.Library().borrow('brysiu', 1000, 'Nowak'), 'Too much')

    def test_borrow_wrong_item(self):
        self.assertEqual(script.Library().borrow('cos', 1, 'Nowak'), 'Wrong book')

    def test_borrow_wrong_name(self):
        self.assertEqual(script.Library().borrow('brysiu', 1, 'Nowak12['), 'Wrong name')

    def test_borrow_lack_of__name(self):
        self.assertEqual(script.Library().borrow('brysiu', 1, ''), 'No name')

    def test_borrow_wrong_quantity(self):
        self.assertEqual(script.Library().borrow('brysiu', '[aa]', 'Nowak'), 'Wrong quantity')

    def test_borrow_quantity_less_than_0(self):
        self.assertEqual(script.Library().borrow('brysiu', -3, 'Nowak'), 'Quantity equal or less than 0')


# class Test_TestRefund(unittest.TestCase):

#     def test_refund_wrong_item(self):
#         self.assertEqual(script.refund('Brysiu', 12, 'Nowak'), 'Nieprawidłowy produkt\n')

#     def test_refund_wrong_name(self):
#         self.assertEqual(script.refund('T-shirt', 12, 'Nowak((1'), 'Wrong name')

#     def test_refundlack_of__name(self):
#         self.assertEqual(script.refund('T-shirt', 1, ''), 'No name')

#     def test_refund_wrong_quantity(self):
#         self.assertEqual(script.refund('T-shirt', '[aa]', 'Nowak'), 'Wrong quantity')

#     def test_refund_quantity_less_than_0(self):
#         self.assertEqual(script.refund('T-shirt', -3, 'Nowak'), 'Quantity equal or less than 0')

if __name__ == '__main__':
    unittest.main()