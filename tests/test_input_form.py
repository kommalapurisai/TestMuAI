"""
File        : test_input_form.py
Author      : Sai Krishna
Description : Test Scenario 3.
"""

from pages.playground_page import PlaygroundPage
from pages.input_form_page import InputFormPage


def test_input_form(driver):

    playground = PlaygroundPage(driver)

    form = InputFormPage(driver)

    # Open Application
    playground.open_application()

    # Navigate to Input Form
    form.open_input_form()

    # Click Submit without data
    form.click_submit()

    # Validate browser HTML5 message
    validation_message = form.get_validation_message()

    assert validation_message == "Please fill out this field."

    # Fill form
    form.fill_form()

    # Submit again
    form.click_submit_after_form()

    # Validate success message
    actual = form.get_success_message()

    assert actual == \
        "Thanks for contacting us, we will get back to you shortly."