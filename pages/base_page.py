import math

from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException


class BasePage:
    def __init__(self, browser, url: str, timeout: int = 10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)
        self.dict_objects = dict()     # save key and link objects

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what: str) -> bool:
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def is_str_in_url_present(self, sub_url: str) -> bool:
        try:
            self.url.index(sub_url)
        except ValueError:
            return False
        return True

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def is_element_present_save_him_in_dict_objects(self, how, what: str, key) -> bool:
        list_element = self.browser.find_elements(how, what)
        if len(list_element) == 0:
            assert False, f"Bad locators for '{key}'. Not found no one object."
        elif len(list_element) > 1:
            assert False, f"Bad locators for '{key}'. Find more one object."
        else:
            self.dict_objects[key] = list_element[0]
            return True

    def click_element(self, key) -> bool:
        try:
            self.dict_objects[key].click()
            return True
        except TypeError:
            print(f"Bad locators for '{key}'.This objects or not clicked or not exist in this moment.")

