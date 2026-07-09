"""
File        : base_page.py
Author      : Sai Krishna
Description : Base Page containing reusable Selenium methods.
"""

from utils.wait_utils import WaitUtils
from utils.logger import Logger


logger = Logger.get_logger()


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WaitUtils(driver)

    def click(self, locator):
        logger.info(f"Clicking element : {locator}")
        self.wait.wait_for_clickable(locator).click()

    def enter_text(self, locator, text):
        logger.info(f"Entering text : {text}")

        element = self.wait.wait_for_visibility(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        text = self.wait.wait_for_visibility(locator).text

        logger.info(f"Captured Text : {text}")

        return text

    def get_current_url(self):
        return self.driver.current_url

    def verify_url_contains(self, expected_text):

        current_url = self.get_current_url()

        logger.info(f"Current URL : {current_url}")

        assert expected_text in current_url, \
            f"Expected '{expected_text}' in URL but got '{current_url}'"

        logger.info("URL validation successful.")

        return current_url