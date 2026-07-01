from pages.base_page import BasePage
from pages.locators.login_locators import LoginLocators
from playwright.sync_api import expect


class LoginPage(BasePage):

    def open(self):
        self.page.goto("/")

    def login(self, username, password):
        if not username or not password:
            raise ValueError("Username or Password is missing")

        self.fill(LoginLocators.USERNAME_INPUT, username)
        self.fill(LoginLocators.PASSWORD_INPUT, password)
        self.click(LoginLocators.LOGIN_BUTTON)

        # ✅ חשוב — לחכות שיצא מה-login
        expect(self.page).not_to_have_url("**login**")
        print(f"Logged in as {username}")