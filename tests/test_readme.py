import os
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class TestReadme(unittest.TestCase):
    def setUp(self):
        with open(os.path.join(ROOT, "README.md"), encoding="utf-8") as f:
            self.content = f.read()

    def test_mentioneaza_functiile(self):
        for name in ("adunare", "scadere", "multiply", "divide", "putere(a, b)"):
            self.assertIn(name, self.content)

    def test_mentioneaza_comenzi_si_config(self):
        for item in ("make install", "make start", "make test", "tests/",
                     ".env.local", "python-dotenv", "8080", "web/index.html"):
            self.assertIn(item, self.content)

    def test_caile_din_readme_exista(self):
        for path in ("calculator.py", "config.py", "app.py", "web/index.html",
                     "Makefile", "requirements.txt", "verify.sh", ".env.example"):
            self.assertTrue(os.path.exists(os.path.join(ROOT, path)), path)


if __name__ == "__main__":
    unittest.main()
