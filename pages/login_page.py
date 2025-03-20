from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from pages.base_page import BasePage


class LoginPage(BasePage):
    __url = 'https://practicetestautomation.com/practice-test-login/'
    __username_field = (By.ID, 'username')
    __password_field = (By.NAME, 'password')
    __submit_button = (By.XPATH, '//button[@class=("btn")]')
    __error_locator = (By.ID, 'error')

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open(self):
        super()._navigate_to(self.__url)

    def enter_username(self, username: str):
        super()._type(self.__username_field, username)

    def enter_password(self, password: str):
        super()._type(self.__password_field, password)

    def click_on_submit(self):
        super()._click(self.__submit_button)

    def is_error_displayed(self, time: int = 10) -> bool:
        super()._wait_until_element_is_visible(self.__error_locator, 3)
        return super()._is_displayed(self.__error_locator)

    def retrieve_error_text(self) -> str:
        return super()._find(self.__error_locator).text
