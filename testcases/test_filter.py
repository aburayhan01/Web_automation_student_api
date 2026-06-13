import random
import time
from dotenv import load_dotenv
import os

from pages.login_page import LoginPage
from pages.student_page import StudentPage


def test_department_filter(driver):
    base_url = os.getenv("BASE_URL")
    username = os.getenv("SITE_USERNAME")
    password = os.getenv("SITE_PASSWORD")
    driver.get(base_url)

    login_page = LoginPage(driver)
    student_page = StudentPage(driver)

    login_page.login(username, password)




    assert login_page.is_login_successful(), "Login failed!"

    student_page.select_page_size("100")
    time.sleep(2)

    selected_department = student_page.select_random_department_from_filter()
    print(f"selected_department: {selected_department}")

    student_page.click_filter_button()
    time.sleep(2)

    print("Table data",student_page.get_table_data_as_a_dictionary())


    while True:
        table_data = student_page.get_table_data_as_a_dictionary()

        for row in table_data:
            actual_department = row["department"]

            print(
                f"Expected: {selected_department} |"
                f"Actual: {actual_department}"
            )

            assert actual_department == selected_department,(
                f"Department mismatch"
                f"Expected: {selected_department},"
                f"Found: {actual_department}"
            )

        has_next = student_page.click_next_page()

        if has_next == "disabled":
            print("Reached last page")
            break


def test_search_by_name_filter(driver):
    base_url = os.getenv("BASE_URL")
    username = os.getenv("SITE_USERNAME")
    password = os.getenv("SITE_PASSWORD")
    driver.get(base_url)

    login_page = LoginPage(driver)
    student_page = StudentPage(driver)

    login_page.login(username, password)

    time.sleep(3)

    all_students = student_page.get_table_data_as_a_dictionary()
    random_student = random.choice(all_students)


    search_name = random_student["name"]
    print(f"Searching for: {search_name}")

    student_page.search_by_name(search_name)
    student_page.click_filter_button()
    time.sleep(2)

    filtered_student = student_page.get_table_data_as_a_dictionary()

    for student in filtered_student:
        assert search_name.lower() in student["name"].lower(),(
            f" {search_name}, not found in {student['name']}"
        )
    print("name filter working correctly")






















