import unittest
from fractions import Fraction
from my_sum import sum


class TestSum(unittest.TestCase):
    def test_list_init(self):
        """
        Test that it can sum a list of integers
        """
        data = [1, 2, 3]
        result = sum(data)
        self.assertEqual(result, 6)

    def test_list_fractions(self):
        """
        Test that it can sum a list of fractions
        """
        data = [Fraction(1, 4), Fraction(1, 4), Fraction(2, 5)]
        result = sum(data)
        self.assertEqual(result, Fraction(8, 10))


if __name__ == "__main__":
    unittest.main()
