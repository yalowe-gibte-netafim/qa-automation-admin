from pages.dashboard_page import DashboardPage
from pages.locators.login_locators import LoginLocators

def test_login_via_api(api_logged_page):

    print("URL:", api_logged_page.url)

    api_logged_page.screenshot(
        path="login_debug.png",
        full_page=True
    )
    dashboard = DashboardPage(api_logged_page)

    dashboard.is_element_visible(LoginLocators.SUCCESS_INDICATOR)
    print("FINAL URL:", api_logged_page.url)