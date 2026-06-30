import os
from playwright.sync_api import expect, sync_playwright
from pages.login_page import LoginPage
from utils.utils_config import CONFIG


with sync_playwright() as p:
    username = os.getenv("USERNAME")
    password = os.getenv("PASSWORD")
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    login = LoginPage(page)

    login.open()
    login.login(username, password)
    expect(page).to_have_url(lambda url: "login" not in url)

    # ✅ שומר session
    context.storage_state(path="state.json")

    browser.close()