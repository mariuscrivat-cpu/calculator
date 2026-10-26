import os
import re
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class TestMakefile(unittest.TestCase):
    def test_target_uri(self):
        with open(os.path.join(ROOT, "Makefile"), encoding="utf-8") as f:
            content = f.read()
        for target in ("start", "install", "test"):
            self.assertRegex(content, r"(?m)^%s:" % re.escape(target))

    def test_teste_doar_in_tests(self):
        gasite = [n for n in os.listdir(ROOT) if n.startswith("test_") and n.endswith(".py")]
        self.assertEqual(gasite, [])


if __name__ == "__main__":
    unittest.main()
