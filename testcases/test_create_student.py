import time
from dotenv import load_dotenv
import os

from pages.student_page import StudentPage
from pages.login_page import LoginPage

load_dotenv()


def _login_and_go(driver):
    """Helper: login kore StudentPage return kore"""
    base_url = os.getenv("BASE_URL")
    username = os.getenv("SITE_USERNAME")
    password = os.getenv("SITE_PASSWORD")
    driver.get(base_url)

    login_page = LoginPage(driver)
    login_page.login(username, password)
    time.sleep(2)

    return StudentPage(driver)


def test_view_added_student_information(driver):
    student_page = _login_and_go(driver)

    added_student = student_page.add_student()
    print("Added Student Data: ", added_student)

    student_page.search_by_name(added_student["name"])
    student_page.click_filter_button()

    viewed_student = student_page.click_view_button_and_get_data()
    print("Viewed Student Data: ", viewed_student)

    assert viewed_student["name"] == added_student["name"]
    assert viewed_student["email"] == added_student["email"]
    assert viewed_student["department"] == added_student["department"]
    assert viewed_student["registration_id"] == added_student["registration_id"]
    assert viewed_student["age"] == added_student["age"]

    print("Student information matched successfully")


def test_create_student_with_empty_form(driver):
    student_page = _login_and_go(driver)

    student_page.open_add_student_modal()
    # Kono field fill na kore directly Create click
    student_page.click_create_button()

    assert student_page.is_modal_still_open(), "Empty form submit howa uchit na!"
    print("Empty form validation working correctly")


def test_create_student_with_invalid_email(driver):
    student_page = _login_and_go(driver)

    student_page.open_add_student_modal()
    student_page.fill_student_form(
        name="Test Student",
        email="invalidemail123",  # invalid email
        select_department=True,
        reg_id="123456",
        age="22"
    )
    student_page.click_create_button()

    assert student_page.is_modal_still_open(), "Invalid email accept howa uchit na!"
    print("Invalid email validation working correctly")


def test_create_student_with_duplicate_email(driver):
    student_page = _login_and_go(driver)

    # First student add koro
    first_student = student_page.add_student()
    print("First student added:", first_student)
    time.sleep(1)

    # Same email diye second student add korar cheshta
    student_page.open_add_student_modal()
    student_page.fill_student_form(
        name="Duplicate Student",
        email=first_student["email"],  # same email
        select_department=True,
        reg_id="999999",
        age="22"
    )
    student_page.click_create_button()

    assert student_page.is_modal_still_open(), "Duplicate email accept howa uchit na!"
    print("Duplicate email validation working correctly")