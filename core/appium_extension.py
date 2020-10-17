import enum

from selenium.common.exceptions import *


class LocatorType(enum.Enum):
    id = 1
    name = 2
    class_name = 3
    link_text = 4
    tag_name = 5
    partial_link_text = 6
    css = 7
    xpath = 8
    predicate_string = 9
    class_chain_string = 10
    accessibility_id = 11


class AppiumExtension:
    """
    Selenium wrapper class for all the built-in appium methods.
    """

    def __init__(self, swipe_count=1):
        self.swipe_count = swipe_count

    driver, mobile_os = None, None

    def get_element(self, locator_info):
        """
        To find the element in DOM to interact with.
        :param locator_info:  unique locator and locator type.
        :return: identified web element.
        """
        locator_type, locator_value = get_locator(locator_info)
        count = 0
        while count < self.swipe_count:
            try:
                return self.driver.find_element(locator_type, locator_value)

            except NoSuchElementException:
                size = self.driver.get_window_size()
                start_y = size['height'] * 0.8
                end_y = size['height'] * 0.2
                start_x = size['width'] * 0.8
                end_x = size['width'] * 0.8
                self.driver.swipe(start_x, start_y, end_x, end_y, 2000)
                count += 1

        print("element not found with the given locator info: " + str(locator_info))
        raise NoSuchElementException


def get_locator(locator_info):
    """
    Used to returned tuple with locator type and its value
    :param locator_info: list of locator type and its value
    :return: locator and its value as a tuple
    """
    locator_type = None
    locator_value = None
    for key, value in locator_info.items():
        locator_type = key
        locator_value = value
    return locator_type, locator_value
