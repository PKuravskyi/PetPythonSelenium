from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from pages.base_page import BasePage


class LoggedInSuccessfullyPage(BasePage):
    __url = 'https://practicetestautomation.com/logged-in-successfully/'
    __title_text = (By.CLASS_NAME, 'post-title')
    __log_out_button = (By.LINK_TEXT, 'Log out')

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def retrieve_title_text(self) -> str:
        return super()._get_text(self.__title_text)

    def is_log_out_button_displayed(self) -> bool:
        return super()._is_displayed(self.__log_out_button)
