from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from pages.base_page import BasePage


class ExceptionsPage(BasePage):
    __url = 'https://practicetestautomation.com/practice-test-exceptions/'
    __add_button = (By.ID, 'add_btn')
    __row1_edit_button = (By.CSS_SELECTOR, '#row1 #edit_btn')
    __row1_input = (By.CSS_SELECTOR, '#row1 input')
    __row1_save_button = (By.CSS_SELECTOR, '#row1 #save_btn')
    __row2_input = (By.CSS_SELECTOR, '#row2 input')
    __row2_save_button = (By.CSS_SELECTOR, '#row2 #save_btn')
    __confirmation_label = (By.ID, 'confirmation')
    __instruction_label = (By.ID, 'instructions')

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open(self):
        super()._navigate_to(self.__url)

    def click_on_add(self):
        super()._click(self.__add_button)

    def is_row2_displayed(self) -> bool:
        super()._wait_until_element_is_visible(self.__row2_input)
        return super()._is_displayed(self.__row2_input)

    def enter_row2_value(self, value, time: int = 10):
        super()._type(self.__row2_input, value, time)

    def click_on_save_for_row2(self):
        super()._click(self.__row2_save_button)

    def retrieve_confirmation_text(self) -> str:
        return super()._get_text(self.__confirmation_label)

    def click_on_edit_for_row1(self):
        super()._click(self.__row1_edit_button)

    def enter_row1_value(self, value):
        super()._type(self.__row1_input, value)

    def click_on_save_for_row1(self):
        super()._click(self.__row1_save_button)

    def retrieve_row1_value(self) -> str:
        return super()._get_attribute(self.__row1_input, 'value')

    def is_instructions_label_visible(self) -> bool:
        super()._wait_until_element_is_invisible(self.__instruction_label)
        return super()._is_displayed(self.__instruction_label)
