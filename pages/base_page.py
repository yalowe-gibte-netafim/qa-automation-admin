from playwright.sync_api import Page
from utils.utils_config import CONFIG

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def open(self, path=""):
        url = f"{CONFIG['base_url']}/{path}".rstrip("/")
        self.page.goto(url)

    def click(self, selector):
        self.page.click(selector)

    def fill(self, selector, value):
        self.page.fill(selector, value)

    def get_text(self, selector):
        return self.page.inner_text(selector)
    
    def is_visible(self, selector):
        return self.page.is_visible(selector)
    
    def wait_for_timeout(self, timeout):
        self.page.wait_for_timeout(timeout)