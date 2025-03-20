import pytest

from pages.exceptions_page import ExceptionsPage


class TestExceptionsScenarios:

    @pytest.mark.exceptions
    def test_no_such_element_exception(self, driver):
        exceptions_page = ExceptionsPage(driver)

        exceptions_page.open()

        exceptions_page.click_on_add()

        assert exceptions_page.is_row2_displayed(), 'Row 2 input should be displayed, but it\'s not'

    @pytest.mark.exceptions
    def test_element_not_interactable_exception(self, driver):
        exceptions_page = ExceptionsPage(driver)

        exceptions_page.open()

        exceptions_page.click_on_add()

        exceptions_page.enter_row2_value('Omelette')

        exceptions_page.click_on_save_for_row2()

        assert exceptions_page.retrieve_confirmation_text() == 'Row 2 was saved', 'Row 2 should be saved, but was not'

    @pytest.mark.exceptions
    def test_invalid_element_state_exception(self, driver):
        exceptions_page = ExceptionsPage(driver)

        exceptions_page.open()

        exceptions_page.click_on_edit_for_row1()

        exceptions_page.enter_row1_value('Sushi')

        exceptions_page.click_on_save_for_row1()

        assert exceptions_page.retrieve_row1_value() == 'Sushi', 'Row 1 value should have changed, but did not'

    @pytest.mark.exceptions
    def test_stale_element_reference_exception(self, driver):
        exceptions_page = ExceptionsPage(driver)

        exceptions_page.open()

        exceptions_page.click_on_add()

        assert not exceptions_page.is_instructions_label_visible(), 'Instructions should not be located on page, but is'

    @pytest.mark.exceptions
    def test_timeout_exception(self, driver):
        exceptions_page = ExceptionsPage(driver)

        exceptions_page.open()

        exceptions_page.click_on_add()

        assert exceptions_page.is_row2_displayed(), 'Row 2 should be visible, but is not'
