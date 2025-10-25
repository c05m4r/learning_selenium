from selenium.webdriver.common.by import By


class CheckoutOverviewPage:
    def __init__(self, driver):
        self.driver = driver

    def finish_purchase(self) -> None:
        finish_button = self.driver.find_element(By.ID, "finish")
        finish_button.click()
