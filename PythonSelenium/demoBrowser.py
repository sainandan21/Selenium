from selenium import webdriver
from selenium.webdriver.chrome.service import Service
service_obj = Service()#Selenium manager-> it will download chromedriver externally.
driver = webdriver.Chrome(service=service_obj)
driver.get("https://www.youtube.com/")