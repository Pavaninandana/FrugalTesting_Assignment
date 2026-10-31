from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutOverviewPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    item_total = (By.CLASS_NAME, "summary_subtotal_label")
    tax = (By.CLASS_NAME, "summary_tax_label")
    total = (By.CLASS_NAME, "summary_total_label")
    finish_button = (By.ID, "finish")

    def get_item_total(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.item_total)
        ).text

    def get_tax(self):
        return self.driver.find_element(*self.tax).text

    def get_total(self):
        return self.driver.find_element(*self.total).text

    def finish_order(self):
        self.wait.until(
            EC.element_to_be_clickable(self.finish_button)
        ).click() 