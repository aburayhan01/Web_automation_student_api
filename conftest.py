import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


@pytest.fixture
def driver():
    service = Service(ChromeDriverManager().install())
    driver_instance = webdriver.Chrome(service=service)
    driver_instance.maximize_window()

    yield driver_instance

    driver_instance.quit()