import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="session")
def browser_open():
    options=Options()
    driver=webdriver.Chrome(options=options)
    driver.get("https://nitka.com/")
    yield driver
    driver.quit()