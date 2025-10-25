from selenium.webdriver.common.by import By


class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.items = self.driver.find_elements(By.CLASS_NAME, "inventory_item_name")
        self.continue_button = self.driver.find_element(By.ID, "continue-shopping")

    def get_cart_item_names(self) -> list[str]:
        cart_items = self.driver.find_elements(By.CLASS_NAME, "cart_item")
        return [
            item.find_element(By.CLASS_NAME, "inventory_item_name").text
            for item in cart_items
        ]

    def proceed_to_checkout(self) -> None:
        self.driver.find_element(By.ID, "checkout").click()

    def remove_item_by_name(self, product_name: str) -> None:
        cart_items = self.driver.find_elements(By.CLASS_NAME, "cart_item")
        for cart_item in cart_items:
            name = cart_item.find_element(By.CLASS_NAME, "inventory_item_name").text
            if name == product_name:
                cart_item.find_element(
                    By.CSS_SELECTOR, "button[data-test^='remove']"
                ).click()
                return
        raise AssertionError(f"Product '{product_name}' not found in cart")

    def continue_shopping(self) -> None:
        self.continue_button.click()
