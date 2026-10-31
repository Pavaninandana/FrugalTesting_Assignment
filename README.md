# FrugalTesting Assignment – Selenium Automation Framework

## Project Overview
This project automates the login, product selection, cart, and checkout workflows of the SauceDemo web application using Python, Selenium WebDriver, and pytest.

## Technologies Used
- Python 3.12
- Selenium WebDriver
- pytest
- pytest-html
- CSV for test data management
- Page Object Model (POM)

## Project Structure
```text
FrugalTesting_Assignment/
│
├── pages/
│   ├── login_page.py
│   ├── inventory_page.py
│   ├── cart_page.py
│   ├── checkout_page.py
│   ├── checkout_overview_page.py
│   └── confirmation_page.py
│
├── tests/
│   ├── test_browser.py
│   ├── test_login.py
│   ├── test_login_negative.py
│   ├── test_cart.py
│   ├── test_checkout.py
│   └── test_checkout_negative.py
│
├── test_data/
│   └── login_data.csv
│
├── screenshots/
├── conftest.py
├── report.html
└── README.md
```

## Automated Test Scenarios
1. Verify that the browser opens successfully.
2. Verify successful login with valid credentials.
3. Verify invalid login with incorrect credentials.
4. Verify login for a locked-out user.
5. Verify adding products to the shopping cart.
6. Verify the checkout process and order confirmation.
7. Verify checkout validation when the first name is empty.

## Key Features
- Page Object Model for better code organization.
- Data-driven negative login testing using CSV.
- Automated browser testing using Selenium.
- Test execution and assertions using pytest.
- Automatic screenshot capture when a test fails.
- HTML test report generation.

## Installation and Setup

### 1. Clone the repository
```bash
git clone <your-github-repository-url>
cd FrugalTesting_Assignment
```

### 2. Create a virtual environment
```bash
python -m venv venv
```

### 3. Activate the virtual environment

Windows PowerShell:
```powershell
.\venv\Scripts\Activate.ps1
```

### 4. Install dependencies
```bash
python -m pip install selenium pytest pytest-html
```

## Run Tests

Run the complete test suite:
```bash
python -m pytest tests/ -v
```

Generate an HTML test report:
```bash
python -m pytest tests/ -v --html=report.html --self-contained-html
```

Open `report.html` in a browser to view the test execution results.

## Test Results
- Total test cases: 7
- Passed: 7
- Failed: 0
- Skipped: 0

## Application Under Test
SauceDemo: https://www.saucedemo.com/

## Author
Pavani Nandana