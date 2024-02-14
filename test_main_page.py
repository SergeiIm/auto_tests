from time import sleep
from .pages.main_page import MainPage
from .pages.login_page import LoginPage


# cmd: pytest -v --tb=line --language=en
def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser=browser, url=link)
    page.open()
    sleep(1)
    page.should_be_login_link()
    sleep(1)
    page.go_to_login_page()
    sleep(1)
    page_login = LoginPage(browser=browser, url=browser.current_url)
    sleep(1)
    page_login.should_be_login_page()

#def test_add_to_cart(browser):
#    page = ProductPage(url="", browser)   # инициализируем объект Page Object
#    page.open()                           # открываем страницу в браузере
#    page.should_be_add_to_cart_button()   # проверяем что есть кнопка добавления в корзину
#    page.add_product_to_cart()            # жмем кнопку добавить в корзину
#    page.should_be_success_message()      # проверяем что есть сообщение с нужным текстом
