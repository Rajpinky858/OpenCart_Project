import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ActionChains

serv_obj = Service("C:\Automation_projects\Drivers\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://demo.opencart.com/index.php?route=account/login&language=en-gb")
#driver.maximize_window()
#driver.find_element(By.XPATH, '//*[@id="top"]/div[2]/div[2]/ul/li[2]/div/a/i[2]').click()
#time.sleep(2)
#driver.find_element(By.XPATH, '//*[@id="top"]/div[2]/div[2]/ul/li[2]/div/a/i[2]').click()
#time.sleep(2)
#driver.find_element(By.XPATH, '//*[@id="top"]/div[2]/div[2]/ul/li[2]/div/ul/li[2]/a').click()

driver.find_element(By.XPATH, '//*[@id="input-email"]').send_keys("abc123456623@gmail.com")
driver.find_element(By.XPATH, '//*[@id="input-password"]').send_keys("123456789")
driver.find_element(By.XPATH, '//*[@id="form-login"]/button').click()
time.sleep(2)
