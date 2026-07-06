from pages.base_page import BasePage
from pages.components.components_locator import SidebarLocators
from pages.locators.commonlocators import CommonLocators


class SidebarComponent(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.SidebarLocators = SidebarLocators
        self.CommonLocators = CommonLocators

    def open_tech_toolbox(self):
        self.click_on_element(self.SidebarLocators.TECH_TOOLBOX)

    def open_users(self):
        self.click_on_element(self.SidebarLocators.USERS)
        self.validate_element_text(self.CommonLocators.DASHBOARD_TITLE, "USERS INFO")


    def open_bus(self):
        self.click_on_element(self.SidebarLocators.BUS)

    def open_regions(self):
        self.click_on_element(self.SidebarLocators.REGIONS)

    def open_companies(self):
        self.click_on_element(self.SidebarLocators.COMPANIES)

    def open_farms(self):
        self.click_on_element(self.SidebarLocators.FARMS)

    def open_crop_management(self):
        self.click_on_element(self.SidebarLocators.CROP_MANAGEMENT)

    def open_device_management(self):
        self.click_on_element(self.SidebarLocators.DEVICE_MANAGEMENT)

    def open_documentation(self):
        self.click_on_element(self.SidebarLocators.DOCUMENTATION)

    def logout(self):
        self.click_on_element(self.SidebarLocators.LOGOUT)