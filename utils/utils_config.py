import json
import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

def get_env():

    return os.getenv("ENV", "qa")

def load_config():
    env = get_env()
    config_path = BASE_DIR / "configs" / f"{env}.json"

    print(f"Loading config from: {config_path}")

    if not config_path.exists():
        raise FileNotFoundError(f"Config file not found: {config_path}")

    with open(config_path, encoding="utf-8") as f:
        config = json.load(f)
    
    
    config["username"] = os.getenv("TEST_USERNAME")
    config["password"] = os.getenv("TEST_PASSWORD")

    if not config["username"]:
        raise ValueError("TEST_USERNAME is missing.")

    if not config["password"]:
        raise ValueError("TEST_PASSWORD is missing.")

    return config

CONFIG = load_config()