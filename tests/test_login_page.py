import pytest

from pages.logged_in_successfully_page import LoggedInSuccessfullyPage
from pages.login_page import LoginPage


class TestPositiveScenarios:

    @pytest.mark.login
    @pytest.mark.positive
    def test_positive_login(self, driver):
        login_page = LoginPage(driver)
        logged_in_successfully_page = LoggedInSuccessfullyPage(driver)

        login_page.open()

        login_page.enter_username('student')

        login_page.enter_password('Password123')

        login_page.click_on_submit()

        assert logged_in_successfully_page.retrieve_url() == 'https://practicetestautomation.com/logged-in-successfully/', 'Correct url should be opened, but is not'

        assert logged_in_successfully_page.retrieve_title_text() == 'Logged In Successfully', 'Logged in message should be displayed, but is not'

        assert logged_in_successfully_page.is_log_out_button_displayed(), 'Log out button should be displayed, but is not'
