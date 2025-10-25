from selenium.webdriver.common.by import By


class CheckoutCompletePage:
    def __init__(self, driver):
        self.driver = driver

    def get_complete_message(self) -> str:
        return self.driver.find_element(By.CLASS_NAME, "complete-header").text
