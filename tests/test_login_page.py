import time

import pytest
from selenium.webdriver.common.by import By


class TestPositiveScenarios:

    @pytest.mark.login
    @pytest.mark.positive
    def test_positive_login(self, driver):
        driver.get('https://practicetestautomation.com/practice-test-login/')

        user_locator = driver.find_element(By.ID, 'username')
        user_locator.send_keys("student")

        password_locator = driver.find_element(By.NAME, 'password')
        password_locator.send_keys("Password123")

        submit_locator = driver.find_element(By.XPATH, '//button[@class=("btn")]')
        submit_locator.click()
        time.sleep(1)

        actual_url = driver.current_url
        assert actual_url == 'https://practicetestautomation.com/logged-in-successfully/'

        actual_text = driver.find_element(By.CLASS_NAME, 'post-title').text
        assert actual_text == 'Logged In Successfully'

        log_out_button_locator = driver.find_element(By.LINK_TEXT, 'Log out')
        assert log_out_button_locator.is_displayed()
