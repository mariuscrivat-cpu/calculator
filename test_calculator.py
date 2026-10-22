import unittest

from calculator import adunare, scadere


class TestAdunare(unittest.TestCase):
    def test_pozitive(self):
        self.assertEqual(adunare(2, 3), 5)

    def test_negative(self):
        self.assertEqual(adunare(-2, -3), -5)

    def test_semne_diferite(self):
        self.assertEqual(adunare(-2, 3), 1)
        self.assertEqual(adunare(5, -3), 2)

    def test_zero(self):
        self.assertEqual(adunare(0, 0), 0)
        self.assertEqual(adunare(0, 7), 7)
        self.assertEqual(adunare(7, 0), 7)

    def test_float(self):
        self.assertEqual(adunare(1.5, 2.25), 3.75)
        self.assertAlmostEqual(adunare(0.1, 0.2), 0.3)
        self.assertEqual(adunare(-1.5, 1.5), 0.0)
        self.assertEqual(adunare(1, 0.5), 1.5)


class TestScadere(unittest.TestCase):
    def test_pozitive(self):
        self.assertEqual(scadere(5, 3), 2)
        self.assertEqual(scadere(3, 5), -2)

    def test_negative(self):
        self.assertEqual(scadere(-2, -3), 1)

    def test_semne_diferite(self):
        self.assertEqual(scadere(-2, 3), -5)
        self.assertEqual(scadere(5, -3), 8)

    def test_zero(self):
        self.assertEqual(scadere(0, 0), 0)
        self.assertEqual(scadere(0, 7), -7)
        self.assertEqual(scadere(7, 0), 7)

    def test_float(self):
        self.assertEqual(scadere(5.5, 2.25), 3.25)
        self.assertAlmostEqual(scadere(0.3, 0.1), 0.2)
        self.assertEqual(scadere(-1.5, -1.5), 0.0)
        self.assertEqual(scadere(1, 0.5), 0.5)


class TestExempleTichet(unittest.TestCase):
    def test_adunare_opuse(self):
        self.assertEqual(adunare(-1, 1), 0)

    def test_scadere_rezultat_zero(self):
        self.assertEqual(scadere(4, 4), 0)

    def test_scadere_float_aproximativ(self):
        self.assertAlmostEqual(scadere(0.5, 0.2), 0.3)


if __name__ == "__main__":
    unittest.main()
