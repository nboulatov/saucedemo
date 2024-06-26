from selenium.webdriver.support import  expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage():

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver,10)

    def open(self, url):
        self.driver.get(url)

    def click(self, *locator):
        self.driver.find_element(*locator).click()

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def wait_for_visible_element(self, *locator):
        self.wait.until(EC.visibility_of_element_located(locator), message=f"Element via {locator} is not visible")

    def wait_for_clickable_element(self, *locator):
        self.wait.until(EC.element_to_be_clickable(locator), message=f"Element via {locator} is not clickable")

    def wait_for_clickable_element_and_click(self, *locator):
        self.wait.until(EC.element_to_be_clickable(locator), message=f"Element via {locator} is not clickable").click()

    def input_text(self, text, *locator):
        self.wait.until(
            EC.visibility_of_element_located(locator),
            message=f"Element via {locator} is not visible").send_keys(text)

    def verify_text(self, expected_text, *locator):
        actual_text = self.wait.until(
            EC.visibility_of_element_located(locator),
            message=f"Element via {locator} is not visible").text
        assert expected_text in actual_text, f"\nExpected: {expected_text}.\nActual: {actual_text}."

    def verify_url(self, expected_text_in_url):
        url = self.driver.current_url
        assert expected_text_in_url in url, f'\nExpected: {expected_text_in_url}.\nActual: {url}.'
