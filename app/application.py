from pages.base_page import BasePage
from pages.main_page import MainPage
from pages.cart_page import CartPage
from pages.inventory_page import InventoryPage


class Application:

    def __init__(self, driver):
        self.base_page = BasePage(driver)
        self.main_page = MainPage(driver)
        self.cart_page = CartPage(driver)
        self.inventory_page = InventoryPage(driver)