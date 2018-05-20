from selenium.webdriver import Chrome
import time
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--headless")

driver = Chrome(executable_path="chromedriver", chrome_options=options)
driver.get("https://www.facebook.com")

driver.find_element_by_id("email").send_keys("")
driver.find_element_by_id("pass").send_keys("")

driver.find_element_by_id("login_form").submit()
time.sleep(1)
print(driver.find_element_by_class_name("userContent").text)

time.sleep(1)
driver.close()









