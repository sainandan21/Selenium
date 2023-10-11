import webbrowser
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import  time

service_obj = Service()
driver = webdriver.Chrome(service = service_obj)
driver.get("https://rahulshettyacademy.com/practice-project")
driver.find_element(By.NAME,'name').send_keys("Sai Nandan Mamidi")
driver.find_element(By.XPATH,"//input[@name='email']").send_keys("sainandan@gmail.com")
driver.find_element(By.CSS_SELECTOR, "#agreeTerms").click()
driver.find_element(By.XPATH,"//button[@type='submit']").click()
time.sleep(20)
driver.close()