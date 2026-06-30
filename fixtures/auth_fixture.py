import pytest
from pages.login_page import LoginPage
from utils.utils_config import CONFIG

@pytest.fixture
def logged_page(page):
    login = LoginPage(page)

    login.open()
    login.login(CONFIG["username"], CONFIG["password"])

    assert login.is_logged_in()

    return page
