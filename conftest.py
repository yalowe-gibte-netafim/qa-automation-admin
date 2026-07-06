import sys
import os
sys.dont_write_bytecode = True

import allure
import pytest
from playwright.sync_api import sync_playwright

from auth.token_manager import TokenManager
from auth.auth_injector import inject_storage
from pages.login_page import LoginPage
from utils.utils_config import CONFIG


@pytest.fixture(scope="function")
def page(request):
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

    if TokenManager.is_token_valid():
        print("Token is valid. Injecting token into storage...")
        storage = TokenManager.load_storage()
        inject_storage(page, storage)

        page.goto(CONFIG["base_url"])
        page.wait_for_load_state("domcontentloaded")
    
    else:
        print("Token is invalid or expired. Performing UI login...")
        login_page = LoginPage(page)
        login_page.open()
        login_page.login(CONFIG["username"], CONFIG["password"])

        page.wait_for_load_state("domcontentloaded")

        storage = TokenManager.get_local_storage(page)
        TokenManager.save_storage(storage)

        print("Token saved successfully to storage after login.")

    return page


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):

    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:

        page = item.funcargs.get("api_logged_page") or item.funcargs.get("page")

        if page:

            screenshot = page.screenshot(full_page=True)

            allure.attach(
                screenshot,name="Failure Screenshot",
                attachment_type=allure.attachment_type.PNG
            )

            allure.attach(
                page.url, name="Failure Page URL", attachment_type=allure.attachment_type.TEXT,
            )
