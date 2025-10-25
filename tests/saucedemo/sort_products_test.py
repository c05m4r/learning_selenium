import pytest

from helpers.ddt import DDTHelper
from pages.saucedemo.login.login_page import LoginPage
from pages.saucedemo.inventory.inventory_page import InventoryPage

DATA_PATH = "data/saucedemo/data.json"
ddt = DDTHelper(DATA_PATH)
data = ddt.get_json_data_by_testid("tc1")


@pytest.mark.saucedemo
@pytest.mark.tc1
@pytest.mark.parametrize("case", data)
def test_sort_products(case, driver):
    base_url = case["base_url"]
    username = case["username"]
    password = case["password"]
    sort_option = case["sort_option"]
    dashboard_title = case["dashboard_title"]

    driver.get(base_url)

    login_page = LoginPage(driver)
    login_page.login(username, password)

    assert driver.title == dashboard_title

    inventory_page = InventoryPage(driver)
    inventory_page.sort_products(sort_option)
    prices = inventory_page.get_product_prices()

    assert prices == sorted(prices)
