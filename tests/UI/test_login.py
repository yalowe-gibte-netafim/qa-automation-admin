import os
from conftest import page
from pages.dashboard_page import DashboardPage
from pages.locators.login_locators import LoginLocators
from pages.login_page import LoginPage
from playwright.sync_api import expect
from utils.utils_config import CONFIG


def test_login(page):
    login = LoginPage(page)
    
    username = os.getenv("TEST_USERNAME")
    password = os.getenv("TEST_PASSWORD")

    username = os.getenv("TEST_USERNAME") or CONFIG["username"]
    password = os.getenv("TEST_PASSWORD") or CONFIG["password"]

    login.open()
    login.login(username, password)
    # expect(page.locator(LoginLocators.SUCCESS_INDICATOR)).to_be_visible(timeout=CONFIG["timeout"])

def test_go_to_users(logged_page):
    dashboard = DashboardPage(logged_page)

    dashboard.sidebar.open_users()    
    expect(logged_page.locator(LoginLocators.BU_DASHBOARD_TITLE)).to_have_text("USERS INFO")


    # assert "users" in page.url.lower(),"The URL does not contain 'users' after navigating to the dashboard."