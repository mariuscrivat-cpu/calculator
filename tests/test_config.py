import os
import tempfile
import unittest

from config import ENV_FILE, load_config

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class TestConfig(unittest.TestCase):
    def test_valori_implicite(self):
        cfg = load_config(env_file="/nonexistent/.env.local", environ={})
        self.assertEqual(cfg, {"host": "127.0.0.1", "port": 8080})

    def test_valori_din_fisier(self):
        with tempfile.TemporaryDirectory() as d:
            path = os.path.join(d, ".env.local")
            with open(path, "w") as f:
                f.write("# comentariu\nHOST=0.0.0.0\nPORT=9090\n")
            cfg = load_config(env_file=path, environ={})
        self.assertEqual(cfg, {"host": "0.0.0.0", "port": 9090})

    def test_foloseste_python_dotenv(self):
        import config
        import dotenv

        self.assertIs(config.dotenv_values, dotenv.dotenv_values)
        self.assertFalse(hasattr(config, "parse_env_file"))

    def test_python_dotenv_in_requirements(self):
        path = os.path.join(ROOT, "requirements.txt")
        with open(path) as f:
            self.assertIn("python-dotenv", f.read())

    def test_valori_cu_ghilimele_si_export(self):
        with tempfile.TemporaryDirectory() as d:
            path = os.path.join(d, ".env.local")
            with open(path, "w") as f:
                f.write('export HOST="0.0.0.0"\nPORT=\'7000\'\n')
            cfg = load_config(env_file=path, environ={})
        self.assertEqual(cfg, {"host": "0.0.0.0", "port": 7000})

    def test_mediul_are_prioritate(self):
        cfg = load_config(env_file="/nonexistent", environ={"PORT": "1234"})
        self.assertEqual(cfg["port"], 1234)

    def test_env_local_din_proiect_foloseste_8080(self):
        cfg = load_config(env_file=ENV_FILE, environ={})
        self.assertEqual(cfg["port"], 8080)
        self.assertEqual(cfg["host"], "127.0.0.1")


if __name__ == "__main__":
    unittest.main()
