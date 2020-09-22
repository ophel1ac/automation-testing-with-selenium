from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")


class MainPageLocators:
    pass


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REG_FROM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    BASKET_TOTAL = (By.CSS_SELECTOR, ".alertinner p strong")
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "#add_to_basket_form [type='submit']")
    CONFIRM_ADDING = (By.CSS_SELECTOR, ".alertinner strong")
    BOOK_TITLE = (By.CSS_SELECTOR, ".product_main h1")
    BOOK_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
