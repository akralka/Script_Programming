import unittest
from dekoratory_funkcji import Operacje

class Test_Operacje(unittest.TestCase):

    def test_suma_3arg(self):
        self.assertEqual(Operacje().suma(1,2,3), ('1+2+3=6'))

    def test_suma_2arg(self):
        self.assertEqual(Operacje().suma(1,2), ('1+2+4=7'))

    def test_suma_1arg(self):
        self.assertEqual(Operacje().suma(1), ('1+4+5=10'))
    
    def test_suma_0arg(self):
        try:
            Operacje().suma()
        except TypeError:
            val = True
        self.assertTrue(val)

    def test_suma(self):
        op = Operacje()
        op['suma']=[1,2]
        self.assertEqual(op.argumentySuma, [1,2])


    def test_roznica_2arg(self):
        self.assertEqual(Operacje().roznica(2,1), ('2-1=1'))

    def test_roznica_1arg(self):
        self.assertEqual(Operacje().roznica(2), ('2-4=-2'))

    def test_roznica_0arg(self):
        op = Operacje()
        self.assertEqual(op.roznica(), ('4-5=-1'))
    
    def test_roznica(self):
        op = Operacje()
        op['roznica']=[1,2,3]
        self.assertEqual(op.argumentyRoznica, [1,2,3])

if __name__ == '__main__':
    unittest.main()


