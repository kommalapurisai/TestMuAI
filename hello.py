from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.get("https://www.testmuai.com/selenium-playground/")
driver.maximize_window()
get_url=driver.current_url
print(get_url)
driver.find_element(By.XPATH, "//a[text()='Simple Form Demo']").click()
sample_url=driver.current_url
print(sample_url)
if sample_url.endswith("simple-form-demo"):
    print("Yes")
else:
    print("No")

