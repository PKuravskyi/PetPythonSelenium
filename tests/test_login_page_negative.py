import time

import pytest
from selenium.webdriver.common.by import By


class TestNegativeScenarios:

    @pytest.mark.login
    @pytest.mark.negative
    @pytest.mark.parametrize('username, password, expected_error_message',
                             [('incorrectUser', 'Password123', 'Your username is invalid!'),
                              ('student', 'incorrectPassword', 'Your password is invalid!')])
    def test_negative_login(self, driver, username, password, expected_error_message):
        driver.get('https://practicetestautomation.com/practice-test-login/')

        user_locator = driver.find_element(By.ID, 'username')
        user_locator.send_keys(username)

        password_locator = driver.find_element(By.NAME, 'password')
        password_locator.send_keys(password)

        driver.find_element(By.XPATH, '//button[@class=("btn")]').click()

        error_locator = driver.find_element(By.ID, 'error')

        assert error_locator.is_displayed(), 'Error message is not present'
        assert error_locator.text == expected_error_message, 'Expected error message is not present'
