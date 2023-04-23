from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class HeaderCureskin(Page):

    SEARCH_CURE_ICON = (By.CSS_SELECTOR, 'svg.icon.icon-search.modal__toggle-open')
    SEARCH_INPUT_FIELD = (By.ID, 'Search-In-Modal')
    SEARCH_FOR_BUTTON = (By.CSS_SELECTOR, 'button.predictive-search__item--term.button')

    def click_cure_search_icon(self):
        self.click(*self.SEARCH_CURE_ICON)


    def enter_search_text(self, text):
        self.input_text(text, *self.SEARCH_INPUT_FIELD)


    def click_search_for_button(self):
        self.click(*self.SEARCH_FOR_BUTTON)



