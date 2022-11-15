import biblioteka
import unittest
from biblioteka import Library, Book, Reader


class Test_TestBorrow(unittest.TestCase):

    def test_add(self):
        self.assertEqual(biblioteka.Reader("Adam", "Nowak", 123).__add__( Book(1, "Goethe", "Faust")), None)

    def test_add__(self):
        self.assertEqual(biblioteka.Reader("Adam", "Nowak", 111).__add__( Book(1, "Goethe", "Fa")), "can't borrow :there is no a book of that title or author")

    def test_sub(self):
        self.assertEqual(biblioteka.Reader("Adam", "Nowak", 1).__sub__( Book(1, "ethe", "Faust")),  "can't return :there is no a book of that title or author")

    def test_sub__(self):
        self.assertEqual(biblioteka.Reader("Adam", "Nowak", 1).__sub__( Book(1, "Nie", "Działa")),  "can't return :there is no a book of that title or author")

    def test_sub_not(self):
        self.assertEqual(biblioteka.Reader("Adam", "Nowak", 1).__sub__( Book(1, "Goethe", "Faust")),  None)

    def test_name_add(self):
        self.assertEqual(biblioteka.Reader("1mniam", "Nowak", 1).__add__( Book(1, "Goethe", "Faust")),  "Wrong name")
    
    def test_surname_add(self):
        self.assertEqual(biblioteka.Reader("mniam", "{5i", 1).__add__( Book(1, "Goethe", "Faust")),  "Wrong surname")

    def test_name_sub(self):
        self.assertEqual(biblioteka.Reader("1mniam", "Nowak", 1).__sub__( Book(1, "Goethe", "Faust")),  "Wrong name")

    def test_name_sub(self):
        self.assertEqual(biblioteka.Reader("mniam", "Nowa123", 1).__sub__( Book(1, "Goethe", "Faust")),  "Wrong surname")

if __name__ == '__main__':
    unittest.main()