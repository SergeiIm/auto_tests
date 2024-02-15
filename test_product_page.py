from time import sleep
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage


# cmd: pytest -v --tb=line --language=en
def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/"
    end_promo_link = "?promo=newYear"
    full_link = link + end_promo_link
    product_page = ProductPage(browser, full_link)
    product_page.open()
    product_page.check_and_add_price_name_product_and_basket_default()
    product_page.click_add_to_basket_btn_and_pass_the_check_stepik()

    sleep(3)
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

    sleep(10)
