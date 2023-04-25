from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class SearchResultPage(Page):

    FIRST_SEARCH_ELEMENT = (By.ID, 'product-grid')
    PRODUCT_IMAGE = (By.CSS_SELECTOR, 'img.motion-reduce')
    PRODUCT_NAME = (By.CSS_SELECTOR, 'a.card-information__text')
    PRODUCT_PRICE = (By.CSS_SELECTOR, 'div.price.price--on-sale')
    PRODUCT_ADD_TO_CART = (By.CSS_SELECTOR, 'add-to-cart.button.button--small')
    VIEW_CART = (By.XPATH, "//form[@id='cart']//a[text()='View cart']")

    def verify_first_product_image(self):
        product = self.find_element(*self.FIRST_SEARCH_ELEMENT)
        assert product.find_element(*self.PRODUCT_IMAGE).is_displayed, 'Image Missing'

    def verify_first_product_name(self):
        product = self.find_element(*self.FIRST_SEARCH_ELEMENT)
        assert product.find_element(*self.PRODUCT_NAME).is_displayed(), 'Name Missing'

    def verify_first_product_price(self):
        product = self.find_element(*self.FIRST_SEARCH_ELEMENT)
        assert product.find_element(*self.PRODUCT_PRICE).is_displayed(), 'Price Missing'

    def add_item_to_cart(self):
        a = ActionChains(self.driver)
        product = self.find_element(*self.FIRST_SEARCH_ELEMENT)
        image = product.find_element(*self.PRODUCT_IMAGE)
        a.move_to_element(image).perform()
        add_button = product.find_element(*self.PRODUCT_ADD_TO_CART)
        a.move_to_element(add_button).click().perform()

    def click_view_cart(self):
        self.wait_for_element_click(*self.VIEW_CART)

