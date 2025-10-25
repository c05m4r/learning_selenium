from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.product_sort_select = driver.find_element(
            By.CLASS_NAME, "product_sort_container"
        )
        self.inventory_items = driver.find_elements(By.CLASS_NAME, "inventory_item")

    def sort_products(self, sort_option: str):
        select = Select(self.product_sort_select)
        # select.select_by_visible_text(sort_option)
        select.select_by_value(sort_option)

    def get_product_prices(self) -> list[float]:
        price_elements = self.driver.find_elements(
            By.CSS_SELECTOR, "[data-test='inventory-item-price']"
        )
        return [float(price.text.replace("$", "").strip()) for price in price_elements]

    def add_all_products_to_cart(self) -> list[str]:
        items = self.inventory_items
        product_names: list[str] = []
        for item in items:
            name = item.find_element(By.CLASS_NAME, "inventory_item_name").text
            add_button = item.find_element(
                By.CSS_SELECTOR, "button[data-test^='add-to-cart']"
            )
            add_button.click()
            product_names.append(name)
        return product_names

    def add_first_product_to_cart(self) -> str:
        item = self.driver.find_element(By.CSS_SELECTOR, ".inventory_item")
        name = item.find_element(By.CLASS_NAME, "inventory_item_name").text
        add_button = item.find_element(
            By.CSS_SELECTOR, "button[data-test^='add-to-cart']"
        )
        add_button.click()
        return name

    def add_two_products_to_cart(self) -> list[str]:
        items = self.driver.find_elements(By.CSS_SELECTOR, ".inventory_item")
        selected_names: list[str] = []
        for item in items[:2]:
            name = item.find_element(By.CLASS_NAME, "inventory_item_name").text
            add_button = item.find_element(
                By.CSS_SELECTOR, "button[data-test^='add-to-cart']"
            )
            add_button.click()
            selected_names.append(name)
        return selected_names

    def open_cart(self) -> None:
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
