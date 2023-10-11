import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service()#Selenium manager-> it will download chromedriver externally.
driver = webdriver.Chrome(service=service_obj)
driver.get("https://phptravels.net/")
driver.find_element(By.ID,"round-trip").click()
time.sleep(10)