from pages.base_page import BasePage
from pages.cart_page import CartPage
from pages.header import Header
from pages.inventory_page import InventoryPage
from pages.main_page import MainPage


class Application:

    def __init__(self, driver):
        self.base_page = BasePage(driver)
        self.cart_page = CartPage(driver)
        self.header = Header(driver)
        self.inventory_page = InventoryPage(driver)
        self.main_page = MainPage(driver)
