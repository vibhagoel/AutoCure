from pages.base_page import Page
from selenium.webdriver.common.by import By


class CartPage(Page):
    CART_COUNT_BUBBLE = (By.CSS_SELECTOR, 'div.cart-count-bubble')
    DELETE_FIRST_PRODUCT = (By.ID, 'Remove-1')
    EMPTY_CART_TEXT = (By.CSS_SELECTOR, 'h2.cart__empty-text')

    def verify_cart_items(self, number_of_item):
        self.verify_partial_text(str(number_of_item), *self.CART_COUNT_BUBBLE)

    def delete_first_product(self):
        self.click(*self.DELETE_FIRST_PRODUCT)

    def verify_cart_is_empty(self, empty_cart_text):
         self.verify_text(empty_cart_text, *self.EMPTY_CART_TEXT)



