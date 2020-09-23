from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_not_be_products(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEM), \
            "There should be no items in the basket, but they are"

    def should_be_message(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY_MESSAGE), \
            "There should be an empty cart message"
