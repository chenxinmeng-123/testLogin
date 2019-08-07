from selenium import webdriver
driver=webdriver.Chrome()
driver.maximize_window()

driver.implicitly_wait(10)

driver.get('http://chat.shopee.com/#/dashboard')

