from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.get("https://www.testmuai.com/selenium-playground/input-form-demo/")
driver.maximize_window()
driver.find_element(By.XPATH,"(//button[@type='submit'])[2]").click()

name = driver.find_element(By.ID, "name")

validation_msg = driver.execute_script(
    "return arguments[0].validationMessage;",
    name
)

print(validation_msg)

# print(driver.title)
# print(driver.current_url)
#
# slider = driver.find_element(By.CSS_SELECTOR, "#slider3 input")
# slider_value = slider.get_attribute("value")
# print(slider_value)
#
#
#
# from selenium.webdriver.common.by import By
# from selenium.webdriver import ActionChains
#
# # Locate the 3rd slider
# slider = driver.find_element(By.XPATH, "(//input[@type='range'])[3]")
#
# # Get slider dimensions
# slider_width = slider.size["width"]
#
# # Current and target values
# current_value = int(slider.get_attribute("value"))   # 15
# target_value = 95
#
# # Calculate pixel offset
# offset = int(((target_value - current_value) / (100 - 5)) * slider_width)
#
# # Move the slider
# ActionChains(driver) \
#     .click_and_hold(slider) \
#     .move_by_offset(offset, 0) \
#     .release() \
#     .perform()
#
# # Verify
# print("Slider Value:", slider.get_attribute("value"))
#
# output = driver.find_element(By.ID, "rangeSuccess")
# print("Displayed Value:", output.text)
#
# time.sleep(5)

#
# driver.execute_script("""
# arguments[0].value = 95;
# arguments[0].dispatchEvent(new Event('input', { bubbles: true }));
# arguments[0].dispatchEvent(new Event('change', { bubbles: true }));
# """, slider)

from selenium.webdriver import ActionChains
#
# slider = driver.find_element(By.CSS_SELECTOR, "#slider3 input")
#
# ActionChains(driver)\
#     .click_and_hold(slider)\
#     .move_by_offset(220, 0)\
#     .release()\
#     .perform()
#
# print(driver.find_element(By.ID, "rangeSuccess").text)
# time.sleep(2)
#
# # print(slider.get_attribute("value"))
# # time.sleep(5)
# # ele=driver.find_element(By.ID,"rangeSuccess")
# # print(ele.text)



# ActionChains(driver).move_by_offset(946, 349).pause(2).click().perform()
# exp_val = '95'
# obtained_val = driver.find_element(By.ID, "rangeSuccess").text
# print(obtained_val)
#
# time.sleep(3)

