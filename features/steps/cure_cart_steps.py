from selenium.webdriver.common.by import By
from behave import when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC


@then('Verify {number_of_item} Items added to the cart')
def verify_cart_items(context, number_of_item):
    context.app.cart_page.verify_cart_items(number_of_item)


@then('Delete First Item from the cart')
def delete_first_product(context):
    context.app.cart_page.delete_first_product()


@then('Verify text {empty_cart_text} is displayed on empty cart')
def verify_empty_cart(context, empty_cart_text):
    sleep(5)
    context.app.cart_page.verify_cart_is_empty(empty_cart_text)


