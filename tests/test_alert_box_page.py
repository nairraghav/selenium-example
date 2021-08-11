from tests.pages.home_page import HomePage
from tests.test_base import TestBase


class TestAlertBoxPage(TestBase):
    def test_alert_box(self):
        home_page = HomePage(self.driver)
        assert home_page.is_page_rendered() is True
        alert_box_page = home_page.go_to_alert_box_page()

        assert alert_box_page.is_page_rendered() is True
        alert_box_page.validate_text_on_page()

        alert_box_page.interact_with_alert_box()
        alert_box_page.interact_with_confirm_box()
        alert_box_page.interact_with_prompt_box()
