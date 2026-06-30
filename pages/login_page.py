from pages.base_page import BasePage
from pages.locators.login_locators import LoginLocators
from utils.utils_config import CONFIG

class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

    def open(self):
        super().open("login")  # או "/login" אם יש route

    def login(self, username, password):
        self.fill(LoginLocators.USERNAME_INPUT, username)
        self.fill(LoginLocators.PASSWORD_INPUT, password)
        self.click(LoginLocators.LOGIN_BUTTON)

    # def is_logged_in(self):
    #     print("Checking if logged in by verifying the visibility of the success indicator.")
    #     return self.page.is_visible(LoginLocators.SUCCESS_INDICATOR)