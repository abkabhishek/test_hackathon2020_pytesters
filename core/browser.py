from sys import platform
from selenium import webdriver
import os
import sys
sys.path.append("/Users/abk/dev2020/python/all/office/test_hackathon2020_pytesters")
from pom.home_page import HomePage
import time

from selenium.webdriver.chrome.options import Options

dir_path = os.path.dirname(os.path.realpath(__file__))


class Browser:

    @classmethod
    def get_driver(cls, settings={"browser": "chrome", "environment": "local","headless":"false"}):
        print('==============INIT=================')
        driver = None
        if settings["environment"] == "local":
            if platform == "darwin":
                # OS X
                if settings["browser"] == 'chrome':
                    chrome_options = Options()
                    if settings["headless"] == "true":
                        chrome_options.add_argument("--headless")
                    driver = webdriver.Chrome(executable_path="resources/chromedriver_mac",options=chrome_options)

                else:
                    print("Invalid Browser passed")
                    raise Exception("Invalid Browser passed")

            elif platform == "win32":
                # Windows...
                if settings["browser"] == 'chrome':
                    chrome_options = Options()
                    if settings["headless"] == "true":
                        chrome_options.add_argument("--headless")

                    driver = webdriver.Chrome(
                        executable_path='./resources/chromedriver.exe',
                        options=chrome_options
                    )

                else:
                    print("Invalid Browser passed")
                    raise Exception("Invalid Browser passed")
            elif platform == "linux" or platform == "linux2":
                # linux
                raise Exception("TBD for Linux")
        elif settings["environment"] == "remote":
             # Make sure to run "docker-compose up -d" before running test
            remote_grid_url = 'http://localhost:4444/wd/hub'
            chrome_options = Options()
            if settings["headless"] == "true":
                chrome_options.add_argument('--headless')
            capabilities = {'browserName': 'chrome', 'javascriptEnabled': True}
            capabilities.update(chrome_options.to_capabilities())
            driver = webdriver.Remote(
                command_executor=remote_grid_url,
                desired_capabilities=capabilities
            )

        return driver


if __name__ == "__main__":
    pass
    # driver = Browser.get_driver()
    # home = HomePage(driver,"https://www.covid19india.org/")
    # home.open_home()
    # time.sleep(3)
    # home.click_deceased_sort_desc()
    # time.sleep(3)
    # x = home.get_nth_state_name(1)
    # print(x)
    # # assert ( x== "Odisha")
    # x = home.get_nth_state_confirmed_count(1)
    # print(x)
    # # assert (x == 266345)
    # x = home.get_nth_state_active_count(1)
    # print(x)
    # # assert (x == 23786)
    # x = home.get_nth_state_recovered_count(1)
    # print(x)
    # # assert ( x== 241385)
    # x = home.get_nth_state_deceased_count(1)
    # print(x)
    # # assert ( x== 1174)
    # x = home.get_nth_state_tested_count(1)
    # print(x)
    # driver.quit()
