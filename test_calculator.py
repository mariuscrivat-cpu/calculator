import unittest

from calculator import adunare, divide, multiply, scadere


class TestAdunare(unittest.TestCase):
    def test_positive(self):
        self.assertEqual(adunare(3, 4), 7)

    def test_negative(self):
        self.assertEqual(adunare(-3, 4), 1)
        self.assertEqual(adunare(-3, -4), -7)

    def test_floats(self):
        self.assertAlmostEqual(adunare(0.1, 0.2), 0.3)


class TestScadere(unittest.TestCase):
    def test_positive(self):
        self.assertEqual(scadere(10, 4), 6)

    def test_negative_result(self):
        self.assertEqual(scadere(4, 10), -6)

    def test_negative_operands(self):
        self.assertEqual(scadere(-3, -4), 1)

    def test_floats(self):
        self.assertAlmostEqual(scadere(0.3, 0.1), 0.2)


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
