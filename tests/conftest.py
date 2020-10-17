import pytest
import pytest_html


from core.browser import Browser
from pom.home_page import HomePage
from pom.API import APITest

@pytest.fixture
def app():
    # get Web Driver
    b = Browser.get_driver()
    b.implicitly_wait(5)
    # creating App object
    app = App(b, "https://www.covid19india.org/")

    yield app   # return App

    b.quit()  # closing all browser
    del app


class App:

    def __init__(self, driver, base_url):
        self.home_page = HomePage(driver, base_url)
        self.api = APITest(driver)