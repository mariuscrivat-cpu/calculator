import unittest
from unittest import mock

import app


class TestApp(unittest.TestCase):
    def test_porneste_pe_portul_configurat(self):
        eel = mock.MagicMock()
        cfg = {"host": "127.0.0.1", "port": 8080}
        with mock.patch.dict("sys.modules", {"eel": eel}), mock.patch.object(app, "load_config", return_value=cfg):
            app.main()
        eel.init.assert_called_once_with(app.WEB_DIR)
        eel.start.assert_called_once_with("index.html", host="127.0.0.1", port=8080, mode=False)


if __name__ == "__main__":
    unittest.main()
