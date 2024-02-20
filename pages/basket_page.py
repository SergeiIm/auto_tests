from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_not_be_rows_on_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.ROWS_IN_BASKET), "Basket_should_be_empty."

    def should_be_attribute_text(self):
        try:
            element = self.browser.find_element(*BasketPageLocators.LINK_MESSAGE_BASKET_IS_EMPTY)
        except ValueError:
            assert False, "Not find element 'MESSAGE_BASKET_IS_EMPTY' on the page."
        try:
            tmp = element.text
        except TypeError:
            assert False, "Element not have attribute 'text'."
        message = BasketPageLocators.TEXT_MESSAGE_BASKET_IS_EMPTY
        assert message in tmp, f"Text element '{tmp}' not include message '{message}'."
        return True
