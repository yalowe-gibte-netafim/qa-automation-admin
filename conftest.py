import sys

sys.dont_write_bytecode = True

import os
import pytest
from playwright.sync_api import sync_playwright
from utils.utils_config import CONFIG
from pages.login_page import LoginPage
from playwright.sync_api import expect
from pages.locators.login_locators import LoginLocators



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
def logged_page(page):
    login = LoginPage(page)

    username = os.getenv("TEST_USERNAME") or CONFIG["username"]
    password = os.getenv("TEST_PASSWORD") or CONFIG["password"]

    login.open()
    login.login(username, password)

    return page
