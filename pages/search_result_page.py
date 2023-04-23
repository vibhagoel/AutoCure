from pages.base_page import Page
from selenium.webdriver.common.by import By


class SearchResultPage(Page):

    FIRST_SEARCH_ELEMENT = (By.ID, 'product-grid')
    PRODUCT_IMAGE = (By.CSS_SELECTOR, 'img.motion-reduce')
    PRODUCT_NAME = (By.CSS_SELECTOR, 'a.card-information__text')
    PRODUCT_PRICE = (By.CSS_SELECTOR, 'div.price.price--on-sale')

    def verify_first_product_image(self):
        product = self.find_element(*self.FIRST_SEARCH_ELEMENT)
        assert product.find_element(*self.PRODUCT_IMAGE).is_displayed, 'Image Missing'

    def verify_first_product_name(self):
        product = self.find_element(*self.FIRST_SEARCH_ELEMENT)
        assert product.find_element(*self.PRODUCT_NAME).is_displayed(), 'Name Missing'

    def verify_first_product_price(self):
        product = self.find_element(*self.FIRST_SEARCH_ELEMENT)
        assert product.find_element(*self.PRODUCT_PRICE).is_displayed(), 'Price Missing'