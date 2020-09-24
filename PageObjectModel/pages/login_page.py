from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, \
            "Current page is not a login page"

    def should_be_login_form(self):
        assert self.browser.find_element(*LoginPageLocators.LOGIN_FORM), \
            "There is no login form"

    def should_be_register_form(self):
        assert self.browser.find_element(*LoginPageLocators.REG_FROM), \
            "There is no registration form"

    def register_new_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.REG_EMAIL).send_keys(email)
        self.browser.find_element(*LoginPageLocators.REG_PASSWORD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REG_CONF_PASSWORD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REG_BUTTON).click()