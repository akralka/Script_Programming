import biblioteka
import unittest


class Test_TestBorrow(unittest.TestCase):
    def test_borrow_too_much(self):
        self.assertEqual(biblioteka.Library("book.txt").borrow('Faust', 1000, 'Nowak'), 'Too much')

    def test_borrow_wrong_item(self):
        self.assertEqual(biblioteka.Library("book.txt").borrow('cos', 1, 'Nowak'), 'Wrong book')

    def test_borrow_wrong_name(self):
        self.assertEqual(biblioteka.Library("book.txt").borrow('Faust', 1, 'Nowak12['), 'Wrong name')

    def test_borrow_lack_of__name(self):
        self.assertEqual(biblioteka.Library("book.txt").borrow('Faust', 1, ''), 'No name')

    def test_borrow_wrong_quantity(self):
        self.assertEqual(biblioteka.Library("book.txt").borrow('Faust', '[aa]', 'Nowak'), 'Wrong quantity')

    def test_borrow_quantity_less_than_0(self):
        self.assertEqual(biblioteka.Library("book.txt").borrow('Faust', -3, 'Nowak'), 'Quantity equal or less than 0')


class Test_TestReturn(unittest.TestCase):

    def test_book_return_wrong_item(self):
        self.assertEqual(biblioteka.Library("book.txt").book_return('cos', 1, 'Nowak'), 'Wrong book')

    def test_book_return_wrong_name(self):
        self.assertEqual(biblioteka.Library("book.txt").book_return('Faust', 1, 'Nowak12['), 'Wrong name')

    def test_book_returnlack_of__name(self):
        self.assertEqual(biblioteka.Library("book.txt").book_return('Faust', 1, ''), 'No name')

    def test_book_return_wrong_quantity(self):
        self.assertEqual(biblioteka.Library("book.txt").book_return('Faust', '[aa]', 'Nowak'), 'Wrong quantity')

    def test_book_return_quantity_less_than_0(self):
        self.assertEqual(biblioteka.Library("book.txt").book_return('Faust', -3, 'Nowak'), 'Quantity equal or less than 0')



if __name__ == '__main__':
    unittest.main()