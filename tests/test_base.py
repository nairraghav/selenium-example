from selenium import webdriver
from os import getenv as os_getenv


class TestBase:
    def setup(self):
        self.requested_browser = os_getenv("TEST_BROWSER", "chrome").lower()
        if self.requested_browser == "chrome":
            self.driver = webdriver.Chrome()
        elif self.requested_browser == "firefox":
            self.driver = webdriver.Firefox()
        else:
            raise TypeError("Unsupported Browser. Valid Options: Chrome/Firefox")

        self.driver.get("https://testpages.herokuapp.com/styled/index.html")

    def teardown(self):
        self.driver.close()
