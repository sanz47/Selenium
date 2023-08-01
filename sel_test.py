from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
# create webdriver object
driver = webdriver.Chrome()
driver.get("https://google.com")
search=driver.find_element(By.ID,"APjFqb")
search.send_keys("Adidas")
search.send_keys(Keys.RETURN)
time.sleep(20)