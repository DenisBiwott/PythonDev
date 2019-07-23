# Biwott
import unittest
import calc


class TestCalcs(unittest.TestCase):

    def test_add(self):
        result = calc.addition(2, 4)
        self.assertEqual(result, 6)

    def test_multiply(self):
        self.assertEqual(calc.multiply(2, 4), 8)

    def test_subtract(self):
        self.assertEqual(calc.subtract(2, 4), -2)

    def test_divide(self):
        self.assertEqual(calc.divide(4, 2), 2)
        with self.assertRaises(ValueError):
            calc.divide(10, 0)


if __name__ == '__main__':
    unittest.main()
