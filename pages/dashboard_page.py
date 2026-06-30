from pages.base_page import BasePage
from pages.components.sidebar_component import SidebarComponent


class DashboardPage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.sidebar = SidebarComponent(page)