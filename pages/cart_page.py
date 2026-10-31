from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    cart_items = (By.CLASS_NAME, "cart_item")
    item_names = (By.CLASS_NAME, "inventory_item_name")
    item_prices = (By.CLASS_NAME, "inventory_item_price")
    checkout_button = (By.ID, "checkout")

    def get_product_names(self):
        items = self.wait.until(
            EC.visibility_of_all_elements_located(self.item_names)
        )
        return [item.text for item in items]

    def get_product_prices(self):
        items = self.wait.until(
            EC.visibility_of_all_elements_located(self.item_prices)
        )
        return [item.text for item in items] 
    def click_checkout(self):
        self.wait.until(
            EC.element_to_be_clickable(self.checkout_button)
        ).click()  