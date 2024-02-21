from time import time

import pytest

from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
from .pages.product_page import ProductPage


links_1 = ['http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear', ]
links_2 = ['http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019', ]
links_3 = ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
           "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
           "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
           "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
           "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
           "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
           "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
           pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                        marks=pytest.mark.xfail),
           "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
           "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"]
links_4 = ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/", ]
links_5 = ["http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/", ]
links_6 = ["http://selenium1py.pythonanywhere.com"]


@pytest.mark.xfail
@pytest.mark.parametrize('link', links_4)
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, link):
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.click_btn_add_to_basket()
    product_page.should_not_be_success_message()


@pytest.mark.xfail
@pytest.mark.parametrize('link', links_4)
def test_message_disappeared_after_adding_product_to_basket(browser, link):
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.click_btn_add_to_basket()
    product_page.should_be_disappeared_message()


@pytest.mark.parametrize('link', links_5)
def test_guest_should_see_login_link_on_product_page(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
@pytest.mark.parametrize('link', links_5)
def test_guest_can_go_to_login_page_from_product_page(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


@pytest.mark.need_review
@pytest.mark.parametrize('link', links_4)
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_rows_on_basket()
    basket_page.should_be_attribute_text()


@pytest.mark.need_review
@pytest.mark.parametrize('link', links_1)
def test_guest_can_add_product_to_basket(browser, link):
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.click_btn_add_to_basket()
    product_page.solve_quiz_and_get_code()
    product_page.check_added_product_on_basket()
    product_page.check_name_of_product_on_message_add_on_basket()
    product_page.check_price_of_product_on_message_add_on_basket()


class TestUserAddToBasketFromProductPage:
    @classmethod
    def get_email_and_password(cls):
        tmp = time()
        email = str(tmp) + "@fakemail.org"
        password = str(tmp)
        return email, password

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser, link):
        login_page = LoginPage(browser, link)
        login_page.open()
        login_page.go_to_login_page()
        login_page.register_new_user(*self.get_email_and_password())

    @pytest.mark.parametrize('link', links_1)
    def test_user_cant_see_success_message(self, browser, link):
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.should_not_be_success_message()

    @pytest.mark.need_review
    @pytest.mark.parametrize('link', links_1)
    def test_user_can_add_product_to_basket(self, browser, link):
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.click_btn_add_to_basket()
        product_page.solve_quiz_and_get_code()
        product_page.check_added_product_on_basket()
        product_page.check_name_of_product_on_message_add_on_basket()
        product_page.check_price_of_product_on_message_add_on_basket()
