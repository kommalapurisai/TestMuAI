"""
File        : browser_factory.py
Author      : Sai Krishna
Description : Browser Factory for Local and TestMu AI Remote Execution.
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.firefox.service import Service as FirefoxService

from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.ie.options import Options as IEOptions

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import (
    ChromeType,
    EdgeChromiumDriverManager,
)

from config.config import Config
from utils.logger import Logger


logger = Logger.get_logger()


class BrowserFactory:
    """
    Creates WebDriver instances for Local and Remote execution.
    """

    @staticmethod
    def get_driver(
            browser_name: str = "chrome",
            browser_version: str = "",
            platform_name: str = "",
            test_name: str = "Automation Test"
    ):

        execution_mode = Config.EXECUTION_MODE.lower()
        browser = browser_name.lower()

        logger.info(f"Execution Mode : {execution_mode}")
        logger.info(f"Browser        : {browser}")

        if execution_mode == "local":
            return BrowserFactory._create_local_driver(browser)

        elif execution_mode == "remote":
            return BrowserFactory._create_remote_driver(
                browser_name,
                browser_version,
                platform_name,
                test_name
            )

        else:
            raise ValueError(
                f"Invalid EXECUTION_MODE : {execution_mode}"
            )

    # ======================================================
    # LOCAL DRIVER
    # ======================================================

    @staticmethod
    def _create_local_driver(browser):

        if browser == "chrome":

            options = ChromeOptions()

            driver = webdriver.Chrome(
                service=ChromeService(
                    ChromeDriverManager().install()
                ),
                options=options
            )

        elif browser == "firefox":

            options = FirefoxOptions()

            driver = webdriver.Firefox(
                service=FirefoxService(
                    GeckoDriverManager().install()
                ),
                options=options
            )

        elif browser == "edge":

            options = EdgeOptions()

            driver = webdriver.Edge(
                service=EdgeService(
                    EdgeChromiumDriverManager().install()
                ),
                options=options
            )

        else:

            raise ValueError(
                f"Unsupported local browser : {browser}"
            )

        driver.maximize_window()

        driver.implicitly_wait(Config.IMPLICIT_WAIT)

        driver.set_page_load_timeout(Config.EXPLICIT_WAIT)

        logger.info("Local browser launched successfully.")

        return driver

    # ======================================================
    # REMOTE DRIVER
    # ======================================================

    @staticmethod
    def _create_remote_driver(
            browser_name,
            browser_version,
            platform_name,
            test_name
    ):

        browser = browser_name.lower()

        if browser == "chrome":
            options = ChromeOptions()

        elif browser == "firefox":
            options = FirefoxOptions()

        elif browser == "edge":
            options = EdgeOptions()

        elif browser in ("internet explorer", "ie"):
            options = IEOptions()

        else:
            raise ValueError(
                f"Unsupported browser : {browser_name}"
            )

        options.set_capability(
            "browserName",
            browser_name
        )

        options.set_capability(
            "browserVersion",
            browser_version
        )

        options.set_capability(
            "platformName",
            platform_name
        )

        options.set_capability(
            "testmu:options",
            {
                "username": Config.TESTMU_USERNAME,
                "accessKey": Config.TESTMU_ACCESS_KEY,
                "build": "Python Selenium Assignment",
                "name": test_name,
                "video": True,
                "network": True,
                "console": True,
                "visual": True
            }
        )

        driver = webdriver.Remote(
            command_executor=Config.GRID_URL,
            options=options
        )

        driver.maximize_window()

        driver.implicitly_wait(Config.IMPLICIT_WAIT)

        driver.set_page_load_timeout(Config.EXPLICIT_WAIT)

        logger.info("Remote browser launched successfully.")

        return driver

    # ======================================================
    # CLOSE DRIVER
    # ======================================================

    @staticmethod
    def quit_driver(driver):

        if driver:

            logger.info("Closing browser.")

            driver.quit()