from playwright.sync_api import expect

from pages.base_page import BasePage
from pages.locators.users_page_locators import UsersLocators
import allure

class UsersPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

    @allure.step("Filter users by email: {email}")
    def filter_user_by_email(self, email):
        self.fill_value(UsersLocators.EMAIL_FILTER, email)

        first_email_cell = self.page.locator(UsersLocators.USER_EMAIL_CELL_AG).first
        expect(first_email_cell).to_be_visible()


    @allure.step("Filter users by enterprise: {enterprise}")
    def filter_by_enterprise(self, enterprise):
        self.fill_value(UsersLocators.ENTERPRISE_FILTER, enterprise)

        first_enterprise_cell = self.page.locator(UsersLocators.USER_ENTERPRISE_CELL_AG).first
        expect(first_enterprise_cell).to_be_visible()


    @allure.step("Click on found email: {user_email}")
    def click_on_found_email(self, user_email):
        self.filter_user_by_email(user_email)
        self.click_on_element(f"{UsersLocators.USER_EMAIL_CELL_AG} >> text={user_email}")
        
    @allure.step("Get count of filtered users")
    def get_filtered_users_count(self):
        return self.page.locator(UsersLocators.USER_EMAIL_CELL_AG).count()
    
    @allure.step("Get first filtered email")
    def get_first_filtered_email(self):
        
        email_cell = self.page.locator(UsersLocators.USER_EMAIL_CELL_AG).first
        expect(email_cell).to_be_visible()

        return email_cell.inner_text().strip()

    @allure.step("Get filtered enterprises")
    def get_filtered_enterprises(self):

        cells = self.page.locator(UsersLocators.USER_ENTERPRISE_CELL_AG)
        expect(cells.first).to_be_visible()

        values = cells.all_inner_texts()
        return [value.strip() for value in values if value.strip()]
    
    @allure.step("Impersonate user by email: {user_email}")
    def impersonate_user_by_email(self, user_email):
        self.filter_user_by_email(user_email)
        self.click_on_element(f"{UsersLocators.USER_EMAIL_CELL_AG} >> text={user_email}")
        self.click_on_element(UsersLocators.IMPERSONATE_BUTTON)
    

    @allure.step("Validate Users page is opened")
    def validate_users_page_opened(self):
        self.validate_element_text(UsersLocators.PAGE_TITLE, "USERS INFO")


    @allure.step("Get email filter value")
    def get_email_filter_value(self):
        return self.get_element_value(UsersLocators.EMAIL_FILTER)


    @allure.step("Get enterprise filter value")
    def get_enterprise_filter_value(self):
        return self.get_element_value(UsersLocators.ENTERPRISE_FILTER)


    @allure.step("Validate no user email equals: {email}")
    def validate_no_user_email_equals(self, email):
        email_cells = self.page.locator(UsersLocators.USER_EMAIL_CELL_AG)

        if email_cells.count() == 0:
            return

        values = email_cells.all_inner_texts()
        cleaned_values = [value.strip() for value in values if value.strip()]

        assert email not in cleaned_values, (
            f"Unexpectedly found email '{email}' in filtered results: {cleaned_values}"
        )
    
    @allure.step("Type email filter without waiting for results: {email}")
    def type_email_filter(self, email):
        self.fill_value(UsersLocators.EMAIL_FILTER, email)


    @allure.step("Validate Edit User page is opened")
    def validate_edit_user_page_opened(self):
        expect(self.page.locator(UsersLocators.PAGE_TITLE)).to_be_visible()
        expect(self.page).to_have_url(lambda url: "/users/edit/" in url)

    @allure.step("Validate user form fields are visible")
    def validate_user_form_fields_visible(self):
        expect(self.page.locator(UsersLocators.USER_NAME_INPUT)).to_be_visible()
        expect(self.page.locator(UsersLocators.FIRST_NAME_INPUT)).to_be_visible()
        expect(self.page.locator(UsersLocators.LAST_NAME_INPUT)).to_be_visible()
        expect(self.page.locator(UsersLocators.EMAIL_INPUT)).to_be_visible()
        expect(self.page.locator(UsersLocators.PHONE_INPUT)).to_be_visible()
        expect(self.page.locator(UsersLocators.ENTERPRISE_INPUT)).to_be_visible()

    @allure.step("Validate action buttons are visible")
    def validate_action_buttons_visible(self):
        expect(self.page.locator(UsersLocators.IMPERSONATE_BUTTON)).to_be_visible()
        expect(self.page.locator(UsersLocators.CANCEL_BUTTON)).to_be_visible()
        expect(self.page.locator(UsersLocators.SAVE_BUTTON)).to_be_visible()

    @allure.step("Validate email field is disabled")
    def validate_email_field_disabled(self):
        expect(self.page.locator(UsersLocators.EMAIL_INPUT)).to_be_disabled()

    @allure.step("Validate Save button is disabled")
    def validate_save_button_disabled(self):
        expect(self.page.locator(UsersLocators.SAVE_BUTTON)).to_be_disabled()

    @allure.step("Validate Save button is enabled")
    def validate_save_button_enabled(self):
        expect(self.page.locator(UsersLocators.SAVE_BUTTON)).to_be_enabled()

    @allure.step("Get first name value")
    def get_first_name_value(self):
        return self.page.locator(UsersLocators.FIRST_NAME_INPUT).input_value()

    @allure.step("Update first name without saving: {first_name}")
    def update_first_name_without_saving(self, first_name):
        first_name_input = self.page.locator(UsersLocators.FIRST_NAME_INPUT)

        expect(first_name_input).to_be_visible()
        first_name_input.fill(first_name)

    @allure.step("Click Cancel button")
    def click_cancel(self):
        self.click_on_element(UsersLocators.CANCEL_BUTTON)

    @allure.step("Validate Impersonate button is enabled")
    def validate_impersonate_button_enabled(self):
        expect(self.page.locator(UsersLocators.IMPERSONATE_BUTTON)).to_be_enabled()
