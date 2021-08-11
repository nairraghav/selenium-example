from tests.pages.basic_web_page import BasicWebPage
from tests.pages.alert_box_page import AlertBoxPage
from tests.pages.dynamic_table_page import DynamicTablePage


class HomePage:
    def __init__(self, driver):
        self.driver = driver

        self.basic_page_text_id = "basicpagetest"
        self.alert_page_text_id = "alerttest"
        self.dynamic_table_text_id = "dynamictablestest"

    def is_page_rendered(self):
        for element in (
            self.basic_page_text_id,
            self.alert_page_text_id,
            self.dynamic_table_text_id,
        ):
            found_element = self.driver.find_element_by_id(element)
            if found_element is None:
                return False
        return True

    def go_to_basic_page(self):
        self.driver.find_element_by_id(self.basic_page_text_id).click()
        return BasicWebPage(self.driver)

    def go_to_alert_box_page(self):
        self.driver.find_element_by_id(self.alert_page_text_id).click()
        return AlertBoxPage(self.driver)

    def go_to_dynamic_table_page(self):
        self.driver.find_element_by_id(self.dynamic_table_text_id).click()
        return DynamicTablePage(self.driver)
