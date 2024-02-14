from selenium import webdriver
import pytest
from selenium.webdriver.firefox.options import Options as OptionsFirefox
from selenium.webdriver.chrome.options import Options as OptionsChrome


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en', help='input language')
    parser.addoption('--browser_name', action='store', default='Chrome', help='input browser name: chrome or firefox')


@pytest.fixture(scope='class')
def browser(request):
    browser_name = request.config.getoption('browser_name')
    browser_lang = request.config.getoption('language')
    if browser_name.lower() == 'chrome':
        options = OptionsChrome()
        options.add_experimental_option("prefs", {'intl.accept_languages': browser_lang})
        print("\n>>> start browser chrome for class test.")
        browser = webdriver.Chrome(options=options)
    elif browser_name.lower() == 'firefox':
        options = OptionsFirefox()
        options.set_preference("intl.accept_languages", browser_lang)
        print("\n>>> start browser firefox for class test.")
        browser = webdriver.Firefox(options=options)
    else:
        assert False, \
            '\n>>> input browser name: chrome or firefox.'

    yield browser
    print("\nquit browser for test.")
    browser.quit()
