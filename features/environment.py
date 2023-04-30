from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from app.application import Application


def browser_init(context):
    """
    :param context: Behave context
    """
    # context.driver = webdriver.Chrome(executable_path=r"C:\Users\shekh\OneDrive\Desktop\Vibha\AutoCure\chromedriver_win32\chromedriver.exe")
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
