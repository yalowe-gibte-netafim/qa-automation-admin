import sys
sys.dont_write_bytecode = True

import os
import pytest
from playwright.sync_api import sync_playwright
from utils.utils_config import CONFIG
from pages.login_page import LoginPage
from playwright.sync_api import expect
from pages.locators.login_locators import LoginLocators


from auth.auth_injector import inject_oidc_session
from auth.access_token import (
    ACCESS_TOKEN,
    ID_TOKEN,
    REFRESH_TOKEN,
    EXPIRES_AT,
)




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

    inject_oidc_session(
        page=page,
        access_token=ACCESS_TOKEN,
        id_token=ID_TOKEN,
        refresh_token=REFRESH_TOKEN,
        expires_at=EXPIRES_AT,
    )

    page.goto(CONFIG["base_url"])

    return page

