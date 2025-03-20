import pytest

from pages.login_page import LoginPage


class TestNegativeScenarios:

    @pytest.mark.login
    @pytest.mark.negative
    @pytest.mark.parametrize('username, password, expected_error_message',
                             [('incorrectUser', 'Password123', 'Your username is invalid!'),
                              ('student', 'incorrectPassword', 'Your password is invalid!')])
    def test_negative_login(self, driver, username, password, expected_error_message):
        login_page = LoginPage(driver)

        login_page.open()

        login_page.enter_username(username)

        login_page.enter_password(password)

        login_page.click_on_submit()

        assert login_page.is_error_displayed(), 'Error message should be displayed, but is not'
        assert login_page.retrieve_error_text() == expected_error_message, 'Expected error message is not present'
