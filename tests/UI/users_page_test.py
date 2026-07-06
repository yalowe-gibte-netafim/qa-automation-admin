from playwright.sync_api import expect

from pages.dashboard_page import DashboardPage
from pages.users_page import UsersPage
import allure

@allure.title("Test Login via API")
def test_search_user(api_logged_page):

    dashboard = DashboardPage(api_logged_page)
    users_page = UsersPage(api_logged_page)

    with allure.step("Open Users page"):
        dashboard.sidebar.open_users()

    email = "a.skout@netafim.com"

    with allure.step(f"Filter users by email: {email}"):
        users_page.filter_user_by_email(email)

    with allure.step("Get first filtered email"):
        displayed_user = users_page.get_first_filtered_email()
    api_logged_page.wait_for_timeout(2000)

    with allure.step(f"Assert that the displayed user email matches the expected email: {email}"):
        assert displayed_user == email, f"Expected email: {email}, but got: {displayed_user}"


@allure.title("Test Search Users by Enterprise")
def test_search_users_by_enterprise(api_logged_page):

    dashboard = DashboardPage(api_logged_page)
    users_page = UsersPage(api_logged_page)

    enterprise = "Comp001"
    with allure.step(f"Open Users page and filter by enterprise: {enterprise}"):
        dashboard.sidebar.open_users()
    with allure.step(f"Filter users by enterprise: {enterprise}"):
        users_page.filter_by_enterprise(enterprise)
    
    
    with allure.step(f"Assert that the second filtered user's enterprise is: {enterprise}"):
        expect(api_logged_page.locator('div[col-id="enterpriseName"]').nth(1)).to_have_text("Comp001")

    with allure.step(f"Get filtered enterprises for the specified enterprise: {enterprise}"):
        count_of_filtered_users = users_page.get_filtered_enterprises()
        assert len(count_of_filtered_users) > 0, "No users found for the specified enterprise."
    with allure.step(f"Assert that all filtered users belong to the enterprise: {enterprise}"):
        assert all(value.lower() == enterprise.lower() for value in count_of_filtered_users)

   