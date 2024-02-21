import math

from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException, NoSuchAttributeException, \
    ElementNotInteractableException, TimeoutException

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from .locators import BasePageLocators


class BasePage:
    def __init__(self, browser, url: str, timeout: int = 10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, (TimeoutException, )). \
                until_not(ec.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

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

    def get_element_attribute_text(self, how, what) -> bool:
        try:
            tmp = self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        try:
            return tmp.text
        except NoSuchAttributeException:
            return False

    def click_element(self, how, what: str) -> bool:
        try:
            link = self.browser.find_element(how, what)
        except NoSuchElementException:
            assert False, 'Element not found.'
        try:
            link.click()
        except ElementNotInteractableException:
            assert False, 'Element not clickabling.'
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

    # ------------------------------------------- methods for interface.-------------------------------------------

    def go_to_login_page(self):
        try:
            login_link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        except NoSuchElementException:
            assert False, "Not find locator 'LOGIN_LINK'."
        try:
            login_link.click()
        except NoSuchAttributeException:
            assert False, "Link with locator 'LOGIN_LINK' is not be click."

    def go_to_basket_page(self):
        try:
            basket_link = self.browser.find_element(*BasePageLocators.BASKET_LINK)
        except NoSuchElementException:
            assert False, "Not find locator 'BASKET_LINK'."
        try:
            basket_link.click()
        except NoSuchAttributeException:
            assert False, "Link with locator 'BASKET_LINK' is not be click."

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented."

    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented," \
                                                                     " probably unauthorised user"
