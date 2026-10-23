import os
import re
import unittest

WEB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "web")


def read(name):
    with open(os.path.join(WEB, name), encoding="utf-8") as f:
        return f.read()


class TestUI(unittest.TestCase):
    def test_fisiere_exista(self):
        for name in ("index.html", "style.css", "script.js"):
            self.assertTrue(os.path.isfile(os.path.join(WEB, name)), name)

    def test_ecran(self):
        self.assertIn('id="display"', read("index.html"))

    def test_butoane(self):
        html = read("index.html")
        keys = set(re.findall(r'data-key="([^"]+)"', html))
        expected = set("0123456789") | {".", "+", "−", "×", "÷", "=", "C"}
        self.assertTrue(expected <= keys, expected - keys)

    def test_referinte_css_js(self):
        html = read("index.html")
        self.assertIn("style.css", html)
        self.assertIn("script.js", html)


if __name__ == "__main__":
    unittest.main()
