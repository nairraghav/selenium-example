from json import dumps as json_dumps
class DynamicTablePage:
    def __init__(self, driver):
        self.driver = driver

        self.title_css = "h1"
        self.title_text = "Dynamic HTML TABLE Tag"
        self.explanation_css = "div.explanation > p"
        self.explanation_text = "An example of an HTML Table populated by JavaScript"
        self.table_name_css = "table#dynamictable > caption"
        self.table_name_text = "Dynamic Table"
        self.table_data_button_css = "div.centered > details"
        self.table_json_field_id = "jsondata"
        self.table_caption_field_id = "caption"
        self.table_id_field_id = "tableid"
        self.table_refresh_button_id = "refreshtable"
        self.table_values_css = "table#dynamictable > tr > td"

        self.default_table_data = [
            {"name": "Bob", "age": 20},
            {"name": "George", "age": 42},
        ]

    def is_page_rendered(self):
        for element_css in (
            self.title_css,
            self.explanation_css,
            self.table_name_css,
            self.table_data_button_css,
        ):
            found_element = self.driver.find_element_by_css_selector(element_css)
            if found_element is None:
                return False

        for element_id in (
            self.table_json_field_id,
            self.table_caption_field_id,
            self.table_id_field_id,
            self.table_refresh_button_id
        ):
            found_element = self.driver.find_element_by_id(element_id)
            if found_element is None:
                return False

        return True

    def validate_table(self):
        counter = 0
        table_data = self.driver.find_elements_by_css_selector(self.table_values_css)
        for user in self.default_table_data:
            assert table_data[counter].text == user["name"], f"Actual: {table_data[counter].text}\t\tExpected: {user['name']}"
            assert table_data[counter+1].text == str(user["age"]), f"Actual: {table_data[counter+1].text}\t\tExpected: {user['age']}"
            counter += 2

    def update_table_data(self):
        self.driver.find_element_by_tag_name("summary").click()
        table_data = self.driver.find_element_by_id(self.table_json_field_id)
        table_data.clear()
        table_data.send_keys(json_dumps(self.default_table_data))

        self.driver.find_element_by_id(self.table_refresh_button_id).click()

