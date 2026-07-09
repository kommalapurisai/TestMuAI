"""
File        : playground_page.py
Author      : Sai Krishna
Description : Selenium Playground Page Object.
"""

from selenium.webdriver.common.by import By

from config.config import Config
from pages.base_page import BasePage


class PlaygroundPage(BasePage):

    # ============================
    # Locators
    # ============================

    SIMPLE_FORM_DEMO = (
        By.XPATH,
        "//a[text()='Simple Form Demo']"
    )

    ENTER_MESSAGE = (
        By.ID,
        "user-message"
    )


    GET_CHECKED_VALUE = (
        By.XPATH,
        "//button[@id='showInput']"
    )

    DISPLAYED_MESSAGE = (
        By.ID,
        "message"
    )


    DRAG_DROP_SLIDER = (
        By.XPATH,
        "//a[text()='Drag & Drop Sliders']"
    )

    # ============================

    def __init__(self, driver):
        super().__init__(driver)

    # ============================

    def open_application(self):

        self.driver.get(Config.BASE_URL)

    def click_simple_form_demo(self):

        self.click(self.SIMPLE_FORM_DEMO)

    def validate_simple_form_url(self):

        return self.verify_url_contains("simple-form-demo")

    def enter_message(self, message):

        self.enter_text(self.ENTER_MESSAGE, message)

    def click_get_checked_value(self):
        """
        Click 'Get Checked Value' button.
        """

        button = self.wait.wait_for_clickable(self.GET_CHECKED_VALUE)

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            button
        )

        try:
            button.click()
        except Exception:
            self.driver.execute_script("arguments[0].click();", button)

    def get_displayed_message(self):

        return self.get_text(self.DISPLAYED_MESSAGE)

    def wait_until_page_loaded(self):
        pass

    def click_drag_drop_slider(self):
        """
        Navigate to Drag & Drop Sliders page.
        """

        self.click(self.DRAG_DROP_SLIDER)

        self.verify_url_contains("drag-drop-range-sliders")