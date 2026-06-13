from pages.login_page import LoginPage
from dotenv import load_dotenv
import os
load_dotenv()


def test_login_success(driver):
    base_url = os.getenv("BASE_URL")
    username = os.getenv("SITE_USERNAME")
    password = os.getenv("SITE_PASSWORD")
    driver.get(base_url)

    login_page = LoginPage(driver)
    login_page.login(username, password)

    assert login_page.is_login_successful() == True, "Login failed!"


def test_login_with_wrong_password(driver):
    base_url = os.getenv("BASE_URL")
    username = os.getenv("SITE_USERNAME")
    driver.get(base_url)

    login_page = LoginPage(driver)
    login_page.login(username, "wrongpassword999")

    assert login_page.is_login_successful() == False, "Login should have failed with wrong password!"


def test_login_with_empty_credentials(driver):
    base_url = os.getenv("BASE_URL")
    driver.get(base_url)

    login_page = LoginPage(driver)
    login_page.login("", "")

    assert login_page.is_login_successful() == False, "Login should have failed with empty credentials!"
