from time import sleep
from selenium.webdriver.common.by import By


# cmd: pytest -v --tb=line --language=en
def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    browser.get(link)
    sleep(3)
    login_link = browser.find_element(By.CSS_SELECTOR, "#login_link")
    login_link.click()
    sleep(3)
