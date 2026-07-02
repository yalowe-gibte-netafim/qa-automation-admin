from pages.dashboard_page import DashboardPage
from pages.users_page import UsersPage


def test_search_user(api_logged_page):

    dashboard = DashboardPage(api_logged_page)
    users_page = UsersPage(api_logged_page)

    dashboard.sidebar.open_users()
    email = "a.skout@netafim.com"

    users_page.filter_user_by_email(email)

    displayed_user = users_page.get_first_filtered_email()
    api_logged_page.wait_for_timeout(2000)  # Wait for 5 seconds to ensure the page has updated

    assert displayed_user == email, f"Expected email: {email}, but got: {displayed_user}"



def test_search_users_by_enterprise(api_logged_page):

    dashboard = DashboardPage(api_logged_page)
    users_page = UsersPage(api_logged_page)

    enterprise = "Comp001"
    dashboard.sidebar.open_users()
    users_page.filter_by_enterprise(enterprise)
    api_logged_page.wait_for_timeout(2000)

    count_of_filtered_users = users_page.get_filtered_enterprises()
    assert len(count_of_filtered_users) > 0, "No users found for the specified enterprise."
    assert all(value.lower() == enterprise.lower() for value in count_of_filtered_users)

   
