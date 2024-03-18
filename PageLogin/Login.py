import sys
import time

sys.path.append(r"C:\Users\ashwi\PycharmProjects\Testing Project\BaseClass")


import Base
from selenium.webdriver.common.by import By
# User Name
txtuser = Base.driver.find_element(By.NAME, "email")
txtuser.send_keys("kashwinchn@gmail.com")

# Password
txtpass = Base.driver.find_element(By.NAME, "pass")
txtpass.send_keys("98764321")

# login
butnlogin = Base.driver.find_element(By.NAME, "login")
butnlogin.click()

time.sleep(8)

# Base.driver.back()
# time.sleep(3)

