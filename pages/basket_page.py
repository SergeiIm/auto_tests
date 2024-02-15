from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def add_product_on_basket(self):
        self.is_element_present_save_him_in_dict_objects(*BasketPageLocators.NAME_PRODUCT, key='name')
        self.dict_objects['name'] = self.dict_objects['name'].text
        self.is_element_present_save_him_in_dict_objects(*BasketPageLocators.BASKET_MINI, key='basket-mini')
        self.dict_objects['basket-mini'] = self.dict_objects['basket-mini'].text
