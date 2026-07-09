"""
File        : slider_page.py
Author      : Sai Krishna
Description : Page Object for Drag & Drop Slider.
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

from pages.base_page import BasePage


class SliderPage(BasePage):

    # Slider with Default Value 15
    SLIDER_15 = (
        By.CSS_SELECTOR,
        "#slider3 input"
    )

    # Output Value
    RANGE_VALUE = (
        By.ID,
        "rangeSuccess"
    )

    def __init__(self, driver):
        super().__init__(driver)

    def move_slider_to_95(self):

        slider = self.wait.wait_for_visibility(self.SLIDER_15)

        #
        # Use JavaScript because HTML5 sliders are much more stable
        #

        self.driver.execute_script("""
        arguments[0].value = 95;
        arguments[0].dispatchEvent(new Event('input', { bubbles: true }));
        arguments[0].dispatchEvent(new Event('change', { bubbles: true }));
        """, slider)

    def get_slider_value(self):

        return self.get_text(self.RANGE_VALUE)