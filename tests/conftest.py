import pytest

from utils.browser_factory import BrowserFactory


@pytest.fixture(scope="function")
def driver():

    driver = BrowserFactory.get_driver()

    yield driver

    BrowserFactory.quit_driver(driver)