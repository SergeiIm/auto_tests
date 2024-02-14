

class BasePage:
    def __init__(self, browser, url: str):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)
