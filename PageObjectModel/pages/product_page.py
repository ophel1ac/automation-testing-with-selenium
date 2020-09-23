from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        basket_button.click()

    def should_be_right_book_added(self):
        book_title = self.browser.find_element(*ProductPageLocators.BOOK_TITLE)
        confirm_message = self.browser.find_element(*ProductPageLocators.CONFIRM_ADDING)
        assert book_title.text == confirm_message.text, \
            "Wrong book added, wrong title." \
            f"\nExpected {book_title.text}, result {confirm_message.text}"

    def should_be_right_book_price(self):
        basket_total = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL)
        book_price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE)
        assert basket_total.text == book_price.text, \
            "Wrong book added, wrong price." \
            f"\nExpected {book_price.text}, result {basket_total.text}"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.CONFIRM_ADDING), \
            "Success message is presented, but should not be"

    def should_disappear_of_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.CONFIRM_ADDING), \
            "Success message should to disappear, but it is present"
