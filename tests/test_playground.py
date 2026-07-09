"""
File        : test_playground.py
Author      : Sai Krishna
Description : Scenario 1 Automation.
"""

from pages.playground_page import PlaygroundPage
import time


def test_simple_form_navigation(driver):

    message = "Welcome to TestMu AI"

    playground = PlaygroundPage(driver)

    playground.open_application()

    playground.click_simple_form_demo()

    playground.validate_simple_form_url()

    playground.wait_until_page_loaded()

    playground.enter_message(message)
    playground.click_get_checked_value()

    playground.click_get_checked_value()

    actual_message = playground.get_displayed_message()

    assert actual_message == message