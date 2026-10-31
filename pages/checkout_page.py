from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    first_name = (By.ID, "first-name")
    last_name = (By.ID, "last-name")
    postal_code = (By.ID, "postal-code")
    continue_button = (By.ID, "continue")
    error_message = (By.CSS_SELECTOR, "[data-test='error']")

    def enter_checkout_details(self, first, last, postal):

        self.wait.until(
            EC.visibility_of_element_located(self.first_name)
        ).send_keys(first)

        self.driver.find_element(*self.last_name).send_keys(last)

        self.driver.find_element(*self.postal_code).send_keys(postal)

    def click_continue(self):

        self.wait.until(
            EC.element_to_be_clickable(self.continue_button)
        ).click()

    def get_error_message(self):

        return self.wait.until(
            EC.visibility_of_element_located(self.error_message)
        ).text 