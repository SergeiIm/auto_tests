from selenium.common.exceptions import NoSuchElementException


class BasePage:
    def __init__(self, browser, url: str, timeout: int = 10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what: str) -> bool:
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def is_str_in_url_present(self, sub_url: str) -> bool:
        try:
            self.url.index(sub_url)
        except ValueError:
            return False
        return True
