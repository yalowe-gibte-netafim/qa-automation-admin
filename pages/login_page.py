import os

from pages.base_page import BasePage
from pages.locators.login_locators import LoginLocators
from utils.utils_config import CONFIG

class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

    def open(self):
        super().open("login")

    def login(self, username, password):
        
        if not username or not password:
            raise ValueError("Username or Password is missing")

        self.fill(LoginLocators.USERNAME_INPUT, os.getenv("USERNAME"))
        self.fill(LoginLocators.PASSWORD_INPUT, os.getenv("PASSWORD"))
        self.click(LoginLocators.LOGIN_BUTTON)

    # def is_logged_in(self):
    #     print("Checking if logged in by verifying the visibility of the success indicator.")
    #     return self.page.is_visible(LoginLocators.SUCCESS_INDICATOR)