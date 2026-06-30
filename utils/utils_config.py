import json
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

def get_env():
    return os.getenv("ENV", "qa")

def load_config():
    env = get_env()
    config_path = BASE_DIR / "configs" / f"{env}.json"

    print(f"Loading config from: {config_path}")

    if not config_path.exists():
        raise FileNotFoundError(f"Config file not found: {config_path}")

    with open(config_path) as f:
        return json.load(f)

CONFIG = load_config()