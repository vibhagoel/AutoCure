from selenium.webdriver.common.by import By
from behave import when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC


@when('Add Item to the cart')
def add_item_to_cart(context):
    context.app.search_result_page.add_item_to_cart()


@when('Click on View Cart')
def click_view_cart(context):
    #sleep(10)
    context.app.search_result_page.click_view_cart()


@then('Verify search result UI is correct')
def verify_search_result(context):
    context.app.search_result_page.verify_first_product_image()
    context.app.search_result_page.verify_first_product_name()
    context.app.search_result_page.verify_first_product_price()

