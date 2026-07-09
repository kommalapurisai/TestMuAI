"""
File        : input_form_page.py
Author      : Sai Krishna
Description : Page Object for Input Form Submit.
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from pages.base_page import BasePage


class InputFormPage(BasePage):

    # Navigation
    INPUT_FORM_SUBMIT = (
        By.XPATH,
        "//a[text()='Input Form Submit']"
    )

    # Form Fields
    NAME = (By.ID, "name")

    EMAIL = (By.ID, "inputEmail4")

    PASSWORD = (By.NAME, "password")

    COMPANY = (By.ID, "company")

    WEBSITE = (By.ID, "websitename")

    COUNTRY = (By.NAME, "country")

    CITY = (By.NAME, "city")

    ADDRESS1 = (By.ID, "inputAddress1")

    ADDRESS2 = (By.ID, "inputAddress2")

    STATE = (By.ID, "inputState")

    ZIPCODE = (By.ID, "inputZip")

    SUBMIT = (
        By.XPATH,
        "(//button[@type='submit'])[2]"
    )

    SUCCESS_MESSAGE = (
        By.XPATH,
        "//p[text()='Thanks for contacting us, we will get back to you shortly.']"
    )

    def __init__(self, driver):
        super().__init__(driver)

    # ------------------------------------------

    def open_input_form(self):

        self.click(self.INPUT_FORM_SUBMIT)

    # ------------------------------------------

    def click_submit(self):

        self.click(self.SUBMIT)

    # ------------------------------------------

    def get_validation_message(self):

        element = self.wait.wait_for_visibility(self.NAME)

        return element.get_attribute("validationMessage")

    # ------------------------------------------

    def fill_form(self):

        self.enter_text(self.NAME, "saikrishna")

        self.enter_text(self.EMAIL, "sai@gmail.com")

        self.enter_text(self.PASSWORD, "7799456")

        self.enter_text(self.COMPANY, "HCL")

        self.enter_text(self.WEBSITE, "www.saiHCL.com")

        Select(
            self.wait.wait_for_visibility(self.COUNTRY)
        ).select_by_visible_text("United States")

        self.enter_text(self.CITY, "Tirupathi")

        self.enter_text(self.ADDRESS1, "2-15")

        self.enter_text(self.ADDRESS2, "Tirupathi,2-156/5A")

        self.enter_text(self.STATE, "Andhra Pradesh")

        self.enter_text(self.ZIPCODE, "517501")

    # ------------------------------------------

    def click_submit_after_form(self):

        self.click(self.SUBMIT)

    # ------------------------------------------

    def get_success_message(self):

        return self.get_text(self.SUCCESS_MESSAGE)