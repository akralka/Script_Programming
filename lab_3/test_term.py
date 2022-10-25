import unittest
from DeanerySystem import term, day

class TestTerm(unittest.TestCase):

    def test_laterThan(self):
        self.assertEqual(term.Term(day.Day.MON, 9, 10).laterThan(term.Term(day.Day.FRI, 10, 26)), False)
        # self.assertEqual(term.laterThan(1, 2))
        # self.assertEqual(term.laterThan(2, 1))
        # self.assertEqual(term.laterThan(2, 2))


if __name__ == '__main__':
    unittest.main()