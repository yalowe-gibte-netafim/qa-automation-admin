import json
import time
from pathlib import Path

import jwt


class TokenManager:
    STORAGE_FILE = Path("data/auth_storage.json")

    @classmethod
    def is_storage_exists(cls):
        return cls.STORAGE_FILE.exists()
    
    @classmethod
    def load_storage(cls):

        if not cls.is_storage_exists():
            return {}
        
        try:
            with open(cls.STORAGE_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON from storage file: {e}")
            return {}
        
    @classmethod
    def save_storage(cls, storage_data):
        with open(cls.STORAGE_FILE, "w", encoding="utf-8") as f:
            json.dump(storage_data, f, ensure_ascii=False, indent=4)
    
    @classmethod
    def is_token_valid(cls):
        print("Checking token validity...")
        storage_data = cls.load_storage()
        if not storage_data:
            print("Storage file not found")
            return False
        
        token = storage_data.get("access_token")
        if not token:
            print("Access token not found")
            return False

        try:
            claims = jwt.decode(token, options={"verify_signature": False})
            valid = time.time() < claims["exp"]
            print(f"Token valid: {valid}")
            return valid
        
        except Exception as e:
            print(f"Error decoding token: {e}")
            return False
        

    @classmethod
    def get_local_storage(cls, page):
        return page.evaluate(
            "() => ({...localStorage})"
        )