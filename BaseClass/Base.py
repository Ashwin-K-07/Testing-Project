from selenium import webdriver

# Browser launch
driver=webdriver.Chrome()

# Url Launch
driver.get("https://www.facebook.com/")
driver.maximize_window()

# Get Title
title=driver.title
print(title)

# Get Current Url
url=driver.current_url
print(url)


