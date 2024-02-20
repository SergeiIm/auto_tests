# from time import sleep

import pytest

from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage

links_1 = ["http://selenium1py.pythonanywhere.com/", ]
links_2 = ['http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer', ]


@pytest.mark.parametrize('link', links_1)
def test_guest_can_go_to_login_page(browser, link):
    page_main = MainPage(browser=browser, url=link)
    page_main.open()
    page_main.should_be_login_link()
    page_main.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


@pytest.mark.parametrize('link', links_1)
def test_guest_should_see_login_link(browser, link):
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.parametrize('link', links_1)
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser, link):
    # Гость открывает главную страницу.
    page = MainPage(browser, link)
    page.open()
    # Переходит в корзину по кнопке в шапке сайта.
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    # Ожидаем, что в корзине нет товаров.
    basket_page.should_not_be_rows_on_basket()
    # Ожидаем, что есть текст о том что корзина пуста.
    basket_page.should_be_attribute_text()
