import time
from dotenv import load_dotenv
import os

from pages.student_page import StudentPage
from pages.login_page import LoginPage

load_dotenv()


def _login_and_go(driver):
    base_url = os.getenv("BASE_URL")
    username = os.getenv("SITE_USERNAME")
    password = os.getenv("SITE_PASSWORD")
    driver.get(base_url)

    login_page = LoginPage(driver)
    login_page.login(username, password)
    time.sleep(2)

    return StudentPage(driver)


def test_update_student(driver):
    student_page = _login_and_go(driver)

    # Prothome student add koro
    added_student = student_page.add_student()
    print("Added student:", added_student)

    # Name diye search koro
    student_page.search_by_name(added_student["name"])
    student_page.click_filter_button()
    time.sleep(1)

    # Edit button click
    student_page.click_edit_button()

    # Pre-filled name check
    prefilled_name = student_page.get_edit_modal_prefilled_name()
    assert prefilled_name == added_student["name"], \
        f"Pre-filled name mismatch! Expected: {added_student['name']}, Got: {prefilled_name}"
    print(f"Pre-filled name matched: {prefilled_name}")

    # Name update koro
    new_name = "Updated Student Name"
    student_page.clear_and_update_name(new_name)

    # Age update koro
    new_age = "25"
    student_page.clear_and_update_age(new_age)

    # Update button click
    student_page.click_update_button()

    # Updated name diye search koro
    student_page.search_by_name(new_name)
    student_page.click_filter_button()
    time.sleep(1)

    # Table e updated name ache kina check
    assert student_page.is_student_in_table(new_name), \
        f"Updated student '{new_name}' not found in table!"
    print(f"Student updated successfully: {new_name}")


def test_update_student_with_empty_name(driver):
    student_page = _login_and_go(driver)

    # Prothome student add koro
    added_student = student_page.add_student()
    print("Added student:", added_student)

    # Name diye search koro
    student_page.search_by_name(added_student["name"])
    student_page.click_filter_button()
    time.sleep(1)

    # Edit button click
    student_page.click_edit_button()

    # Name field clear kore khali rakho
    student_page.clear_and_update_name("")

    # Update button click
    student_page.driver.find_element(*student_page.update_button).click()
    time.sleep(1)

    # Modal ekhono open thakbe
    assert student_page.is_update_modal_still_open(), \
        "Empty name diye update howa uchit na!"
    print("Empty name validation working correctly")