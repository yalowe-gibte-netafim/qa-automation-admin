from playwright.sync_api import Page, expect
from utils.utils_config import CONFIG

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def open(self, path=""):
        url = f"{CONFIG['base_url']}/{path}".rstrip("/")
        self.page.goto(url)

    def click_on_element(self, selector):
        locator = self.page.locator(selector)
        expect(locator).to_be_visible()
        locator.click()

    def fill_value(self, selector, value):
        self.page.locator(selector).fill(value)
    
    def is_element_visible(self, selector):
        locator = self.page.locator(selector)
        expect(locator).to_be_visible()
        return locator.is_visible()
    
    def wait_for_timeout(self, timeout):
        self.page.wait_for_timeout(timeout)

    def get_element_count(self, selector):
        locator = self.page.locator(selector)
        expect(locator).to_be_visible()
        return locator.count()
    
    def get_element_text(self, selector, text=None):
        locator = self.page.locator(selector)
        expect(locator).to_be_visible()
        return locator.inner_text()
    
    def validate_element_text(self, selector, expected_text):
        locator = self.page.locator(selector)
        expect(locator).to_have_text(expected_text)


    def get_element_attribute(self, selector, attribute):
        locator = self.page.locator(selector)
        expect(locator).to_be_visible()
        return locator.get_attribute(attribute)
    
    def get_element_value(self, selector):
        locator = self.page.locator(selector)
        expect(locator).to_be_visible()
        return locator.input_value()
    
    def get_element_locator(self, selector):
        locator = self.page.locator(selector)
        expect(locator).to_be_visible()
        return locator
    
    def wait_element_visible(self, selector, timeout=CONFIG["timeout"]):
        expect(self.page.locator(selector)).to_be_visible(timeout=timeout)

    def wait_element_not_visible(self, selector, timeout=CONFIG["timeout"]):
        expect(self.page.locator(selector)).not_to_be_visible(timeout=timeout)