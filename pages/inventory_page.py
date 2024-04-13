from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class InventoryPage(BasePage):
    default_inventory_names = []
    default_inventory_prices = []
    actual_ordered_names = []
    actual_ordered_prices = []

    ALL_ADD_TO_CART_BUTTONS = (By.CSS_SELECTOR, ".btn_inventory")
    PRODUCT_SORT_CONTAINER = (By.CSS_SELECTOR, ".product_sort_container")
    ALL_INVENTORY_ITEM_NAMES = (By.CSS_SELECTOR, ".inventory_item_name")
    ALL_INVENTORY_ITEM_PRICES = (By.CSS_SELECTOR, ".inventory_item_price")
    IMAGE_SRC = (By.CSS_SELECTOR, "img.inventory_item_img")

    def add_items_to_cart(self, number_of_items):
        add_to_cart_buttons = self.driver.find_elements(*self.ALL_ADD_TO_CART_BUTTONS)
        for i in range(int(number_of_items)):
            add_to_cart_buttons[i].click()
        cart_badge_text = self.find_element(*self.SHOPPING_CART_LINK).text
        assert number_of_items == cart_badge_text, f"\nExpected: {number_of_items}.\nActual: {cart_badge_text}"

    def get_default_data(self):
        self.inventory_names = [item.text for item in self.driver.find_elements(*self.ALL_INVENTORY_ITEM_NAMES)]
        self.inventory_prices = [float(item.text.split('$')[1]) for item in
                            self.driver.find_elements(*self.ALL_INVENTORY_ITEM_PRICES)]

    def select_sort_option(self, sort_option):
        dropdown = Select(self.find_element(*self.PRODUCT_SORT_CONTAINER))
        dropdown.select_by_value(sort_option)
        self.actual_ordered_names = [item.text for item in self.driver.find_elements(*self.ALL_INVENTORY_ITEM_NAMES)]
        self.actual_ordered_prices = [float(price.text.split('$')[1]) for price in self.driver.find_elements(*self.ALL_INVENTORY_ITEM_PRICES)]

    def verify_sort_option(self, sort_option):
        if sort_option == "az":
            expected_order = sorted(self.inventory_names)
            assert expected_order == self.actual_ordered_names,\
                f"Sorting failed for 'az'.\nExpected: {expected_order}.\nActual: {self.actual_ordered_names}."
        elif sort_option == "za":
            expected_order = sorted(self.inventory_names, reverse=True)
            assert expected_order == self.actual_ordered_names,\
                f"Sorting failed for 'za'.\nExpected: {expected_order}.\nActual: {self.actual_ordered_names}."
        elif sort_option == "lohi":
            expected_order = sorted(self.inventory_prices)
            assert expected_order == self.actual_ordered_prices,\
                f"Sorting failed for 'lohi'.\nExpected: {expected_order}.\nActual: {self.actual_ordered_prices}."
        elif sort_option == "hilo":
            expected_order = sorted(self.inventory_prices, reverse=True)
            assert expected_order == self.actual_ordered_prices,\
                f"Sorting failed for 'hilo'.\nExpected: {expected_order}.\nActual: {self.actual_ordered_prices}."

    def validate_images(self):
        image_src = [item.get_attribute('src') for item in self.driver.find_elements(*self.IMAGE_SRC)]
        unique_images = list(set(image_src))
        assert len(unique_images) == len(image_src), f'\nExpected all images to be unique.\nActual: {image_src}.'
