from pages.home_page import HomePage


class Application:

    def __init__(self, driver):
        self.driver = driver
        self.home_page = HomePage(self.driver)
