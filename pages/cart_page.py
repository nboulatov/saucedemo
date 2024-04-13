from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CartPage(BasePage):
    CART_QUANTITY = (By.CSS_SELECTOR, ".cart_quantity")
    CHECKOUT_BUTTON = (By.CSS_SELECTOR, "#checkout")

    def verify_cart_items(self, number_of_items):
        cart_quantity = [int(item.text) for item in self.driver.find_elements(*self.CART_QUANTITY)]
        assert sum(cart_quantity) == int(number_of_items),\
            f"\nExpected: {number_of_items}.\nActual: {sum(cart_quantity)}."

    def click_checkout_button(self, button):
        self.click(*self.CHECKOUT_BUTTON)
