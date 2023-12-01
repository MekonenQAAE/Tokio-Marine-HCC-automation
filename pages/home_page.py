from pages.base_page import BasePage
from selenium.webdriver.common.by import By



class HomePage(BasePage):
    LEFT_4_HEADER_MENU = (By.CSS_SELECTOR, ".header__primary-item")
    RIGHT_6_HEADER_MENU = (By.CSS_SELECTOR, ".header__secondary-item")
    SEARCH_ICON = (By.CSS_SELECTOR, ".header__search-icon")
    LOGO = (By.XPATH, "//a[@ href='/en-us']")
    SEARCH_FIELD =(By.ID, "SearchInputBox")
    SEARCH_SUBMIT = (By.ID, "searchSubmit")
    LANGUAGE_BUTTON = (By.CSS_SELECTOR, ".select-box-region__input-text")
    LANGUAGE_OPTIONS = (By.CSS_SELECTOR, ".select-box-region__list li")

    def open_home_page(self, url):
        self.open_page(url)

    def verify_visibility_header_menu(self):
        actual_header_menu = 10
        left_menu_elements = self.find_elements(*self.LEFT_4_HEADER_MENU)
        left_header_count = len(left_menu_elements)
        right_menu_elements = self.find_elements(*self.RIGHT_6_HEADER_MENU)
        right_header_count = len(right_menu_elements)
        expected_header_menu = left_header_count + right_header_count

        self.verify_element_int(actual_header_menu, expected_header_menu)

    def verify_user_can_click_header_menu(self):
        left_menu_elements = self.find_elements(*self.LEFT_4_HEADER_MENU)
        right_menu_elements = self.find_elements(*self.RIGHT_6_HEADER_MENU)
        total_menu = len(right_menu_elements)

        for i in range(total_menu):
            if i <= 3:
                left_menu_elements = self.find_elements(*self.LEFT_4_HEADER_MENU)
                left_menu_elements[i].click()
                right_menu_elements = self.find_elements(*self.RIGHT_6_HEADER_MENU)
                right_menu_elements[i].click()
            if i == 4:
                i += 1
            else:
                right_menu_elements = self.find_elements(*self.RIGHT_6_HEADER_MENU)
                right_menu_elements[i].click()

    def click_search_icon(self):
        element = self.find_elements(*self.SEARCH_ICON)
        element[1].click()

    def verify_clicking_logo_home_page(self):
        element = self.find_elements(*self.LOGO)
        element[0].click()
        self.verify_for_url_contains(self.base_url)

    def populate_search_field(self, input_data):
        self.input_text(input_data, *self.SEARCH_FIELD)

    def search_submit(self):
        self.wait_for_element_click(*self.SEARCH_SUBMIT)

    def verify_search_result(self, input_data):
        url_query = 'query=' + input_data
        print(url_query)
        self.verify_for_url_contains(url_query)

    def click_language_button(self):
        elements = self.find_elements(*self.LANGUAGE_BUTTON)[0].click()

    def verify_changing_language(self):
        languages = self.find_elements(*self.LANGUAGE_OPTIONS)
        languages[2].click()
        self.verify_for_url_contains('en')
        # count = len(languages)
        # language_list = ['Region', 'en-us', 'en', 'en-mx', 'es-mx']
        # for i in range(2, count):
        #     languages = self.find_elements(*self.LANGUAGE_OPTIONS)
        #     language = language_list[i]
        #     languages[i].click()
        #     self.verify_for_url_contains(language)
        #     self.find_elements(*self.LANGUAGE_OPTIONS)[i].click()



