from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be."

    def should_be_disappeared_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            'Success message is disappeared, but should not be.'

    def click_btn_add_to_basket(self):
        assert self.click_element(*ProductPageLocators.BTN_ADD_TO_BASKET), \
            "Not find object 'BTN_ADD_TO_BASKET' on page or not interactable."

    def check_added_product_on_basket(self):
        message = self.get_element_attribute_text(*ProductPageLocators.SUCCESS_MESSAGE)
        if type(message) != str:
            assert False, "Locator 'CHECK_MESSAGE' not find or not have attribute 'text'."
        if ProductPageLocators.GOOD_CHECK_MESSAGE_TEXT not in message:
            assert False, "Not find text locator 'GOOD_CHECK_MESSAGE_TEXT' on locator 'CHECK_MESSAGE' on the page."

    def check_name_of_product_on_message_add_on_basket(self):
        message_name = self.get_element_attribute_text(*ProductPageLocators.NAME_PRODUCT_ON_MESSAGE)
        name = self.get_element_attribute_text(*ProductPageLocators.NAME_PRODUCT)
        if not message_name:
            if not name:
                assert False, "Locators 'NAME_PRODUCT_ON_MESSAGE' and 'NAME_PRODUCT' not correct or not have " \
                              "attribute 'text'."
            assert False, "Locator 'NAME_PRODUCT_ON_MESSAGE' not correct or not have attribute 'text'."
        elif not name:
            assert False, "Locator 'NAME_PRODUCT' not correct or not have attribute 'text'."
        else:
            if message_name == name:
                return True
            else:
                assert False, "Text NAME_PRODUCT != text NAME_PRODUCT_ON_MESSAGE."

    def check_price_of_product_on_message_add_on_basket(self):
        message_price = self.get_element_attribute_text(*ProductPageLocators.PRICE_PRODUCT_ON_MESSAGE)
        price = self.get_element_attribute_text(*ProductPageLocators.PRICE_PRODUCT)
        if not message_price:
            if not price:
                assert False, "Locators 'PRICE_PRODUCT_ON_MESSAGE' and 'PRICE_PRODUCT' not correct or not have " \
                              "attribute 'text'."
            assert False, "Locator 'PRICE_PRODUCT_ON_MESSAGE' not correct or not have attribute 'text'."
        elif not price:
            assert False, "Locator 'PRICE_PRODUCT' not correct or not have attribute 'text'."
        else:
            if message_price == price:
                return True
            else:
                assert False, "Text PRICE_PRODUCT != text PRICE_PRODUCT_ON_MESSAGE."
