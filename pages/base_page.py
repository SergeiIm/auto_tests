import math
from time import sleep
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from .locators import BasePageLocators


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
            assert False, f"Not find element by how '{how}' and what '{what}' on this page."
        return True

    def is_not_element_present(self, how, what, timeout=4) -> bool:
        try:
            WebDriverWait(self.browser, timeout).until(ec.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, (TimeoutException,)). \
                until_not(ec.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def is_str_in_url_present(self, sub_url: str) -> bool:
        try:
            self.url.index(sub_url)
        except ValueError:
            assert False, f"Sub_url '{sub_url}' not in page '{self.browser.current_url}'."
        return True

    def solve_quiz_and_get_code(self) -> bool:
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f">>> Message: Your code: {alert_text}.")
            alert.accept()
        except NoAlertPresentException:
            print(f"No second alert presented in this page.")
            return False
        return True

    def is_element_present_save_him_in_dict_objects(self, how, what: str, key) -> bool:
        list_element = self.browser.find_elements(how, what)
        if len(list_element) == 0:
            assert False, f"Not found no one object by key = '{key}'."
        elif len(list_element) > 1:
            assert False, f"Find more one object by key = '{key}'."
        else:
            self.dict_objects[key] = list_element[0]
        return True

    def click_element(self, key) -> bool:
        try:
            self.dict_objects[key].click()
        except TypeError:
            assert False, f"Object key '{key}' or not clicked or not exist in this moment."
        return True

    def go_to_login_page(self):
        login_link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        login_link.click()
        # alert = self.browser.switch_to.alert
        # alert.accept()

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"
