from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage
from utils.utils_config import CONFIG


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    login = LoginPage(page)

    login.open()
    login.login(CONFIG["username"], CONFIG["password"])

    # ✅ שומר session
    context.storage_state(path="state.json")

    browser.close()