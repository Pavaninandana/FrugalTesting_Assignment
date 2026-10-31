from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


def test_checkout_empty_first_name(driver):

    # Login
    login = LoginPage(driver)
    login.open()
    login.login("standard_user", "secret_sauce")

    # Add products
    inventory = InventoryPage(driver)
    inventory.add_two_products()
    inventory.open_cart()

    # Open checkout
    cart = CartPage(driver)
    cart.click_checkout()

    # Leave first name empty
    checkout = CheckoutPage(driver)

    checkout.enter_checkout_details(
        "",
        "Revanth",
        "500032"
    )

    checkout.click_continue()

    # Verify validation error
    actual_error = checkout.get_error_message()

    assert actual_error == "Error: First Name is required" 