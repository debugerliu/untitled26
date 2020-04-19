from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class BaseAction:

    def __init__(self, driver):
        self.driver = driver

    def click(self, loc):
        self.find_element(loc).click()

    def input_text(self, loc, text):
        self.find_element(loc).send_keys(text)

    def find_element(self, ele):
        # return WebDriverWait(self.driver, 10, 0.3).until(lambda x: x.find_element(ele[0], ele[1]))
        # return WebDriverWait(self.driver, 10, 0.3).until(lambda x: x.find_element(ele[0], ele[1]))
        return WebDriverWait(self.driver, 10, 0.1).until(EC.visibility_of_element_located((ele[0], ele[1])))
