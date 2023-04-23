from selenium.webdriver.common.by import By
from behave import when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC


@then('Verify search result UI is correct')
def verify_search_result(context):
    context.app.search_result_page.verify_first_product_image()
    context.app.search_result_page.verify_first_product_name()
    context.app.search_result_page.verify_first_product_price()

