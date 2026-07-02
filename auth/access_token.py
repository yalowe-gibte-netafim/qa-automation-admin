import os
from dotenv import load_dotenv

load_dotenv()

ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ID_TOKEN = os.getenv("ID_TOKEN")
REFRESH_TOKEN = os.getenv("REFRESH_TOKEN")
EXPIRES_AT = os.getenv("EXPIRES_AT")