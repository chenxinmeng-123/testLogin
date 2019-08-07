from selenium import webdriver
driver=webdriver.Chrome()
driver.maximize_window()

driver.implicitly_wait(10)

driver.get('http://chat.shopee.com/#/dashboard')
'''
driver.find_element_by_xpath('//*[@id="app"]/div/form/div[3]/div/button').click()
driver.find_element_by_xpath('//*[@id="app"]/div/form/div[3]/div/button').send_keys('123')
'''

driver.find_element_by_xpath('//*[@id="app"]/div/form/div[1]/div/div[1]/input').clear()
driver.implicitly_wait(1)
driver.find_element_by_xpath('//*[@id="app"]/div/form/div[2]/div/div[1]/input').clear()
driver.implicitly_wait(1)
driver.find_element_by_xpath('//*[@id="app"]/div/form/div[1]/div/div[1]/input').click()
driver.find_element_by_xpath('//*[@id="app"]/div/form/div[1]/div/div[1]/input').send_keys(chenxinmeng)
driver.implicitly_wait(1)
driver.find_element_by_xpath('//*[@id="app"]/div/form/div[2]/div/div[1]/input').click()
driver.find_element_by_xpath('//*[@id="app"]/div/form/div[2]/div/div[1]/input').send_keys('123654')
driver.implicitly_wait(1)
driver.find_element_by_xpath('//*[@id="app"]/div/form/div[3]/div/button').click()
