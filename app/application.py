from pages.main_page import MainCurePage
from pages.header_cure import HeaderCureskin
from pages.search_result_page import SearchResultPage
# from pages.sign_in_page import SignInPage
from pages.cart_page import CartPage
#
#
class Application:

    def __init__(self, driver):
        self.driver = driver
        self.main_page = MainCurePage(self.driver)
        self.header_cure = HeaderCureskin(self.driver)
        self.search_result_page = SearchResultPage(self.driver)
#         self.sign_in_page = SignInPage(self.driver)
        self.cart_page = CartPage(self.driver)
