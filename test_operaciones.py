import unittest
from operaciones import *

class TestOperaciones(unittest.TestCase):
    def test_suma(self):
        self.assertEqual(suma(1,2), 3)
        self.assertEqual(suma(2,2), 4)

    # def test_resta(self):
    #     self.assertEqual(resta(1,2), -1)
    #     self.assertEqual(resta(1,2), -2)

if __name__ == '__main__':
    unittest.main()