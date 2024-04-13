from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class MainPage(BasePage):
    USERNAME_FIELD = (By.CSS_SELECTOR, '#user-name')
    PASSWORD_FIELD = (By.CSS_SELECTOR, '#password')
    LOGIN_BUTTON = (By.CSS_SELECTOR, '#login-button')
    ERROR_MESSAGE = (By.CSS_SELECTOR, '.error-message-container.error')
    PASSWORD = 'secret_sauce'

    def login_as(self, user):
        self.input_text(user, *self.USERNAME_FIELD)
        self.input_text(self.PASSWORD, *self.PASSWORD_FIELD)
        self.click(*self.LOGIN_BUTTON)

    def verify_login_button(self):
        self.wait_for_visible_element(*self.LOGIN_BUTTON)

    def verify_error_message(self, error_message):
        self.verify_text(error_message, *self.ERROR_MESSAGE)
