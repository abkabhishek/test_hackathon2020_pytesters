
from core.base_page import BasePage


class StatePage(BasePage):

    confirmed_count_all_district_counts = 'xpath|//div[contains(@class,"districts")]/div/h2'
    confirmed_count_all_district_names = 'xpath|//div[contains(@class,"districts")]/div/h5'

    view_all_districts_button = 'xpath|//div[contains(@class,"district-bar-bottom")]/button/span[text()="View all"]'



    def __init__(self, driver):
        super().__init__(driver)

    def get_all_districts_data(self):
        view_all = self.com.find_elems(self.view_all_districts_button)
        if (view_all):
            view_all[0].click()
        districts = {}
        districts_name_elems = self.com.find_elems(self.confirmed_count_all_district_names)
        districts_count_elems = self.com.find_elems(self.confirmed_count_all_district_counts)
        for i in range(len(districts_name_elems)):
            x = str(districts_count_elems[i].text.strip().replace(",",""))
            if x=="":
                districts[districts_name_elems[i].text.strip()] = 0
            else:
                districts[districts_name_elems[i].text.strip()] = int(x)
        return districts








