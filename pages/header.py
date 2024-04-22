from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class Header(BasePage):
    BURGER_MENU_BUTTON = (By.CSS_SELECTOR, "#react-burger-menu-btn")
    LOGOUT_SIDE_BAR_LINK = (By.CSS_SELECTOR, "#logout_sidebar_link")
    SHOPPING_CART_LINK = (By.CSS_SELECTOR, ".shopping_cart_badge")

    def log_out(self):
        self.click(*self.BURGER_MENU_BUTTON)
        self.wait_for_clickable_element_and_click(*self.LOGOUT_SIDE_BAR_LINK)

    def click_shopping_cart_icon(self):
        self.click(*self.SHOPPING_CART_LINK)
