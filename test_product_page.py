from time import sleep

import pytest

from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage


links = ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
         pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"]

link1 = ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/", ]
link2 = ["http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/", ]


# cmd: pytest -v --tb=line --language=en
@pytest.mark.parametrize('full_link', links)
def test_guest_can_add_product_to_basket(browser, full_link):
    product_page = ProductPage(browser, full_link)
    product_page.open()
    product_page.check_and_add_price_name_product_and_basket_default()
    product_page.click_add_to_basket_btn()
    product_page.pass_the_check_stepik()

    basket_page = BasketPage(browser=browser, url=browser.current_url)
    basket_page.add_product_on_basket()

    name_prod_page = product_page.dict_objects['name']
    name_basket_page = basket_page.dict_objects['name']
    if name_prod_page != name_basket_page:
        assert False, f"Wrong name product: prod_name '{name_prod_page}' and basket_name '{name_basket_page}'."

    price_prod_page = product_page.dict_objects['price']
    price_basket_page = basket_page.dict_objects['basket-mini']
    if price_prod_page not in price_basket_page:
        assert False, f"Wrong price product: price_prod '{price_prod_page}' and price_basket '{price_basket_page}'"


@pytest.mark.parametrize('full_link', link1)
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, full_link):
    product_page = ProductPage(browser, full_link)
    product_page.open()
    product_page.click_add_to_basket_btn()
    product_page.should_not_be_success_message()


@pytest.mark.parametrize('full_link', link1)
def test_guest_cant_see_success_message_one(browser, full_link):
    product_page = ProductPage(browser, full_link)
    product_page.open()
    product_page.should_not_be_success_message()


@pytest.mark.parametrize('full_link', link1)
def test_message_disappeared_after_adding_product_to_basket(browser, full_link):
    product_page = ProductPage(browser, full_link)
    product_page.open()
    product_page.should_disappear_success_message()


@pytest.mark.parametrize('full_link', link2)
def test_guest_should_see_login_link_on_product_page(browser, full_link):
    page = ProductPage(browser, full_link)
    page.open()
    page.should_be_login_link()


@pytest.mark.parametrize('full_link', link2)
def test_guest_can_go_to_login_page_from_product_page(browser, full_link):
    page = ProductPage(browser, full_link)
    page.open()
    page.go_to_login_page()
