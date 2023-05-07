from pages.base_page import Page
from selenium.webdriver.common.by import By


class MainCurePage(Page):

    CLOSE_POPUP = (By.CSS_SELECTOR, 'button.popup-close')

    def open_main_url(self):
        self.open_url('https://shop.cureskin.com/')

    def close_main_popup(self):
        self.wait_for_element_click(*self.CLOSE_POPUP)
