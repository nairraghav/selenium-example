from tests.pages.home_page import HomePage
from tests.test_base import TestBase

class TestDynamicTablePage(TestBase):
    
    def test_dynamic_table(self):
        home_page = HomePage(self.driver)
        assert home_page.is_page_rendered() is True
        dynamic_table_page = home_page.go_to_dynamic_table_page()

        assert dynamic_table_page.is_page_rendered() is True

        dynamic_table_page.validate_table()
        
        dynamic_table_page.default_table_data.append({"name": "Ron", "age": 30})
        dynamic_table_page.update_table_data()
        dynamic_table_page.validate_table()
