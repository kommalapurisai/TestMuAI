"""
File        : wait_utils.py
Author      : Sai Krishna
Description : Explicit wait utility methods for Selenium automation.
"""

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from config.config import Config
from utils.logger import Logger


logger = Logger.get_logger()


class WaitUtils:
    """
    Utility class providing reusable explicit wait methods.
    """

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, Config.EXPLICIT_WAIT)

    def wait_for_visibility(self, locator):
        """Wait until an element is visible."""
        try:
            logger.info(f"Waiting for visibility of element: {locator}")
            return self.wait.until(
                EC.visibility_of_element_located(locator)
            )
        except TimeoutException:
            logger.error(f"Element not visible: {locator}")
            raise

    def wait_for_clickable(self, locator):
        """Wait until an element is clickable."""
        try:
            logger.info(f"Waiting for element to be clickable: {locator}")
            return self.wait.until(
                EC.element_to_be_clickable(locator)
            )
        except TimeoutException:
            logger.error(f"Element not clickable: {locator}")
            raise

    def wait_for_presence(self, locator):
        """Wait until an element is present in the DOM."""
        try:
            logger.info(f"Waiting for presence of element: {locator}")
            return self.wait.until(
                EC.presence_of_element_located(locator)
            )
        except TimeoutException:
            logger.error(f"Element not present: {locator}")
            raise

    def wait_for_invisibility(self, locator):
        """Wait until an element disappears."""
        try:
            logger.info(f"Waiting for invisibility of element: {locator}")
            return self.wait.until(
                EC.invisibility_of_element_located(locator)
            )
        except TimeoutException:
            logger.error(f"Element is still visible: {locator}")
            raise

    def wait_for_url_contains(self, partial_url):
        """Wait until the URL contains the expected text."""
        try:
            logger.info(f"Waiting for URL to contain: {partial_url}")
            return self.wait.until(
                EC.url_contains(partial_url)
            )
        except TimeoutException:
            logger.error(f"URL does not contain: {partial_url}")
            raise

    def wait_for_title_contains(self, title):
        """Wait until the page title contains the expected text."""
        try:
            logger.info(f"Waiting for title to contain: {title}")
            return self.wait.until(
                EC.title_contains(title)
            )
        except TimeoutException:
            logger.error(f"Title does not contain: {title}")
            raise

    def wait_for_text(self, locator, text):
        """Wait until specific text appears in an element."""
        try:
            logger.info(f"Waiting for text '{text}' in element: {locator}")
            return self.wait.until(
                EC.text_to_be_present_in_element(locator, text)
            )
        except TimeoutException:
            logger.error(f"Text '{text}' not found in element: {locator}")
            raise

    def wait_for_alert(self):
        """Wait until an alert is present."""
        try:
            logger.info("Waiting for alert.")
            return self.wait.until(
                EC.alert_is_present()
            )
        except TimeoutException:
            logger.error("Alert not found.")
            raise