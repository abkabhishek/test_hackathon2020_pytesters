import os
import sys

from appium import webdriver
from appium.webdriver.appium_service import AppiumService

dir_path = os.path.dirname(os.path.realpath(__file__))


class AppiumFactory:
    """
    Factory for Appium Driver to handle app type and app instance.
    """
    os_platform = sys.platform
    desired_caps = None

    def __init__(self, request):
        self.mobile_os = request.config.getoption("--mobile-os")

    def get_mobile_app(self):
        """
        This method is used to launch mobile web browser and native apps in mobile environment.
        """
        self.start_appium_server(['--chromedriver-executable', './resources/chromedriver-mob.exe'])
        driver = self._get_mobile_browser()
        return driver

    def start_appium_server(self, server_arguments=None):
        """
        used to start appium server before test executions
        :param server_arguments: Server arguments list
        """
        appium_service = AppiumService()
        appium_service.start(args=server_arguments or [])

    def android_caps(self):
        """
        android capabilities
        :return:
        """
        return dict(
            platformName="android",
            platformVersion="10",
            automationName="UIautomator2",
            browserName="chrome"
        )

    def _get_mobile_browser(self):
        """
        Used to get the web app driver
        :return: Web app driver
        """
        try:
            return webdriver.Remote("http://localhost:4723/wd/hub", self.android_caps(), direct_connection=True)
        except Exception as ex:
            raise ex


