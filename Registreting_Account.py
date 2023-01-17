import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ActionChains

serv_obj = Service("C:\Automation_projects\Drivers\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://demo.opencart.com/")
driver.maximize_window()
driver.find_element(By.XPATH, '//*[@id="top"]/div[2]/div[2]/ul/li[2]/div/a/i[2]').click()
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="top"]/div[2]/div[2]/ul/li[2]/div/ul/li[1]/a').click()
time.sleep(2)

page_title = driver.find_element(By.XPATH, '//*[@id="content"]/h1').text
if page_title == "Register Account":
    print ("Register page open successfully....")
else:
    print('This is not register page')

firstname = driver.find_element(By.NAME, 'firstname')
lastname = driver.find_element(By.XPATH, '//*[@id="input-lastname"]')
email = driver.find_element(By.ID, 'input-email')
paswd = driver.find_element(By.NAME, 'password')
privacypolicy = driver.find_element(By.XPATH, '//*[@id="form-register"]/div/div/div/input')
submit = driver.find_element(By.XPATH, '//*[@id="form-register"]/div/div/button')

# 1. Registering an Account providing all mandatary details.

firstname.send_keys("Abc")
lastname.send_keys("Xyz")
email.send_keys("abcd12866565@gmail.com")
paswd.send_keys("123456789")
time.sleep(3)
act = ActionChains(driver)
#act.move_to_element(privacypolicy).click().perform()
privacypolicy.click()
submit.click()
time.sleep(5)

