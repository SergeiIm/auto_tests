from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "form#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, 'form#register_form')
    SUB_URL = "login"


class ProductPageLocators:
    BTN_ADD_TO_BASKET = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    BASKET_MINI = (By.CSS_SELECTOR, "div.basket-mini")
    GO_TO_THE_BASKET_BTN = (By.CSS_SELECTOR, "div.basket-mini a")
    NAME_PRODUCT = (By.CSS_SELECTOR, "div.product_main  h1")
    PRICE_PRODUCT = (By.CSS_SELECTOR, "div.product_main p.price_color")


class BasketPageLocators:
    BASKET_MINI = (By.CSS_SELECTOR, "div.basket-mini")
    NAME_PRODUCT = (By.CSS_SELECTOR, "div.product_main h1")

