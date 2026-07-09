from pages.playground_page import PlaygroundPage
from pages.slider_page import SliderPage


def test_drag_drop_slider(driver):

    playground = PlaygroundPage(driver)

    slider = SliderPage(driver)

    playground.open_application()

    playground.wait_until_page_loaded()

    playground.click_drag_drop_slider()

    slider.move_slider_to_95()

    actual = slider.get_slider_value()

    assert actual == "95"