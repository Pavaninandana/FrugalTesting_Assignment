from decimal import Decimal

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.checkout_overview_page import CheckoutOverviewPage
from pages.confirmation_page import ConfirmationPage


def test_complete_checkout(driver):

    # Step 1: Login
    login = LoginPage(driver)
    login.open()
    login.login("standard_user", "secret_sauce")

    # Step 2: Add two products
    inventory = InventoryPage(driver)
    inventory.add_two_products()

    assert inventory.get_cart_count() == "2"

    # Step 3: Open cart
    inventory.open_cart()

    # Step 4: Proceed to checkout
    cart = CartPage(driver)
    cart.click_checkout()

    # Step 5: Enter customer details
    checkout = CheckoutPage(driver)

    checkout.enter_checkout_details(
        "Sai",
        "Revanth",
        "500032"
    )

    checkout.click_continue()

    # Step 6: Read price details
    overview = CheckoutOverviewPage(driver)

    item_total = Decimal(
        overview.get_item_total().split("$")[1]
    )

    tax = Decimal(
        overview.get_tax().split("$")[1]
    )

    total = Decimal(
        overview.get_total().split("$")[1]
    )

    # Step 7: Verify total calculation
    assert total == item_total + tax

    # Step 8: Finish order
    overview.finish_order()

    # Step 9: Verify confirmation
    confirmation = ConfirmationPage(driver)

    assert confirmation.get_confirmation_message() == (
        "Thank you for your order!"
    ) 