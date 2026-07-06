from playwright.sync_api import expect

from pages.dashboard_page import DashboardPage
from pages.users_page import UsersPage
import allure


@allure.feature("Admin Portal")
@allure.story("Users Management")
@allure.title("Search user by email")
@allure.severity(allure.severity_level.CRITICAL)
def test_search_user_by_email(api_logged_page):

    dashboard = DashboardPage(api_logged_page)
    users_page = UsersPage(api_logged_page)

    email = "a.skout@netafim.com"


    with allure.step("Open Users page"):
        dashboard.sidebar.open_users()


    with allure.step(f"Filter users by email: {email}"):
        users_page.filter_user_by_email(email)

    with allure.step("Get first filtered email from grid"):
        displayed_user = users_page.get_first_filtered_email()

    with allure.step("Validate displayed email equals expected email"):
        assert displayed_user == email, (
            f"Expected email: {email}, but got: {displayed_user}"
        )



@allure.feature("Admin Portal")
@allure.story("Users Management")
@allure.title("Search users by enterprise")
@allure.severity(allure.severity_level.NORMAL)
def test_search_users_by_enterprise(api_logged_page):

    dashboard = DashboardPage(api_logged_page)
    users_page = UsersPage(api_logged_page)
    enterprise = "Comp001"

    with allure.step("Open Users page"):
        dashboard.sidebar.open_users()

    with allure.step(f"Filter users by enterprise: {enterprise}"):
        users_page.filter_by_enterprise(enterprise)

    with allure.step("Get filtered enterprises from grid"):
        filtered_enterprises = users_page.get_filtered_enterprises()

    with allure.step("Validate at least one user was found"):
        assert len(filtered_enterprises) > 0, "No users found for the specified enterprise."

    with allure.step("Validate all filtered users belong to expected enterprise"):
        assert all(value.lower() == enterprise.lower() for value in filtered_enterprises)
