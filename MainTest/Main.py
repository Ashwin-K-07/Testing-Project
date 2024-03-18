import sys
import time

sys.path.append(r"C:\Users\ashwi\PycharmProjects\Testing Project\PageLogin")

import Login
from selenium.webdriver.common.by import By

Login.Base.driver.back()
time.sleep(3)


crtbtn = Login.Base.driver.find_element(By.XPATH, "(// a[@role = 'button'])[2]")
crtbtn.click()
time.sleep(3)


firstname = Login.Base.driver.find_element(By.NAME, "firstname")
firstname.send_keys("Ashwin")


lastname = Login.Base.driver.find_element(By.NAME, "lastname")
lastname.send_keys("K")


phone = Login.Base.driver.find_element(By.NAME, "reg_email__")
phone.send_keys("9876543210")

time.sleep(4)