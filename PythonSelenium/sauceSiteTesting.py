import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
# products = driver.find_elements(By.XPATH,"//div[@class='inventory_item']/div[2]/div[2]/button[1]")
service_obj = Service()

driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(5)
driver.get("https://www.saucedemo.com/inventory.html")
driver.find_element(By.ID,"user-name").send_keys("standard_user")
driver.find_element(By.ID,"password").send_keys("secret_sauce")
driver.find_element(By.ID,"login-button").click()
select = Select(driver.find_element(By.CLASS_NAME,"product_sort_container"))
select.select_by_value("za")
select_all = driver.find_elements(By.XPATH, "//button[text()='Add to cart']")
for select in select_all:
    select.click()
driver.find_element(By.CLASS_NAME,"shopping_cart_link").click()
time.sleep(2)
driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")
driver.find_element(By.XPATH,"//button[@id='checkout']").click()
driver.find_element(By.ID,"first-name").send_keys("Sai Nandan ")
driver.find_element(By.ID,"last-name").send_keys("Mamidi")
driver.find_element(By.ID,"postal-code").send_keys("30028")
driver.find_element(By.XPATH,"//input[@id='continue']").click()
driver.find_element(By.XPATH,"//button[@id='finish']").click()
time.sleep(1200000)