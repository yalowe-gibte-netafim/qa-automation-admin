from conftest import page
from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage
from playwright.sync_api import expect
from utils.utils_config import CONFIG


def test_login(page):
    login = LoginPage(page)
    login.open()
    login.login(CONFIG["username"], CONFIG["password"])
    # expect(page.locator(LoginLocators.SUCCESS_INDICATOR)).to_be_visible(timeout=CONFIG["timeout"])


def test_go_to_uses(logged_page):
    dashboard_page = DashboardPage(logged_page)
    dashboard_page.sidebar.open_users()
    # assert "users" in logged_page.url.lower(),"The URL does not contain 'users' after navigating to the dashboard."