
from core.base_page import BasePage


class HomePage(BasePage):
    grid_button_heading_deceased = 'xpath|//div[@class="cell heading"]//div[text()="Deceased"]//parent::div'
    grid_button_heading_deceased_invert = 'xpath|//div[@class="cell heading"]//div[text()="Deceased"]//parent::div/div[1]'


    grid_data_rows = 'xpath|//div[contains(@class,"row") and not(contains(@class,"heading"))]'
    grid_data_all_state_names = 'xpath|//div[contains(@class,"state-name")]'
    row_state_name = '//div[1]/div'
    row_state_confirmed_count = '//div[2]/div[@class="total"]'
    row_state_active_count = '//div[3]/div[@class="total"]'
    row_state_recovered_count = '//div[4]/div[@class="total"]'
    row_state_deceased_count = '//div[5]/div[@class="total"]'
    row_state_tested_count = '//div[6]/div[@class="total"]'

    state_page_more_link = 'xpath|//div[contains(@class,"state-page")]'
    no_data_for_district = 'xpath|//div[@class="disclaimer"]//span[text()="District-wise data not available in state bulletin"]'

    def __init__(self, driver, base_url="https://www.covid19india.org"):
        super().__init__(driver)
        self.base_url = base_url

    def open_home_page(self):
        self.open_url(self.base_url)

    def click_deceased_sort_desc(self):
        elem = self.com.find_elem(self.grid_button_heading_deceased)
        elem.click()
        elem_invert = self.com.find_elem(self.grid_button_heading_deceased_invert)
        if "invert" in elem_invert.get_attribute("class"):
            elem.click()

    def click_deceased_sort_asc(self):
        elem = self.com.find_elem(self.grid_button_heading_deceased)
        elem.click()
        elem_invert = self.com.find_elem(self.grid_button_heading_deceased_invert)
        if "invert" not in elem_invert.get_attribute("class"):
            elem.click()

    def get_nth_state_name(self,nth):
        nth = "[{}]".format(nth-1)
        nth_row = self.com.find_elem(self.grid_data_rows + nth +self.row_state_name)
        return nth_row.text

    def get_nth_state_confirmed_count(self,nth):
        nth = "[{}]".format(nth-1)
        nth_row = self.com.find_elem(self.grid_data_rows + nth +self.row_state_confirmed_count)
        return str(nth_row.get_attribute("title"))

    def get_nth_state_active_count(self,nth):
        nth = "[{}]".format(nth-1)
        nth_row = self.com.find_elem(self.grid_data_rows + nth +self.row_state_active_count)
        return str(nth_row.get_attribute("title"))

    def get_nth_state_recovered_count(self,nth):
        nth = "[{}]".format(nth-1)
        nth_row = self.com.find_elem(self.grid_data_rows + nth + self.row_state_recovered_count)
        return str(nth_row.get_attribute("title"))

    def get_nth_state_deceased_count(self,nth):
        nth = "[{}]".format(nth-1)
        nth_row = self.com.find_elem(self.grid_data_rows + nth + self.row_state_deceased_count)
        return str(nth_row.get_attribute("title"))

    def get_nth_state_tested_count(self,nth):
        nth = "[{}]".format(nth-1)
        nth_row = self.com.find_elem(self.grid_data_rows + nth + self.row_state_tested_count)
        return str(nth_row.get_attribute("title"))

    def get_row_count_by_state_name(self,state_name):
        all_state_elems = self.com.find_elems(self.grid_data_all_state_names)
        for i in range(len(all_state_elems)):
            self.com.scroll_into_view(all_state_elems[i])
            if all_state_elems[i].text == state_name:
                return i+1
        return 1

    def click_nth_state_page_link(self,nth):
        nth = "[{}]".format(nth-1)
        nth_row = self.com.find_elem(self.grid_data_rows + nth + self.row_state_name)
        nth_row.click()
        if (self.is_district_data_available()):
            self.com.find_elem(self.state_page_more_link).click()
            return True
        else:
            print("No district data available")
            return False

    def is_district_data_available(self):
        elems = self.com.find_elems(self.no_data_for_district)
        return len(elems)==0




