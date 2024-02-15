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
