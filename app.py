import os

from config import load_config

WEB_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "web")


def main():
    import eel

    config = load_config()
    eel.init(WEB_DIR)
    eel.start("index.html", host=config["host"], port=config["port"], mode=False)


if __name__ == "__main__":
    main()
