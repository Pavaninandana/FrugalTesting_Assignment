
import pytest
import csv
from pathlib import Path
from pages.login_page import LoginPage


# Read test data from CSV
def load_login_data():

    csv_path = (
        Path(__file__).resolve().parents[1]
        / "test_data"
        / "login_data.csv"
    )

    with open(csv_path, mode="r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        return [
            (
                row["username"],
                row["password"],
                row["expected_error"]
            )
            for row in reader
        ]


@pytest.mark.parametrize(
    "username, password, expected_error",
    load_login_data()
)
def test_invalid_login(driver, username, password, expected_error):

    login_page = LoginPage(driver)

    login_page.open()

    login_page.login(username, password)

    actual_error = login_page.get_error_message()

    assert actual_error == expected_error
