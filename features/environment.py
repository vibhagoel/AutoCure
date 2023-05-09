import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from app.application import Application



def browser_init(context):
    """
    :param context: Behave context
    """
     #context.driver = webdriver.Chrome(executable_path=r"C:\Users\shekh\OneDrive\Desktop\Vibha\AutoCure\chromedriver_win32\chromedriver.exe")
    # For chrome
    service = Service(r'C:\Users\shekh\OneDrive\Desktop\Vibha\AutoCure\chromedriver_win32\chromedriver.exe')
    # For Firefox
    #service = Service(r'C:\Users\shekh\OneDrive\Desktop\Vibha\AutoCure\geckodriver-v0.33.0-win32.geckodriver.exe')
    ## HEADLESS MODE ####
    # options = webdriver.ChromeOptions()
    # # options.add_argument('start-maximized')
    # # options.add_argument("--window-size=1600*900")
    # options.add_argument('--headless')
    # context.driver = webdriver.Chrome(
    #     chrome_options=options,
    #     service=service
    # )

    context.driver = webdriver.Chrome(service=service)
    # context.driver = webdriver.Safari()
    # context.driver = webdriver.Firefox(service=service)

    context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.driver.wait = WebDriverWait(context.driver, 10)
    context.app = Application(driver=context.driver)


 # for browerstack ###
    # Register for BrowserStack, then grab it from https://www.browserstack.com/accounts/settings
    # bs_user = 'vibhagoel_0cU5fF'
    # bs_key = '2qjSUtPuqZkBXpSM3KSc'
    #
    # desired_cap = {
    #     'browserName': 'Firefox',
    #     'bstack:options': {
    #         'os': 'Windows',
    #         'osVersion': '10',
    #         'sessionName': test_name
    #     }
    # }
    # url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'
    # context.driver = webdriver.Remote(url, desired_capabilities=desired_cap)
    #
    # context.driver.maximize_window()
    # context.driver.implicitly_wait(5)
    # context.driver.wait = WebDriverWait(context.driver, 10)
    #
    # context.app = Application(context.driver)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()
