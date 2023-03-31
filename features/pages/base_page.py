class BasePage:
    URL = "https://the-internet.herokuapp.com/base_page"

    def __init__(self, driver):
        self.driver = driver

    def go_page_home(self):
        self.driver.get(self.URL)
