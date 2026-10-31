import os
from datetime import datetime

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    setattr(item, "rep_" + report.when, report)


@pytest.fixture
def driver(request):

    options = Options()
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=options)

    yield driver

    if hasattr(request.node, "rep_call"):
        if request.node.rep_call.failed:

            os.makedirs("screenshots", exist_ok=True)

            filename = datetime.now().strftime(
                "failure_%Y%m%d_%H%M%S.png"
            )

            driver.save_screenshot(
                os.path.join("screenshots", filename)
            )

            print(f"Screenshot saved: {filename}")

    driver.quit() 