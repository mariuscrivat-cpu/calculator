import os
import re
import unittest

WEB = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "web")


def read(name):
    with open(os.path.join(WEB, name), encoding="utf-8") as f:
        return f.read()


class TestUI(unittest.TestCase):
    def test_doar_css_extern_custom(self):
        self.assertEqual(sorted(os.listdir(WEB)), ["index.html", "style.css"])

    def test_fundal_galben_ecran(self):
        css = read("style.css")
        rule = re.search(r"#display\s*\{([^}]*)\}", css).group(1)
        self.assertRegex(rule, r"background-color:\s*#ffeb3b")
        self.assertIn("color:", rule.replace("background-color", ""))
        self.assertIn('href="/style.css"', read("index.html"))

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
        self.assertNotIn("script.js", html)
        self.assertNotIn("<style", html)
        self.assertNotIn("background", html)


if __name__ == "__main__":
    unittest.main()
