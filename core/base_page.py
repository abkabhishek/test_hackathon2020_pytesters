
from core.common import Com


class BasePage(object):
    driver = None

    def __init__(self, driver):
        BasePage.driver = driver
        self.com = Com(driver)

    def open_url(self, url):
        self.driver.get(url)

    def close(self):
        BasePage.driver.close()

    def quit(self):
        BasePage.driver.quit()

    def get_title(self):
        return self.driver.title