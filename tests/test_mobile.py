import pytest

from core.appium_extension import AppiumExtension
from pom.home_page import HomePage

appium_extension = AppiumExtension()

home_page = HomePage(appium_extension.driver)


def test_launch_101():
    appium_extension.driver.get("https://www.covid19india.org")
