import os
import re
import unittest

WEB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "web")


def read(name):
    with open(os.path.join(WEB, name), encoding="utf-8") as f:
        return f.read()


class TestUI(unittest.TestCase):
    def test_fara_css_js_custom(self):
        self.assertEqual(os.listdir(WEB), ["index.html"])

    def test_ecran(self):
        self.assertIn('id="display"', read("index.html"))

    def test_butoane(self):
        html = read("index.html")
        keys = set(re.findall(r"'([^']+)'", re.search(r"x-for=\"k in \[([^\]]+)\]", html).group(1)))
        expected = set("0123456789") | {".", "+", "\u2212", "\u00d7", "\u00f7", "=", "C"}
        self.assertTrue(expected <= keys, expected - keys)

    def test_librarii_externe(self):
        html = read("index.html")
        for lib in ("bootstrap", "alpinejs", "mathjs"):
            self.assertRegex(html, r"https://cdn\.jsdelivr\.net/npm/%s@" % lib)
        self.assertIn("/eel.js", html)

    def test_fara_referinte_locale_css_js(self):
        html = read("index.html")
        self.assertNotIn("style.css", html)
        self.assertNotIn("script.js", html)
        self.assertNotIn("<style", html)


if __name__ == "__main__":
    unittest.main()
