from time import sleep

from .base_page import BasePage
from .locators import LoginPageLocators
from selenium.common.exceptions import NoSuchElementException


class LoginPage(BasePage):

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.is_str_in_url_present(*LoginPageLocators.SUB_URL), "Sub url isn't include in login page url."

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented."

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented."

    def register_new_user(self, email, password):
        try:
            input_email = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_INPUT_USER_EMAIL)
        except NoSuchElementException:
            assert False, "Locator 'REGISTER_FORM_INPUT_USER_EMAIL' not find on page."
        input_email.send_keys(email)
        try:
            input_pass_one = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_INPUT_PASSWORD_ONE)
        except NoSuchElementException:
            assert False, "Locator 'REGISTER_FORM_INPUT_PASSWORD_ONE' not find on page."
        input_pass_one.send_keys(password)
        try:
            input_pass_two = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_INPUT_PASSWORD_TWO)
        except NoSuchElementException:
            assert False, "Locator 'REGISTER_FORM_INPUT_PASSWORD_TWO' not fond on page."
        input_pass_two.send_keys(password)
        self.click_element(*LoginPageLocators.REGISTER_FORM_BTN_REGISTRATION)
        self.should_be_authorized_user()
