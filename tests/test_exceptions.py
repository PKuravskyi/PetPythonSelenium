import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestExceptionsScenarios:

    @pytest.mark.exceptions
    def test_no_such_element_exception(self, driver):
        driver.implicitly_wait(0)

        driver.get('https://practicetestautomation.com/practice-test-exceptions/')

        driver.find_element(By.ID, 'add_btn').click()

        wait = WebDriverWait(driver, 10)
        row2_input = wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, '#row2 input')))

        assert row2_input.is_displayed(), 'Row 2 input should be displayed, but it\'s not'

    @pytest.mark.exceptions
    def test_element_not_interactable_exception(self, driver):
        driver.implicitly_wait(0)

        driver.get('https://practicetestautomation.com/practice-test-exceptions/')

        driver.find_element(By.ID, 'add_btn').click()

        wait = WebDriverWait(driver, 10)
        row2_input = wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, '#row2 input')))

        row2_input.send_keys('Omelette')
        driver.find_element(By.CSS_SELECTOR, '#row2 #save_btn').click()

        assert driver.find_element(By.ID,
                                   'confirmation').text == 'Row 2 was saved', 'Row 2 should be saved, but was not'

    @pytest.mark.exceptions
    def test_invalid_element_state_exception(self, driver):
        driver.implicitly_wait(0)

        driver.get('https://practicetestautomation.com/practice-test-exceptions/')

        driver.find_element(By.CSS_SELECTOR, '#row1 #edit_btn').click()

        row1_input = driver.find_element(By.CSS_SELECTOR, '#row1 input')
        row1_input.clear()
        row1_input.send_keys('Sushi')

        driver.find_element(By.CSS_SELECTOR, '#row1 #save_btn').click()

        assert row1_input.get_attribute('value') == 'Sushi', 'Row 1 value should have changed, but did not'
