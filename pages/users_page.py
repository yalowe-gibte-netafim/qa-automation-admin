
from pages.base_page import BasePage
from pages.locators.users_page_locators import UsersLocators
import allure

class UsersPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

    @allure.step("Filter users by email: {email}")
    def filter_user_by_email(self, email):
        self.fill_value(UsersLocators.EMAIL_FILTER, email)

    @allure.step("Filter users by enterprise: {enterprise}")
    def filter_by_enterprise(self, enterprise):
        self.fill_value(UsersLocators.ENTERPRISE_FILTER, enterprise)

    @allure.step("Click on found email: {user_email}")
    def click_on_found_email(self, user_email):
        self.filter_user_by_email(user_email)
        self.click_on_element(f"{UsersLocators.USER_EMAIL_CELL} >> text={user_email}")\
        
    @allure.step("Get count of filtered users")
    def get_filtered_users_count(self):
        return self.page.locator('.ag-row div[col-id="emailAddress"]').count()
    
    @allure.step("Get first filtered email")
    def get_first_filtered_email(self):
        return self.page.locator('.ag-row div[col-id="emailAddress"]').first.inner_text()

    @allure.step("Get filtered enterprises")
    def get_filtered_enterprises(self):
        values = self.page.locator('div[col-id="enterpriseName"]').all_inner_texts()
        
        return [value.strip() for value in values if value.strip() != "Enterprise"]
    
    with allure.step("Impersonate user by email: {user_email}"):
        def impersonate_user_by_email(self, user_email):
            self.filter_user_by_email(user_email)
            self.click_on_element(f"{UsersLocators.USER_EMAIL_CELL} >> text={user_email}")
            self.click_on_element(UsersLocators.IMPERSONATE_BUTTON)