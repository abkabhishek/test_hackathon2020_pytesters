import pytest

from core.browser import Browser
from core.appium_extension import AppiumExtension
from core.appium_factory import AppiumFactory
from pom.home_page import HomePage
from pom.state_page import StatePage
from pom.APIWrapper import APITest


mobile_run = None


def pytest_addoption(parser):
    """Used to add command line arguments."""
    parser.addoption("--mobile-os", help="mobile os")


def pytest_configure(config):
    """
    A pytest hook to add , update config and create loggers for normal and parallel executions
    :param config: config
    """

    global mobile_run
    mobile_run = config.getoption("--mobile-os") or None
    print(mobile_run)


@pytest.fixture(autouse=True)
def appium_setup(request):
    """
    :param request: initialize the driver object
    :return: app instance
    """
    get_appium_factory = AppiumFactory(request)
    if mobile_run:
        AppiumExtension.driver = get_appium_factory.get_mobile_app()
    yield AppiumExtension.driver
    if mobile_run:
        print("Mobile Set up end")
        AppiumExtension.driver.quit()


@pytest.fixture
def app():
    # get Web Driver
    b = Browser.get_driver()

    # creating App object
    app = App(b, "https://www.covid19india.org/")

    yield app   # return App

    b.quit()  # closing all browser
    del app


class App:

    def __init__(self, driver, base_url):
        self.home_page = HomePage(driver, base_url)
        self.state_page = StatePage(driver)
        self.api = APITest(driver)
