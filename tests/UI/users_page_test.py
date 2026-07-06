from playwright.sync_api import expect

from pages.dashboard_page import DashboardPage
from pages.users_page import UsersPage
import allure


EXISTING_USER_EMAIL = "a.skout@netafim.com"


@allure.feature("Admin Portal")
@allure.story("Users Management")
@allure.title("Open Users page successfully")
@allure.severity(allure.severity_level.CRITICAL)
def test_open_users_page_successfully(api_logged_page):
    dashboard = DashboardPage(api_logged_page)
    users_page = UsersPage(api_logged_page)

    with allure.step("Open Users page from sidebar"):
        dashboard.sidebar.open_users()

    with allure.step("Validate Users page is opened"):
        users_page.validate_users_page_opened()


@allure.feature("Admin Portal")
@allure.story("Users Management")
@allure.title("Enterprise filter accepts typed value")
@allure.severity(allure.severity_level.NORMAL)
def test_enterprise_filter_accepts_typed_value(api_logged_page):
    dashboard = DashboardPage(api_logged_page)
    users_page = UsersPage(api_logged_page)

    enterprise = "Comp001"

    with allure.step("Open Users page"):
        dashboard.sidebar.open_users()

    with allure.step(f"Type enterprise in filter: {enterprise}"):
        users_page.filter_by_enterprise(enterprise)

    with allure.step("Validate enterprise filter contains typed value"):
        actual_value = users_page.get_enterprise_filter_value()
        assert actual_value == enterprise, (
            f"Expected enterprise filter value '{enterprise}', but got '{actual_value}'"
        )


@allure.feature("Admin Portal")
@allure.story("Users Management")
@allure.title("Email filter accepts typed value")
@allure.severity(allure.severity_level.NORMAL)
def test_email_filter_accepts_typed_value(api_logged_page):
    dashboard = DashboardPage(api_logged_page)
    users_page = UsersPage(api_logged_page)

    email = "a.skout@netafim.com"

    with allure.step("Open Users page"):
        dashboard.sidebar.open_users()

    with allure.step(f"Type email in filter: {email}"):
        users_page.filter_user_by_email(email)

    with allure.step("Validate email filter contains typed value"):
        actual_value = users_page.get_email_filter_value()
        assert actual_value == email, (
            f"Expected email filter value '{email}', but got '{actual_value}'"
        )


@allure.feature("Admin Portal")
@allure.story("Users Management")
@allure.title("Filtered users count is greater than zero")
@allure.severity(allure.severity_level.NORMAL)
def test_filtered_users_count_greater_than_zero(api_logged_page):
    dashboard = DashboardPage(api_logged_page)
    users_page = UsersPage(api_logged_page)

    email = "a.skout@netafim.com"

    with allure.step("Open Users page"):
        dashboard.sidebar.open_users()

    with allure.step(f"Filter users by email: {email}"):
        users_page.filter_user_by_email(email)

    with allure.step("Get filtered users count"):
        users_count = users_page.get_filtered_users_count()

    with allure.step("Validate filtered users count is greater than zero"):
        assert users_count > 0, "Expected at least one filtered user, but found zero"

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


@allure.feature("Admin Portal")
@allure.story("Users Management")
@allure.title("Search non-existing user by email")
@allure.severity(allure.severity_level.NORMAL)
def test_search_non_existing_user_by_email(api_logged_page):
    dashboard = DashboardPage(api_logged_page)
    users_page = UsersPage(api_logged_page)

    non_existing_email = "not.exist.user@example.com"

    with allure.step("Open Users page"):
        dashboard.sidebar.open_users()

    with allure.step(f"Search non-existing user by email: {non_existing_email}"):
        users_page.type_email_filter(non_existing_email)

    with allure.step("Validate searched email is not displayed in grid"):
        users_page.validate_no_user_email_equals(non_existing_email)

# #####################################

@allure.feature("Admin Portal")
@allure.story("User Edit")
@allure.title("Open Edit User page from Users grid")
@allure.severity(allure.severity_level.CRITICAL)
def test_open_edit_user_page_from_users_grid(api_logged_page):
    dashboard = DashboardPage(api_logged_page)
    users_page = UsersPage(api_logged_page)
    user_edit_page = UsersPage(api_logged_page)

    with allure.step("Open Users page"):
        dashboard.sidebar.open_users()

    with allure.step(f"Open user details by email: {EXISTING_USER_EMAIL}"):
        users_page.click_on_found_email(EXISTING_USER_EMAIL)

    with allure.step("Validate Edit User page is opened"):
        user_edit_page.validate_edit_user_page_opened()


@allure.feature("Admin Portal")
@allure.story("User Edit")
@allure.title("Validate Edit User form fields are visible")
@allure.severity(allure.severity_level.CRITICAL)
def test_edit_user_form_fields_are_visible(api_logged_page):
    dashboard = DashboardPage(api_logged_page)
    users_page = UsersPage(api_logged_page)
    user_edit_page = UsersPage(api_logged_page)

    with allure.step("Open Users page"):
        dashboard.sidebar.open_users()

    with allure.step(f"Open user details by email: {EXISTING_USER_EMAIL}"):
        users_page.click_on_found_email(EXISTING_USER_EMAIL)

    with allure.step("Validate user form fields are visible"):
        user_edit_page.validate_user_form_fields_visible()

    with allure.step("Validate action buttons are visible"):
        user_edit_page.validate_action_buttons_visible()


@allure.feature("Admin Portal")
@allure.story("User Edit")
@allure.title("Validate Email field is disabled on Edit User page")
@allure.severity(allure.severity_level.NORMAL)
def test_edit_user_email_field_is_disabled(api_logged_page):
    dashboard = DashboardPage(api_logged_page)
    users_page = UsersPage(api_logged_page)
    user_edit_page = UsersPage(api_logged_page)

    with allure.step("Open Users page"):
        dashboard.sidebar.open_users()

    with allure.step(f"Open user details by email: {EXISTING_USER_EMAIL}"):
        users_page.click_on_found_email(EXISTING_USER_EMAIL)

    with allure.step("Validate Email field is disabled"):
        user_edit_page.validate_email_field_disabled()


@allure.feature("Admin Portal")
@allure.story("User Edit")
@allure.title("Validate Save button is disabled before changes")
@allure.severity(allure.severity_level.NORMAL)
def test_edit_user_save_button_disabled_before_changes(api_logged_page):
    dashboard = DashboardPage(api_logged_page)
    users_page = UsersPage(api_logged_page)
    user_edit_page = UsersPage(api_logged_page)

    with allure.step("Open Users page"):
        dashboard.sidebar.open_users()

    with allure.step(f"Open user details by email: {EXISTING_USER_EMAIL}"):
        users_page.click_on_found_email(EXISTING_USER_EMAIL)

    with allure.step("Validate Save button is disabled before making changes"):
        user_edit_page.validate_save_button_disabled()


@allure.feature("Admin Portal")
@allure.story("User Edit")
@allure.title("Validate Save button becomes enabled after editing First Name")
@allure.severity(allure.severity_level.NORMAL)
def test_edit_user_save_button_enabled_after_first_name_change(api_logged_page):
    dashboard = DashboardPage(api_logged_page)
    users_page = UsersPage(api_logged_page)
    user_edit_page = UsersPage(api_logged_page)

    with allure.step("Open Users page"):
        dashboard.sidebar.open_users()

    with allure.step(f"Open user details by email: {EXISTING_USER_EMAIL}"):
        users_page.click_on_found_email(EXISTING_USER_EMAIL)

    with allure.step("Get current First Name"):
        original_first_name = user_edit_page.get_first_name_value()

    with allure.step("Update First Name without saving"):
        user_edit_page.update_first_name_without_saving(f"{original_first_name}_test")

    with allure.step("Validate Save button becomes enabled"):
        user_edit_page.validate_save_button_enabled()

    with allure.step("Cancel changes without saving"):
        user_edit_page.click_cancel()


@allure.feature("Admin Portal")
@allure.story("User Edit")
@allure.title("Validate Cancel button returns from Edit User page")
@allure.severity(allure.severity_level.NORMAL)
def test_edit_user_cancel_returns_to_users_page(api_logged_page):
    dashboard = DashboardPage(api_logged_page)
    users_page = UsersPage(api_logged_page)
    user_edit_page = UsersPage(api_logged_page)

    with allure.step("Open Users page"):
        dashboard.sidebar.open_users()

    with allure.step(f"Open user details by email: {EXISTING_USER_EMAIL}"):
        users_page.click_on_found_email(EXISTING_USER_EMAIL)

    with allure.step("Click Cancel button"):
        user_edit_page.click_cancel()

    with allure.step("Validate user returned to Users page"):
        users_page.validate_users_page_opened()


@allure.feature("Admin Portal")
@allure.story("User Edit")
@allure.title("Validate Impersonate button is visible and enabled")
@allure.severity(allure.severity_level.NORMAL)
def test_edit_user_impersonate_button_is_enabled(api_logged_page):
    dashboard = DashboardPage(api_logged_page)
    users_page = UsersPage(api_logged_page)
    user_edit_page = UsersPage(api_logged_page)

    with allure.step("Open Users page"):
        dashboard.sidebar.open_users()

    with allure.step(f"Open user details by email: {EXISTING_USER_EMAIL}"):
        users_page.click_on_found_email(EXISTING_USER_EMAIL)

    with allure.step("Validate Impersonate button is enabled"):
        user_edit_page.validate_impersonate_button_enabled()
