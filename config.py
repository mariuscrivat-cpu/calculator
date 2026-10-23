import os

DEFAULT_HOST = "127.0.0.1"
DEFAULT_PORT = 8080
ENV_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".env.local")


def parse_env_file(path):
    values = {}
    if not os.path.isfile(path):
        return values
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, value = line.split("=", 1)
            values[key.strip()] = value.strip().strip('"').strip("'")
    return values


def load_config(env_file=ENV_FILE, environ=None):
    """Prioritate: variabile de mediu reale, apoi .env.local, apoi valorile implicite."""
    environ = os.environ if environ is None else environ
    file_values = parse_env_file(env_file)

    def get(key, default):
        return environ.get(key) or file_values.get(key) or default

    return {
        "host": get("HOST", DEFAULT_HOST),
        "port": int(get("PORT", DEFAULT_PORT)),
    }
