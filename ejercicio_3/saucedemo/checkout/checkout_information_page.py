from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


class CheckoutInformationPage:
    def __init__(self, driver):
        self.driver = driver
        self.first_name_input = driver.find_element(By.ID, "first-name")
        self.last_name_input = driver.find_element(By.ID, "last-name")
        self.postal_code_input = driver.find_element(By.ID, "postal-code")
        self.continue_button = driver.find_element(By.ID, "continue")

    def enter_first_name(self, value: str) -> None:
        self.first_name_input.clear()
        self.first_name_input.send_keys(value)

    def enter_last_name(self, value: str) -> None:
        self.last_name_input.clear()
        self.last_name_input.send_keys(value)

    def enter_postal_code(self, value: str) -> None:
        self.postal_code_input.clear()
        self.postal_code_input.send_keys(value)

    def click_continue(self) -> None:
        self.continue_button.click()

    def get_error_message(self) -> str:
        try:
            error_container = self.driver.find_element(
                By.CSS_SELECTOR, "[data-test='error']"
            )
            return error_container.text
        except NoSuchElementException as exc:
            raise AssertionError(
                "Expected an error message but none was displayed"
            ) from exc
