from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://trytestingthis.netlify.app/")
driver.find_element(By.ID,"fname").send_keys("sanz")
driver.find_element(By.ID,"lname").send_keys("aziz")
time.sleep(20)
