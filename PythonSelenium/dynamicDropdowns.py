import time
#
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
#
# service_obj = Service()
# driver = webdriver.Chrome(service=service_obj)
# driver.get("https://phptravels.net/")
# driver.find_element(By.XPATH,"//*[@class='select2-selection select2-selection--single']").click()
# driver.find_element(By.XPATH,"//*[@class='select2-search__field']").send_keys("Hyderabad")
# driver.find_element(By.XPATH,"//li[@class='select2-results__option select2-results__option--highlighted']").click()
#
# time.sleep(5)
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service_obj = Service()
driver = webdriver.Chrome(service=service_obj)
driver.get("https://phptravels.net/")

# Wait for the dropdown to be clickable
wait = WebDriverWait(driver, 10)
dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@class='select2-selection select2-selection--single']")))
dropdown.click()

# Enter text into the search field
search_field = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@class='select2-search__field']")))
search_field.send_keys("Hyderabad")

# Wait for the option to be clickable and then select it
option = wait.until(EC.element_to_be_clickable((By.XPATH, "//li[@class='select2-results__option select2-results__option--highlighted']")))
option.click()
time.sleep(10)

