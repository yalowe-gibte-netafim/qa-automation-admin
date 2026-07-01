
class SidebarComponent:
    def __init__(self, page):
        self.page = page

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
        self.page.locator(self.TECH_TOOLBOX).click()

    def open_users(self):
        self.page.locator(self.USERS).click()
        self.page.wait_for_timeout(1000)  # Wait for 1 second to ensure the page has loaded

    def open_bus(self):
        self.page.locator(self.BUS).click()
        self.page.wait_for_timeout(1000)  # Wait for 1 second to ensure the page has loaded
    def open_regions(self):
        self.page.locator(self.REGIONS).click()
        self.page.wait_for_timeout(1000)  # Wait for 1 second to ensure the page has loaded

    def open_companies(self):
        self.page.locator(self.COMPANIES).click()
        self.page.wait_for_timeout(1000)  # Wait for 1 second to ensure the page has loaded

    def open_farms(self):
        self.page.locator(self.FARMS).click()
        self.page.wait_for_timeout(1000)  # Wait for 1 second to ensure the page has loaded

    def open_crop_management(self):
        self.page.locator(self.CROP_MANAGEMENT).click()
        self.page.wait_for_timeout(1000)  # Wait for 1 second to ensure the page has loaded

    def open_device_management(self):
        self.page.locator(self.DEVICE_MANAGEMENT).click()
        self.page.wait_for_timeout(1000)  # Wait for 1 second to ensure the page has loaded

    def open_documentation(self):
        self.page.locator(self.DOCUMENTATION).click()

    def logout(self):
        self.page.locator(self.LOGOUT).click()