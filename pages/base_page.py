from selenium.common import NoSuchElementException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class BasePage:
    def __init__(self, driver: WebDriver):
        self._driver = driver

    def _find(self, locator: tuple[str, str]) -> WebElement:
        return self._driver.find_element(*locator)

    def _type(self, locator: tuple[str, str], text: str, time: int = 10):
        self._wait_until_element_is_visible(locator, time)
        self._find(locator).clear()
        self._find(locator).send_keys(text)

    def _click(self, locator: tuple[str, str]):
        self._find(locator).click()

    def _wait_until_element_is_visible(self, locator: tuple[str, str], time: int = 10):
        wait = WebDriverWait(self._driver, time)
        wait.until(expected_conditions.visibility_of_element_located(locator))

    def _wait_until_element_is_invisible(self, locator: tuple[str, str], time: int = 10):
        wait = WebDriverWait(self._driver, time)
        wait.until(expected_conditions.invisibility_of_element_located(locator))

    def _is_displayed(self, locator: tuple[str, str]) -> bool:
        try:
            return self._find(locator).is_displayed()
        except NoSuchElementException:
            return False

    def _navigate_to(self, url: str):
        self._driver.get(url)

    def _get_text(self, locator: tuple[str, str], time: int = 10) -> str:
        self._wait_until_element_is_visible(locator, time)
        return self._find(locator).text

    def _get_attribute(self, locator: tuple[str, str], attribute, time: int = 10) -> str:
        self._wait_until_element_is_visible(locator, time)
        return self._find(locator).get_attribute(attribute)

    def retrieve_url(self) -> str:
        return self._driver.current_url
