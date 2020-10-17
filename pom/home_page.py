
from core.base_page import BasePage

class HomePage(BasePage):


    def __init__(self,driver,base_url = "https://www.covid19india.org"):
        super().__init__(driver)
        self.base_url = base_url

    def open_home_page(self):
        self.open_url(self.base_url)

