import os
from conftest import page
from pages.dashboard_page import DashboardPage
from pages.locators.login_locators import LoginLocators
from pages.login_page import LoginPage
from playwright.sync_api import expect
from utils.utils_config import CONFIG


# def test_login(page):
#     login = LoginPage(page)
#     username = os.getenv("TEST_USERNAME")
#     password = os.getenv("TEST_PASSWORD")
#     username = os.getenv("TEST_USERNAME") or CONFIG["username"]
#     password = os.getenv("TEST_PASSWORD") or CONFIG["password"]
#     login.open()
#     login.login(username, password)
#     # expect(page.locator(LoginLocators.SUCCESS_INDICATOR)).to_be_visible(timeout=CONFIG["timeout"])



def test_login_via_api(api_logged_page):

    print("URL:", api_logged_page.url)

    api_logged_page.screenshot(
        path="login_debug.png",
        full_page=True
    )

    dashboard = DashboardPage(api_logged_page)

    dashboard.is_element_visible(LoginLocators.SUCCESS_INDICATOR)