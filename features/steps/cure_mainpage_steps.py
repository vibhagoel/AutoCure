from selenium.webdriver.common.by import By
from behave import when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC

@given('Open CureSkin Page')
def open_cureskin_page(context):
    context.app.main_page.open_main_url()


@given('Close pop-up displayed')
def close_mainpage_popup(context):
    # headless mode and Firefox -sleep
    # sleep(5)
    context.app.main_page.close_main_popup()


@when('Click on CureSkin search icon')
def click_search_icon(context):
    # headless mode and Firefox -sleep
    # sleep(5)
    context.app.header_cure.click_cure_search_icon()


@when('Enter {text} in search box')
def enter_search_text(context, text):
    # headless mode
    # sleep(20)
    context.app.header_cure.enter_search_text(text)


@when('Click on Search For button')
def click_search_for_button(context):
    # headless mode and Firefox -sleep
    # sleep(5)
    context.app.header_cure.click_search_for_button()


