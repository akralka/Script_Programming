import unittest
from DeanerySystem import term, day

class TestTerm(unittest.TestCase):

    def test_laterThan(self):
        self.assertEqual(term.Term(day.Day.MON, 9, 10).laterThan(term.Term(day.Day.FRI, 10, 26)), False)
        self.assertEqual(term.Term(day.Day.MON, 9, 10).laterThan(term.Term(day.Day.FRI, 10, 6)), False)
        self.assertEqual(term.Term(day.Day.MON, 9, 10).laterThan(term.Term(day.Day.FRI, 14, 2)), False)
        self.assertEqual(term.Term(day.Day.MON, 9, 10).laterThan(term.Term(day.Day.FRI, 7, 13)), True)
    

    def test_earlierThan(self):
        self.assertEqual(term.Term(day.Day.MON, 9, 10).earlierThan(term.Term(day.Day.FRI, 10, 26)), True)
        self.assertEqual(term.Term(day.Day.MON, 9, 10).earlierThan(term.Term(day.Day.FRI, 10, 6)), True)
        self.assertEqual(term.Term(day.Day.MON, 9, 10).earlierThan(term.Term(day.Day.FRI, 14, 2)), True)
        self.assertEqual(term.Term(day.Day.MON, 9, 10).earlierThan(term.Term(day.Day.FRI, 7, 13)), False)
        


if __name__ == '__main__':
    unittest.main()