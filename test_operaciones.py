import unittest
from operaciones import *

class TestOperaciones(unittest.TestCase):
    def test_suma(self):
        self.assertEqual(suma(1,2), 3)
        self.assertEqual(suma(2,2), 4)
        self.assertEqual(suma(3,6), 9)

    def test_resta(self):
        self.assertEqual(resta(1,2), -1)
        self.assertEqual(resta(6,6), 0)
        self.assertEqual(resta(10,2), 8)

    def test_multiplicacion(self):
        self.assertEqual(multiplicacion(1,2), 2)
        self.assertEqual(multiplicacion(2,2), 4)
        self.assertEqual(multiplicacion(3,6), 18)

    def test_division(self):
        self.assertEqual(division(1,2), 0.5)
        self.assertEqual(division(6,6), 1)
        self.assertEqual(division(10,2), 5)

if __name__ == '__main__':
    unittest.main()