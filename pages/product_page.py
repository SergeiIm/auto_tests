from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def check_and_add_price_name_product_and_basket_default(self):
        self.is_element_present_save_him_in_dict_objects(*ProductPageLocators.NAME_PRODUCT, key='name')
        self.dict_objects['name'] = self.dict_objects['name'].text
        self.is_element_present_save_him_in_dict_objects(*ProductPageLocators.PRICE_PRODUCT, key="price")
        self.dict_objects['price'] = self.dict_objects['price'].text
        self.is_element_present_save_him_in_dict_objects(*ProductPageLocators.BASKET_MINI, key='basket-mini')
        self.dict_objects['basket-mini'] = self.dict_objects['basket-mini'].text

    def click_add_to_basket_btn(self):
        self.is_element_present_save_him_in_dict_objects(*ProductPageLocators.BTN_ADD_TO_BASKET, key='add_to_basket')
        self.click_element(key='add_to_basket')

    def pass_the_check_stepik(self):
        self.solve_quiz_and_get_code()

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_disappear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is not disappear, but should be"
