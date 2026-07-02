
from pages.base_page import BasePage


class SidebarComponent(BasePage):
    def __init__(self, page):
        super().__init__(page)

    # 🔹 Locators
    TECH_TOOLBOX = "text=Tech Toolbox"
    USERS = "text=Users"
    BUS = "text=BU's"
    REGIONS = "text=Regions"
    COMPANIES = "text=Companies"
    FARMS = "text=Farms"
    CROP_MANAGEMENT = "text=Crop management"
    DEVICE_MANAGEMENT = "text=Device management"
    DOCUMENTATION = "text=Documentation"
    LOGOUT = "text=Logout"

    # 🔹 Actions
    def open_tech_toolbox(self):
        self.click_on_element(self.TECH_TOOLBOX)

    def open_users(self):
        self.click_on_element(self.USERS)

    def open_bus(self):
        self.click_on_element(self.BUS)

    def open_regions(self):
        self.click_on_element(self.REGIONS)

    def open_companies(self):
        self.click_on_element(self.COMPANIES)

    def open_farms(self):
        self.click_on_element(self.FARMS)

    def open_crop_management(self):
        self.click_on_element(self.CROP_MANAGEMENT)

    def open_device_management(self):
        self.click_on_element(self.DEVICE_MANAGEMENT)

    def open_documentation(self):
        self.click_on_element(self.DOCUMENTATION)

    def logout(self):
        self.click_on_element(self.LOGOUT)