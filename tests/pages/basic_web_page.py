class BasicWebPage:
    def __init__(self, driver):
        self.driver = driver

        self.title_css = "h1"
        self.title_text = "Basic Web Page Example"
        self.explanation_css = "div.explanation > p"
        self.explanation_text = "Very simple web pages have a structure illustrated by this page. And elements can have id and class attributes for styling and locating"
        self.paragraph_one_id = "para1"
        self.paragraph_one_text = "A paragraph of text"
        self.paragraph_two_id = "para2"
        self.paragraph_two_text = "Another paragraph of text"

    def is_page_rendered(self):
        for element_css in (
            self.title_css,
            self.explanation_css,
        ):
            found_element = self.driver.find_element_by_css_selector(element_css)
            if found_element is None:
                return False

        for element_id in (
            self.paragraph_one_id,
            self.paragraph_two_id
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
            element = self.driver.find_element_by_css_selector(element_css)
            assert element.text == text

        for element_id, text in (
            (self.paragraph_one_id, self.paragraph_one_text),
            (self.paragraph_two_id, self.paragraph_two_text),
        ):
            element = self.driver.find_element_by_id(element_id)
            assert element.text == text
