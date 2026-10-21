import unittest

from calculator import divide, multiply


class TestMultiply(unittest.TestCase):
    def test_positive(self):
        self.assertEqual(multiply(3, 4), 12)

    def test_negative(self):
        self.assertEqual(multiply(-3, 4), -12)
        self.assertEqual(multiply(-3, -4), 12)

    def test_by_zero(self):
        self.assertEqual(multiply(5, 0), 0)

    def test_floats(self):
        self.assertAlmostEqual(multiply(0.1, 3), 0.3)


class TestDivide(unittest.TestCase):
    def test_positive(self):
        self.assertEqual(divide(12, 4), 3)

    def test_negative(self):
        self.assertEqual(divide(-12, 4), -3)
        self.assertEqual(divide(-12, -4), 3)

    def test_fractional_result(self):
        self.assertEqual(divide(1, 4), 0.25)

    def test_zero_numerator(self):
        self.assertEqual(divide(0, 5), 0)

    def test_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            divide(5, 0)


if __name__ == "__main__":
    unittest.main()
