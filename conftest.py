import sys
import os
sys.dont_write_bytecode = True

from auth.token_manager import TokenManager


import pytest
from playwright.sync_api import sync_playwright
from utils.utils_config import CONFIG
from pages.login_page import LoginPage
from auth.auth_injector import inject_storage




@pytest.fixture(scope="function")
def page():
    with sync_playwright() as p:
        headless = os.getenv("CI", "").lower() == "true"
        browser = p.chromium.launch(headless=headless)
        context = browser.new_context(
            base_url=CONFIG["base_url"],
            viewport={"width": 1280, "height": 720},
        )
        page = context.new_page()
        page.set_default_timeout(CONFIG["timeout"])

        yield page

        context.close()
        browser.close()



@pytest.fixture
def api_logged_page(page):
    print("API Logged Page Fixture: Checking token validity...")

    
    is_valid = TokenManager.is_token_valid()

    if is_valid:

        print("Token is valid - using saved session")


    if TokenManager.is_token_valid():

        print("Using saved session")
        storage = TokenManager.load_storage()

        inject_storage(page, storage)

        page.goto(CONFIG["base_url"])

    else:

        print("Performing UI login")

        login = LoginPage(page)

        login.open()

        login.login(
            CONFIG["username"],
            CONFIG["password"]
        )
        
        
        page.wait_for_load_state("networkidle")
        page.wait_for_timeout(3000)
        print("URL BEFORE SAVE:", page.url)

        storage = TokenManager.get_local_storage(page)
        print("Storage after login:", storage)

        TokenManager.save_storage(storage)
        print("Storage keys after save:", storage.keys())

    return page