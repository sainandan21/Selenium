from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service()
driver = webdriver.Chrome(service=service_obj)
driver.get("https://www.techlistic.com/p/selenium-practice-form.html")
driver.find_element(By.NAME,"firstname").send_keys("Abc")
driver.find_element(By.ID,"continents").send_keys("North America")
driver.find_element(By.ID,"profession-0").click()