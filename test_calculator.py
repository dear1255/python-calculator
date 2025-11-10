import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    # Add the following test methods to the TestCalculator class:
    def test_add2(self):
        self.assertEqual(self.calc.add(3, 2), 5)
    def test_subtract1(self):
        self.assertEqual(self.calc.subtract(5, 1), 4)
    def test_subtract2(self):
        self.assertEqual(self.calc.subtract(7, 2), 5)
    def test_multiply1(self):
        self.assertEqual(self.calc.multiply(5, 2), 10)
    def test_multiply2(self):
        self.assertEqual(self.calc.multiply(3, 2), 6)
    def test_divide1(self):
        self.assertEqual(self.calc.divide(20, 2), 10)
    def test_divide2(self):
        self.assertEqual(self.calc.divide(12, 2), 6)
    def test_modulo1(self):
        self.assertEqual(self.calc.modulo(9, 2), 1)
    def test_modulo2(self):
        self.assertEqual(self.calc.modulo(17, 3), 2)




       



    
if __name__ == '__main__':
    unittest.main()