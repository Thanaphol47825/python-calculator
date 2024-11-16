import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(1, 2), 1)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(9,15), 135)
    
    def test_divide(self):
        self.assertEqual(self.calc.divide(5, 25), 5)

    def test_modulo(self):
        self.assertEqual(self.calc.modulo(6, 10), 4)

    def test_ADD(self):
        self.assertEqual(self.calc.add(2, 3), 5)

    def test_SUBTRACT(self):
        self.assertEqual(self.calc.subtract(3, 5), 2)

    def test_MULTIPLY(self):
        self.assertEqual(self.calc.multiply(7, 6), 42)

    def test_DIVIDE(self):
        self.assertEqual(self.calc.divide(2, 10), 5)

    def test_MODULO(self):
        self.assertEqual(self.calc.modulo(4, 9), 1)
if __name__ == '__main__':
    unittest.main()