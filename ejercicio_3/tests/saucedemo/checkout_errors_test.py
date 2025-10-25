import pytest

from helpers.ddt import DDTHelper
from pages.saucedemo.cart.cart_page import CartPage
from pages.saucedemo.checkout.checkout_information_page import CheckoutInformationPage
from pages.saucedemo.inventory.inventory_page import InventoryPage
from pages.saucedemo.login.login_page import LoginPage

DATA_PATH = "data/saucedemo/data.json"
ddt = DDTHelper(DATA_PATH)
data = ddt.get_json_data_by_testid("tc2")


@pytest.mark.saucedemo
@pytest.mark.tc2
@pytest.mark.parametrize("case", data)
def test_checkout_missing_fields(case, driver):
    base_url = case["base_url"]
    username = case["username"]
    password = case["password"]
    dashboard_title = case["dashboard_title"]
    first_name = case["first_name"]
    last_name = case["last_name"]
    expected_last_name_error = case["expected_last_name_error"]
    expected_postal_code_error = case["expected_postal_code_error"]

    driver.get(base_url)

    login_page = LoginPage(driver)
    login_page.login(username, password)

    assert driver.title == dashboard_title

    inventory_page = InventoryPage(driver)
    added_products = inventory_page.add_all_products_to_cart()
    assert added_products

    inventory_page.open_cart()

    cart_page = CartPage(driver)
    cart_items = cart_page.get_cart_item_names()
    assert len(cart_items) == len(added_products)
    assert sorted(cart_items) == sorted(added_products)

    cart_page.proceed_to_checkout()

    checkout_page = CheckoutInformationPage(driver)
    checkout_page.enter_first_name(first_name)
    checkout_page.click_continue()
    assert checkout_page.get_error_message() == expected_last_name_error

    checkout_page.enter_last_name(last_name)
    checkout_page.click_continue()
    assert checkout_page.get_error_message() == expected_postal_code_error
