def test_open_saucedemo(driver):
    driver.get("https://www.saucedemo.com")

    assert "Swag Labs" in driver.title

    print("SauceDemo website opened successfully!")