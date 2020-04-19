from time import sleep

from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://mubu.com/login/password')
driver.find_element_by_xpath('//*[@id="main-form"]/div[1]/input').send_keys(15035757274)
driver.find_element_by_xpath('//*[@id="main-form"]/div[2]/input').send_keys(123456)
driver.find_element_by_xpath('//*[@id="submit"]').click()
sleep(1)
driver.find_element_by_xpath('//*[@id="nav"]/div/div[1]').click()
sleep(1)
driver.find_element_by_xpath('//*[@id="add-document"]').click()
print('你看到这个就说明打印成功了')
sleep(3)
driver.quit()
