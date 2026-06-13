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


def test_delete_student(driver):
    student_page = _login_and_go(driver)

    # Prothome student add koro
    added_student = student_page.add_student()
    print("Added student:", added_student)

    # Name diye search koro
    student_page.search_by_name(added_student["name"])
    student_page.click_filter_button()
    time.sleep(1)

    # Delete button click → confirmation modal asbe
    student_page.click_delete_button()

    # Confirm delete
    student_page.confirm_delete()

    # Table e aro nai kina check
    student_page.search_by_name(added_student["name"])
    student_page.click_filter_button()
    time.sleep(1)

    assert not student_page.is_student_in_table(added_student["name"]), \
        f"Student '{added_student['name']}' should have been deleted!"
    print(f"Student deleted successfully: {added_student['name']}")


def test_delete_student_and_verify_gone(driver):
    student_page = _login_and_go(driver)

    # Prothome student add koro
    added_student = student_page.add_student()
    print("Added student:", added_student)

    # Delete er age table e ache kina verify
    student_page.search_by_name(added_student["name"])
    student_page.click_filter_button()
    time.sleep(1)

    assert student_page.is_student_in_table(added_student["name"]), \
        f"Student '{added_student['name']}' should exist before delete!"
    print("Student exists before delete — confirmed")

    # Delete koro
    student_page.click_delete_button()
    student_page.confirm_delete()

    # Delete er pore table e nai kina verify
    student_page.search_by_name(added_student["name"])
    student_page.click_filter_button()
    time.sleep(1)

    assert not student_page.is_student_in_table(added_student["name"]), \
        f"Student '{added_student['name']}' should not exist after delete!"
    print("Student does not exist after delete — confirmed")