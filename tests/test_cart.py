from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage


def test_add_two_products_to_cart(driver):

    # Login
    login = LoginPage(driver)
    login.open()
    login.login("standard_user", "secret_sauce")

    # Add products
    inventory = InventoryPage(driver)
    inventory.add_two_products()

    # Verify cart badge
    assert inventory.get_cart_count() == "2"

    # Open cart
    inventory.open_cart()

    # Verify product names and prices
    cart = CartPage(driver)

    assert cart.get_product_names() == [
        "Sauce Labs Backpack",
        "Sauce Labs Bike Light"
    ]

    assert cart.get_product_prices() == [
        "$29.99",
        "$9.99"
    ] 