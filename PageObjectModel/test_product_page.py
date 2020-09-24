import time
import pytest
import faker

from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage


product_link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/?promo=newYear"
link_to_login = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"


@pytest.mark.authorized_user
class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        print("\nOpen login page")
        login_page = LoginPage(browser, link_to_login)
        login_page.open()
        print("\nStart new_user registration")
        f = faker.Faker()
        email = f.email()
        password = str(time.time())
        login_page.register_new_user(email, password)
        print("\nShould be authorized user")
        login_page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, product_link)
        page.open()
        page.should_not_be_success_message()

    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, product_link)
        page.open()
        page.add_to_basket()
        page.solve_quiz_and_get_code()
        page.should_be_right_book_added()
        page.should_be_right_book_price()


@pytest.mark.parametrize('url', ["?promo=offer0",
                                 "?promo=offer1",
                                 "?promo=offer2",
                                 "?promo=offer3",
                                 "?promo=offer4",
                                 "?promo=offer5",
                                 "?promo=offer6",
                                 pytest.param("?promo=offer7", marks=pytest.mark.xfail),
                                 "?promo=offer8",
                                 "?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, url):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/{url}"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_right_book_added()
    page.should_be_right_book_price()


@pytest.mark.success_message
@pytest.mark.xfail(reason="success message should appear after adding to basket")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.should_not_be_success_message()


@pytest.mark.success_message
def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.success_message
@pytest.mark.xfail(reason="message should not disappear")
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.should_disappear_of_success_message()


@pytest.mark.login_guest
def test_quest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.login_guest
def test_quest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    page.should_be_login_link()


@pytest.mark.basket
def test_quest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_products()
    basket_page.should_be_message()
