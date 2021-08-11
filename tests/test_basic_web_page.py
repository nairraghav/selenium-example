from tests.pages.home_page import HomePage
from tests.test_base import TestBase


class TestBasicWebPage(TestBase):
    def test_basic_page(self):
        home_page = HomePage(self.driver)
        assert home_page.is_page_rendered() is True
        basic_web_page = home_page.go_to_basic_page()

        assert basic_web_page.is_page_rendered() is True
        basic_web_page.validate_text_on_page()
