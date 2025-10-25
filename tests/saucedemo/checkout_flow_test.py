import pdb
import pytest

from helpers.ddt import DDTHelper
from pages.saucedemo.cart.cart_page import CartPage
from pages.saucedemo.checkout.checkout_information_page import CheckoutInformationPage
from pages.saucedemo.checkout.complete.checkout_complete_page import (
    CheckoutCompletePage,
)
from pages.saucedemo.checkout.overview.checkout_overview_page import (
    CheckoutOverviewPage,
)
from pages.saucedemo.inventory.inventory_page import InventoryPage
from pages.saucedemo.login.login_page import LoginPage

DATA_PATH = "data/saucedemo/data.json"
ddt = DDTHelper(DATA_PATH)
data = ddt.get_json_data_by_testid("tc3")


@pytest.mark.saucedemo
@pytest.mark.tc3
@pytest.mark.parametrize("case", data)
def test_checkout_flow(case, driver):
    base_url = case["base_url"]
    username = case["username"]
    password = case["password"]
    dashboard_title = case["dashboard_title"]
    first_name = case["first_name"]
    last_name = case["last_name"]
    postal_code = case["postal_code"]
    expected_complete_message = case["expected_complete_message"]

    driver.get(base_url)

    login_page = LoginPage(driver)
    login_page.login(username, password)

    assert driver.title == dashboard_title

    inventory_page = InventoryPage(driver)
    first_product = inventory_page.add_first_product_to_cart()
    assert first_product

    inventory_page.open_cart()

    cart_page = CartPage(driver)
    cart_items = cart_page.get_cart_item_names()
    assert first_product in cart_items

    cart_page.remove_item_by_name(first_product)

    cart_page.continue_shopping()

    second_wave_products = inventory_page.add_two_products_to_cart()
    assert len(second_wave_products) == 2

    inventory_page.open_cart()
    cart_items = cart_page.get_cart_item_names()
    assert sorted(cart_items) == sorted(second_wave_products)

    cart_page.proceed_to_checkout()

    checkout_page = CheckoutInformationPage(driver)
    checkout_page.enter_first_name(first_name)
    checkout_page.enter_last_name(last_name)
    checkout_page.enter_postal_code(postal_code)
    checkout_page.click_continue()

    overview_page = CheckoutOverviewPage(driver)
    overview_page.finish_purchase()

    complete_page = CheckoutCompletePage(driver)
    assert complete_page.get_complete_message() == expected_complete_message
