class AlertBoxPage:
    def __init__(self, driver):
        self.driver = driver

        self.title_css = "h1"
        self.title_text = "Alert Box Examples"
        self.explanation_css = "div.explanation > p"
        self.explanation_text = (
            "There are three main JavaScript methods "
            "which show alert dialogs: alert, confirm "
            "and prompt. This page has examples of each."
        )
        self.alert_box_descriptions_css = "div.page-body > p"
        self.alert_box_description_text = (
            "The following button will display an alert when clicked."
        )
        self.alert_box_button_id = "alertexamples"
        self.alert_box_button_text = "Show alert box"
        self.alert_box_text = "I am an alert box!"
        self.confirm_box_description_text = (
            "The following button will display a confirm dialog when clicked."
        )
        self.confirm_box_button_id = "confirmexample"
        self.confirm_box_button_text = "Show confirm box"
        self.confirm_boolean_text_id = "confirmreturn"
        self.confirm_boolean_confirm_text = "true"
        self.confirm_boolean_cancel_text = "false"
        self.confirm_text_id = "confirmexplanation"
        self.confirm_text = "You clicked OK, confirm returned true."
        self.cancel_text = "You clicked Cancel, confirm returned false."
        self.prompt_box_description_text = (
            "The following button will display a prompt dialog when clicked."
        )
        self.prompt_box_button_id = "promptexample"
        self.prompt_box_button_text = "Show prompt box"
        self.prompt_box_text = "I prompt you"
        self.prompt_value_text_id = "promptreturn"
        self.prompt_text_id = "promptexplanation"
        self.prompt_text_prefix = "You clicked OK. 'prompt' returned "
        self.prompt_cancel_text = "You clicked Cancel. 'prompt' returned null"

    def is_page_rendered(self):
        for element_css in (
            self.title_css,
            self.explanation_css,
            self.alert_box_descriptions_css,
        ):
            found_element = self.driver.find_element_by_css_selector(element_css)
            if found_element is None:
                return False

        for element_id in (
            self.alert_box_button_id,
            self.confirm_box_button_id,
            self.prompt_box_button_id,
        ):
            found_element = self.driver.find_element_by_id(element_id)
            if found_element is None:
                return False

        return True

    def validate_text_on_page(self):
        for element_css, text in (
            (self.title_css, self.title_text),
            (self.explanation_css, self.explanation_text),
        ):
            found_element = self.driver.find_element_by_css_selector(element_css)
            assert found_element.text == text
        for element_id, text in (
            (self.alert_box_button_id, self.alert_box_button_text),
            (self.confirm_box_button_id, self.confirm_box_button_text),
            (self.prompt_box_button_id, self.prompt_box_button_text),
        ):
            found_element = self.driver.find_element_by_id(element_id)
            assert found_element.get_attribute("value") == text, (
                f"Actual: {found_element.get_attribute('value')}\t\t" "Expected: {text}"
            )

        descriptions = self.driver.find_elements_by_css_selector(
            self.alert_box_descriptions_css
        )
        assert descriptions[0].text == self.alert_box_description_text
        assert descriptions[2].text == self.confirm_box_description_text
        assert descriptions[4].text == self.prompt_box_description_text

    def interact_with_alert_box(self):
        self.driver.find_element_by_id(self.alert_box_button_id).click()
        alert = self.driver.switch_to.alert
        alert.accept()

    def interact_with_confirm_box(self):
        self.driver.find_element_by_id(self.confirm_box_button_id).click()
        alert = self.driver.switch_to.alert
        alert.accept()
        assert (
            self.driver.find_element_by_id(self.confirm_boolean_text_id).text
            == self.confirm_boolean_confirm_text
        )
        assert (
            self.driver.find_element_by_id(self.confirm_text_id).text
            == self.confirm_text
        )

        self.driver.find_element_by_id(self.confirm_box_button_id).click()
        alert = self.driver.switch_to.alert
        alert.dismiss()
        assert (
            self.driver.find_element_by_id(self.confirm_boolean_text_id).text
            == self.confirm_boolean_cancel_text
        )
        assert (
            self.driver.find_element_by_id(self.confirm_text_id).text
            == self.cancel_text
        )

    def interact_with_prompt_box(self):
        self.driver.find_element_by_id(self.prompt_box_button_id).click()
        alert = self.driver.switch_to.alert
        alert_text = "Testing"
        alert.send_keys(alert_text)
        alert.accept()
        assert (
            self.driver.find_element_by_id(self.prompt_value_text_id).text == alert_text
        )
        assert (
            self.driver.find_element_by_id(self.prompt_text_id).text
            == f"{self.prompt_text_prefix}{alert_text}"
        )

        self.driver.find_element_by_id(self.prompt_box_button_id).click()
        alert = self.driver.switch_to.alert
        alert.dismiss()
        assert (
            self.driver.find_element_by_id(self.prompt_text_id).text
            == self.prompt_cancel_text
        )
