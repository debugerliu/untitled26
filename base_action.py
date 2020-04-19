from selenium.webdriver.support.wait import WebDriverWait


class BaseAction:

    def __init__(self, driver):
        self.driver = driver

    def click(self, loc):
        self.find_element(loc).click()

    def input_text(self, loc, text):
        self.find_element(loc).send_keys(text)

    def find_element(self, ele):
        return WebDriverWait(self.driver, 10, 0.5).until(lambda x: x.find_element(ele[0], ele[1]))



