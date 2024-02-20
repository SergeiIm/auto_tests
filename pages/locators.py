from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.XPATH, '//*[@id="default"]/header/div[1]/div/div[2]/span/a')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators:
    pass


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "form#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, 'form#register_form')
    REGISTER_FORM_INPUT_USER_EMAIL = (By.CSS_SELECTOR, "input#id_registration-email")
    REGISTER_FORM_INPUT_PASSWORD_ONE = (By.CSS_SELECTOR, "input#id_registration-password1")
    REGISTER_FORM_INPUT_PASSWORD_TWO = (By.CSS_SELECTOR, "input#id_registration-password2")
    REGISTER_FORM_BTN_REGISTRATION = (By.CSS_SELECTOR, 'button[name="registration_submit"]')
    SUB_URL = ("login", )


class ProductPageLocators:
    BTN_ADD_TO_BASKET = (By.CSS_SELECTOR, "button.btn-add-to-basket")

    SUCCESS_MESSAGE = (By.XPATH, '//*[@id="messages"]/div[1]/div')
    GOOD_CHECK_MESSAGE_TEXT = 'has been added to your basket.'

    NAME_PRODUCT = (By.CSS_SELECTOR, "div#content_inner div.row h1")
    PRICE_PRODUCT = (By.CSS_SELECTOR, "div#content_inner div.row p.price_color")

    NAME_PRODUCT_ON_MESSAGE = (By.XPATH, '//*[@id="messages"]/div[1]/div/strong')
    PRICE_PRODUCT_ON_MESSAGE = (By.CSS_SELECTOR, 'div.alertinner p strong')


class BasketPageLocators:
    BASKET_MINI = (By.CSS_SELECTOR, "div.basket-mini")
    NAME_PRODUCT = (By.CSS_SELECTOR, "div.product_main h1")
    ROWS_IN_BASKET = (By.CSS_SELECTOR, "div.basket-items div.row")
    LINK_MESSAGE_BASKET_IS_EMPTY = (By.CSS_SELECTOR, "div#content_inner p")
    TEXT_MESSAGE_BASKET_IS_EMPTY = 'Your basket is empty.'
