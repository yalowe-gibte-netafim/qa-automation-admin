import os
from conftest import page
from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage
from playwright.sync_api import expect
from utils.utils_config import CONFIG


def test_login(page):
    login = LoginPage(page)
    login.open()
    login.login(os.getenv("USERNAME"), os.getenv("PASSWORD"))
    # expect(page.locator(LoginLocators.SUCCESS_INDICATOR)).to_be_visible(timeout=CONFIG["timeout"])



def test_go_to_users(logged_page):
    dashboard = DashboardPage(logged_page)

    dashboard.sidebar.open_users()

    assert "users" in logged_page.url.lower()

    # assert "users" in page.url.lower(),"The URL does not contain 'users' after navigating to the dashboard."