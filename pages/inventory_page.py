from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InventoryPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    backpack = (By.ID, "add-to-cart-sauce-labs-backpack")
    bike_light = (By.ID, "add-to-cart-sauce-labs-bike-light")
    cart_badge = (By.CLASS_NAME, "shopping_cart_badge")
    cart_icon = (By.CLASS_NAME, "shopping_cart_link")

    def add_two_products(self):

        self.wait.until(
            EC.element_to_be_clickable(self.backpack)
        ).click()

        self.wait.until(
            EC.element_to_be_clickable(self.bike_light)
        ).click()

    def get_cart_count(self):

        return self.wait.until(
            EC.visibility_of_element_located(self.cart_badge)
        ).text

    def open_cart(self):

        self.driver.find_element(*self.cart_icon).click() 