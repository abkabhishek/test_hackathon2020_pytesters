from sys import stdout as console
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

WAIT_TIME_OUT = 30
class Com:

    driver = None
    wait = None
    windowTabs = {}

    def __init__(self, driver):
        Com.driver = driver
        Com.wait = Wait(driver)


    @classmethod
    def find_elem(cls, locatr, elem=None):
        try:
            if elem:
                return elem.find_element(*Locatr.get_locatr_by(locatr))
            else:
                return cls.driver.find_element(*Locatr.get_locatr_by(locatr))
        except NoSuchElementException as e:
            print(e)
            print("Unable to find the element by: {}, locator: {}".format(*Locatr.get_locatr_by(locatr)))
            raise Exception("Element not found")

    @classmethod
    def find_elems(cls, locatr, elem=None):
        if elem:
            return elem.find_elements(*Locatr.get_locatr_by(locatr))
        else:
            return cls.driver.find_elements(*Locatr.get_locatr_by(locatr))




class Locatr:
    """
    Helper class to convert "css|string" type locator to (CSS_SELECTOR,"string")
    """

    @staticmethod
    def get_locatr_by(locatr):
        if "|" in locatr:
            locatrBy, locatrStr = locatr.split("|")

            if locatrBy.lower() == "xpath":
                return By.XPATH, locatrStr
            elif locatrBy.lower() == "id":
                return By.ID, locatrStr
            elif locatrBy.lower() == "css":
                return By.CSS_SELECTOR, locatrStr
            elif locatrBy.lower() == "name":
                return By.NAME, locatrStr
            elif locatrBy.lower() == "class":
                return By.CLASS_NAME, locatrStr
            elif locatrBy.lower() == "tagname":
                return By.TAG_NAME, locatrStr
            else:
                return By.ID, locatrStr
        else:
            raise Exception("Invalid locatr string : {}".format(locatr))


class Wait:

    def __init__(self, driver):
        self.driver = driver

    def wait_for_element_visible(self, locatr, timeout=WAIT_TIME_OUT):
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(Locatr.get_locatr_by(locatr))
            )
            return element
        except Exception as e:
            print(e)
            raise Exception("Element ( by: {}, locator: {}) is not visible after waiting until timeout {}".format(*Locatr.get_locatr_by(locatr),timeout))

    def wait_for_element_with_text_present(self,locatr,text,timeout=WAIT_TIME_OUT):
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.text_to_be_present_in_element(Locatr.get_locatr_by(locatr),text)
            )
            return element
        except Exception as e:
            print(e)
            raise Exception("Element ( by: {}, locator: {}) is not present with text {} after waiting until timeout {}".format(*Locatr.get_locatr_by(locatr),text,timeout))


    def is_element_present(self, locatr):
        try:
            self.driver.find_element(*Locatr.get_locatr_by(locatr))
            return True
        except Exception:
            return False

    def is_element_text_visible(self,locatr,text):
        try:
            element = self.driver.find_element(*Locatr.get_locatr_by(locatr))
            return element.is_displayed() and text in element.text
        except Exception:
            return False