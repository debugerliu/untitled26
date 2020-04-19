from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://www.baidu.com')
print('你看到这个就说明打印成功了')
driver.quit()
