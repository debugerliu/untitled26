from time import sleep
from base_action import BaseAction
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# driver = webdriver.Chrome()
# driver.implicitly_wait(3)
# driver.get('https://mubu.com/login/password')
# driver.find_element_by_xpath('//*[@id="main-form"]/div[1]/input').send_keys(15035757274)
# driver.find_element_by_xpath('//*[@id="main-form"]/div[2]/input').send_keys(123456)
# driver.find_element_by_xpath('//*[@id="submit"]').click()
# driver.find_element_by_xpath('//*[@id="nav"]/div/div[1]').click()
# driver.find_element_by_xpath('//*[@id="add-document"]').click()
# print('你看到这个就说明打印成功了')
# driver.quit()


class NewDoc(BaseAction):

    name = By.XPATH, '//*[@id="main-form"]/div[1]/input',
    pwd = By.XPATH, '//*[@id="main-form"]/div[2]/input',
    submit = By.XPATH, '//*[@id="submit"]',
    new_form = By.XPATH, '//*[@id="nav"]/div/div[1]',
    new_doc = By.XPATH, '//*[@id="add-document"]'

    def __init__(self, driver):
        BaseAction.__init__(self, driver)

    def send_name(self, text):
        self.input_text(self.name, text)

    def send_pwd(self, text):
        self.input_text(self.pwd, text)

    def click_sub(self):
        self.click(self.submit)

    def click_new_form(self):
        self.click(self.new_form)

    def click_new_doc(self):
        self.click(self.new_doc)


class TestCase(object):

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.tt = NewDoc(self.driver)

    def newtest(self):
        self.driver.get('https://mubu.com/login/password')
        self.tt.send_name(15035757274)
        self.tt.send_pwd(123456)
        self.tt.click_sub()
        self.tt.click_new_form()
        sleep(5)
        self.tt.click_new_doc()
        print('成功了')
        self.driver.quit()


if __name__ == '__main__':
    t = TestCase()
    t.newtest()



