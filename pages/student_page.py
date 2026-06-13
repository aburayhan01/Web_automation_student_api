# import random
# import time
# from faker import Faker
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import Select
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.common.exceptions import TimeoutException
#
#
# class StudentPage:
#
#     def __init__(self, driver):
#         self.driver = driver
#         self.wait = WebDriverWait(driver, timeout=10)
#
#     # page size Locator
#     page_size_dropdown = (By.XPATH, "//select")
#
#     # department filter locator
#     department_dropdown_filter = (By.XPATH, "//button[@role='combobox']")
#     dropdown_options = (By.XPATH, "//div[@role='option']")
#
#     # filter button locator
#     filter_button = (By.XPATH, "//button[text()='Filter']")
#
#     # Table data dictionary
#     table_data = (By.XPATH, "//tbody/tr")
#
#     # next button locator
#     next_button = (By.XPATH, "//button[text()='Next']")
#
#     # search by name locator
#     search_name = (By.XPATH, "//input[@placeholder='Filter by name...']")
#
#     # modal locators
#     add_student_button = (By.XPATH, "//button[contains(text(), 'Add Student')]")
#     name_input = (By.XPATH, "//div[label[text()='Name']]//input")
#     email_input = (By.XPATH, "//div[label[text()='Email']]//input")
#     department_dropdown_form = (By.XPATH, "//button[span[text()='Select department']]")
#     registration_input = (By.XPATH, "//div[label[text()='Registration ID']]//input")
#     age_input = (By.XPATH, "//div[label[text()='Age']]//input")
#     create_button = (By.XPATH, "//button[text()='Create']")
#
#     # -------------------------
#     # Existing Methods
#     # -------------------------
#
#     def select_page_size(self, page_size):
#         dropdown = self.wait.until(
#             lambda d: d.find_element(*self.page_size_dropdown)
#         )
#         select = Select(dropdown)
#         select.select_by_visible_text(str(page_size))
#         print(f"Selected page size : {page_size}")
#         time.sleep(5)
#
#     def select_random_department_from_filter(self):
#         self.driver.find_element(*self.department_dropdown_filter).click()
#         time.sleep(1)
#         departments = self.driver.find_elements(*self.dropdown_options)
#         random_department = random.choice(departments)
#         selected_department = random_department.text
#         random_department.click()
#         time.sleep(2)
#         return selected_department
#
#     def click_filter_button(self):
#         filter_btn = WebDriverWait(self.driver, 10).until(
#             EC.presence_of_element_located(self.filter_button)
#         )
#         self.driver.execute_script("arguments[0].click();", filter_btn)
#
#     def get_table_data_as_a_dictionary(self):
#         table_data = []
#         rows = self.driver.find_elements(*self.table_data)
#         for row in rows:
#             columns = row.find_elements(By.XPATH, "./td")
#             row_data = {
#                 "name": columns[0].text,
#                 "email": columns[1].text,
#                 "department": columns[2].text,
#                 "registration_id": columns[3].text,
#                 "age": columns[4].text
#             }
#             table_data.append(row_data)
#         return table_data
#
#     def click_next_page(self):
#         next_btn = self.driver.find_element(*self.next_button)
#         is_disabled = next_btn.get_attribute("disabled")
#         if is_disabled:
#             print("Next button is disabled")
#             return "disabled"
#         next_btn.click()
#         print("Click Next button")
#         time.sleep(1)
#         return "clicked"
#
#     def search_by_name(self, name):
#         input_box = WebDriverWait(self.driver, 10).until(
#             EC.element_to_be_clickable(self.search_name)
#         )
#         ActionChains(self.driver).move_to_element(input_box).click().perform()
#         time.sleep(0.3)
#         input_box.clear()
#         input_box.send_keys(name)
#         time.sleep(1)
#
#         actual_value = input_box.get_attribute("value")
#         print(f"Typed name   : {name}")
#         print(f"Input value  : {actual_value}")
#
#         time.sleep(1)
#         rows = self.driver.find_elements(By.XPATH, "//tbody/tr")
#         print(f"Row count after search: {len(rows)}")
#         for row in rows[:5]:
#             cols = row.find_elements(By.XPATH, "./td")
#             if cols:
#                 print(f"  Row name: {cols[0].text}")
#
#     def add_student(self):
#         fake = Faker()
#
#         student_name = fake.name()
#         student_email = fake.email()
#         registration_id = fake.random_number(digits=6)
#         student_age = random.randint(a=18, b=30)
#
#         add_student_button = self.wait.until(
#             lambda d: d.find_element(*self.add_student_button)
#         )
#         add_student_button.click()
#
#         name_input = self.wait.until(
#             lambda d: d.find_element(*self.name_input)
#         )
#         name_input.send_keys(student_name)
#
#         self.driver.find_element(*self.email_input).send_keys(student_email)
#
#         self.driver.find_element(*self.department_dropdown_form).click()
#         departments = self.wait.until(
#             lambda d: d.find_elements("xpath", "//div//div[@role='option']")
#         )
#         random_department = random.choice(departments)
#         department_name = random_department.text
#         random_department.click()
#
#         self.driver.find_element(*self.registration_input).send_keys(str(registration_id))
#         self.driver.find_element(*self.age_input).send_keys(str(student_age))
#
#         self.driver.find_element(*self.create_button).click()
#
#         WebDriverWait(self.driver, 15).until(
#             EC.visibility_of_element_located(self.add_student_button)
#         )
#
#         return {
#             "name": student_name,
#             "email": student_email,
#             "department": department_name,
#             "registration_id": str(registration_id),
#             "age": str(student_age)
#         }
#
#     def click_view_button_and_get_data(self):
#         view_button = self.wait.until(
#             lambda d: d.find_element(
#                 "xpath", "//button[.//*[contains(@class,'lucide-eye')]]"
#             )
#         )
#         view_button.click()
#
#         name = self.wait.until(
#             lambda d: d.find_element(
#                 "xpath", "//span[text()='Name']/following-sibling::span"
#             )
#         ).text
#         email = self.driver.find_element(
#             "xpath", "//span[text()='Email']/following-sibling::span"
#         ).text
#         department = self.driver.find_element(
#             "xpath", "//span[text()='Department']/following-sibling::span"
#         ).text
#         registration_id = self.driver.find_element(
#             "xpath", "//span[text()='Registration ID']/following-sibling::span"
#         ).text
#         age = self.driver.find_element(
#             "xpath", "//span[text()='Age']/following-sibling::span"
#         ).text
#
#         time.sleep(5)
#
#         student_data = {
#             "name": name,
#             "email": email,
#             "department": department,
#             "registration_id": registration_id,
#             "age": age
#         }
#         print(student_data)
#         return student_data
#
#     # -------------------------
#     # New Methods
#     # -------------------------
#
#     def open_add_student_modal(self):
#         btn = self.wait.until(EC.element_to_be_clickable(self.add_student_button))
#         btn.click()
#         # Create button visible hole modal open hoyece
#         self.wait.until(EC.visibility_of_element_located(self.create_button))
#
#     def fill_student_form(self, name="", email="", select_department=False, reg_id="", age=""):
#         if name:
#             name_field = self.wait.until(EC.visibility_of_element_located(self.name_input))
#             name_field.send_keys(name)
#
#         if email:
#             self.driver.find_element(*self.email_input).send_keys(email)
#
#         if select_department:
#             self.driver.find_element(*self.department_dropdown_form).click()
#             departments = self.wait.until(
#                 lambda d: d.find_elements("xpath", "//div//div[@role='option']")
#             )
#             departments[0].click()
#
#         if reg_id:
#             self.driver.find_element(*self.registration_input).send_keys(reg_id)
#
#         if age:
#             self.driver.find_element(*self.age_input).send_keys(age)
#
#     def click_create_button(self):
#         self.driver.find_element(*self.create_button).click()
#         time.sleep(1)
#
#     def is_modal_still_open(self):
#         try:
#             WebDriverWait(self.driver, 3).until(
#                 EC.visibility_of_element_located(self.create_button)
#             )
#             return True
#         except TimeoutException:
#             return False


import random
import time
from faker import Faker
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException


class StudentPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout=10)

    # page size Locator
    page_size_dropdown = (By.XPATH, "//select")

    # department filter locator
    department_dropdown_filter = (By.XPATH, "//button[@role='combobox']")
    dropdown_options = (By.XPATH, "//div[@role='option']")

    # filter button locator
    filter_button = (By.XPATH, "//button[text()='Filter']")

    # Table data
    table_data = (By.XPATH, "//tbody/tr")

    # next button locator
    next_button = (By.XPATH, "//button[text()='Next']")

    # search by name locator
    search_name = (By.XPATH, "//input[@placeholder='Filter by name...']")

    # Add student modal locators
    add_student_button = (By.XPATH, "//button[contains(text(), 'Add Student')]")
    name_input = (By.XPATH, "//div[label[text()='Name']]//input")
    email_input = (By.XPATH, "//div[label[text()='Email']]//input")
    department_dropdown_form = (By.XPATH, "//button[span[text()='Select department']]")
    registration_input = (By.XPATH, "//div[label[text()='Registration ID']]//input")
    age_input = (By.XPATH, "//div[label[text()='Age']]//input")
    create_button = (By.XPATH, "//button[text()='Create']")

    # Action buttons (table row)
    edit_button = (By.XPATH, "//button[.//*[contains(@class,'lucide-pencil')]]")
    delete_button = (By.XPATH, "//button[.//*[contains(@class,'lucide-trash2')]]")

    # Edit modal locators
    edit_name_input = (By.XPATH, "//div[label[text()='Name']]//input")
    edit_age_input = (By.XPATH, "//div[label[text()='Age']]//input")
    update_button = (By.XPATH, "//button[text()='Update']")
    cancel_button = (By.XPATH, "//button[text()='Cancel']")

    # Delete modal locators
    confirm_delete_button = (By.XPATH, "//button[text()='Delete']")

    # -------------------------
    # Existing Methods
    # -------------------------

    def select_page_size(self, page_size):
        dropdown = self.wait.until(
            lambda d: d.find_element(*self.page_size_dropdown)
        )
        select = Select(dropdown)
        select.select_by_visible_text(str(page_size))
        print(f"Selected page size : {page_size}")
        time.sleep(5)

    def select_random_department_from_filter(self):
        self.driver.find_element(*self.department_dropdown_filter).click()
        time.sleep(1)
        departments = self.driver.find_elements(*self.dropdown_options)
        random_department = random.choice(departments)
        selected_department = random_department.text
        random_department.click()
        time.sleep(2)
        return selected_department

    def click_filter_button(self):
        filter_btn = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.filter_button)
        )
        self.driver.execute_script("arguments[0].click();", filter_btn)

    def get_table_data_as_a_dictionary(self):
        table_data = []
        rows = self.driver.find_elements(*self.table_data)
        for row in rows:
            columns = row.find_elements(By.XPATH, "./td")
            row_data = {
                "name": columns[0].text,
                "email": columns[1].text,
                "department": columns[2].text,
                "registration_id": columns[3].text,
                "age": columns[4].text
            }
            table_data.append(row_data)
        return table_data

    def click_next_page(self):
        next_btn = self.driver.find_element(*self.next_button)
        is_disabled = next_btn.get_attribute("disabled")
        if is_disabled:
            print("Next button is disabled")
            return "disabled"
        next_btn.click()
        print("Click Next button")
        time.sleep(1)
        return "clicked"

    def search_by_name(self, name):
        input_box = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.search_name)
        )
        ActionChains(self.driver).move_to_element(input_box).click().perform()
        time.sleep(0.3)
        input_box.clear()
        input_box.send_keys(name)
        time.sleep(1)

        actual_value = input_box.get_attribute("value")
        print(f"Typed name   : {name}")
        print(f"Input value  : {actual_value}")

        time.sleep(1)
        rows = self.driver.find_elements(By.XPATH, "//tbody/tr")
        print(f"Row count after search: {len(rows)}")
        for row in rows[:5]:
            cols = row.find_elements(By.XPATH, "./td")
            if cols:
                print(f"  Row name: {cols[0].text}")

    def add_student(self):
        fake = Faker()

        student_name = fake.name()
        student_email = fake.email()
        registration_id = fake.random_number(digits=6)
        student_age = random.randint(a=18, b=30)

        add_student_button = self.wait.until(
            lambda d: d.find_element(*self.add_student_button)
        )
        add_student_button.click()

        name_input = self.wait.until(
            lambda d: d.find_element(*self.name_input)
        )
        name_input.send_keys(student_name)

        self.driver.find_element(*self.email_input).send_keys(student_email)

        self.driver.find_element(*self.department_dropdown_form).click()
        departments = self.wait.until(
            lambda d: d.find_elements("xpath", "//div//div[@role='option']")
        )
        random_department = random.choice(departments)
        department_name = random_department.text
        random_department.click()

        self.driver.find_element(*self.registration_input).send_keys(str(registration_id))
        self.driver.find_element(*self.age_input).send_keys(str(student_age))

        self.driver.find_element(*self.create_button).click()

        WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located(self.add_student_button)
        )

        return {
            "name": student_name,
            "email": student_email,
            "department": department_name,
            "registration_id": str(registration_id),
            "age": str(student_age)
        }

    def click_view_button_and_get_data(self):
        view_button = self.wait.until(
            lambda d: d.find_element(
                "xpath", "//button[.//*[contains(@class,'lucide-eye')]]"
            )
        )
        view_button.click()

        name = self.wait.until(
            lambda d: d.find_element(
                "xpath", "//span[text()='Name']/following-sibling::span"
            )
        ).text
        email = self.driver.find_element(
            "xpath", "//span[text()='Email']/following-sibling::span"
        ).text
        department = self.driver.find_element(
            "xpath", "//span[text()='Department']/following-sibling::span"
        ).text
        registration_id = self.driver.find_element(
            "xpath", "//span[text()='Registration ID']/following-sibling::span"
        ).text
        age = self.driver.find_element(
            "xpath", "//span[text()='Age']/following-sibling::span"
        ).text

        time.sleep(5)

        student_data = {
            "name": name,
            "email": email,
            "department": department,
            "registration_id": registration_id,
            "age": age
        }
        print(student_data)
        return student_data

    # -------------------------
    # Add Student Modal Methods
    # -------------------------

    def open_add_student_modal(self):
        btn = self.wait.until(EC.element_to_be_clickable(self.add_student_button))
        btn.click()
        self.wait.until(EC.visibility_of_element_located(self.create_button))

    def fill_student_form(self, name="", email="", select_department=False, reg_id="", age=""):
        if name:
            name_field = self.wait.until(EC.visibility_of_element_located(self.name_input))
            name_field.send_keys(name)

        if email:
            self.driver.find_element(*self.email_input).send_keys(email)

        if select_department:
            self.driver.find_element(*self.department_dropdown_form).click()
            departments = self.wait.until(
                lambda d: d.find_elements("xpath", "//div//div[@role='option']")
            )
            departments[0].click()

        if reg_id:
            self.driver.find_element(*self.registration_input).send_keys(reg_id)

        if age:
            self.driver.find_element(*self.age_input).send_keys(age)

    def click_create_button(self):
        self.driver.find_element(*self.create_button).click()
        time.sleep(1)

    def is_modal_still_open(self):
        try:
            WebDriverWait(self.driver, 3).until(
                EC.visibility_of_element_located(self.create_button)
            )
            return True
        except TimeoutException:
            return False

    # -------------------------
    # Edit Student Methods
    # -------------------------

    def click_edit_button(self):
        btn = self.wait.until(EC.element_to_be_clickable(self.edit_button))
        btn.click()
        self.wait.until(EC.visibility_of_element_located(self.update_button))

    def get_edit_modal_prefilled_name(self):
        name_field = self.wait.until(EC.visibility_of_element_located(self.edit_name_input))
        return name_field.get_attribute("value")

    def clear_and_update_name(self, new_name):
        name_field = self.wait.until(EC.visibility_of_element_located(self.edit_name_input))
        name_field.clear()
        name_field.send_keys(new_name)

    def clear_and_update_age(self, new_age):
        age_field = self.driver.find_element(*self.edit_age_input)
        age_field.clear()
        age_field.send_keys(str(new_age))

    def click_update_button(self):
        self.driver.find_element(*self.update_button).click()
        # Modal bondo hoye Add Student button visible hobe
        self.wait.until(EC.visibility_of_element_located(self.add_student_button))
        time.sleep(1)

    def is_update_modal_still_open(self):
        try:
            WebDriverWait(self.driver, 3).until(
                EC.visibility_of_element_located(self.update_button)
            )
            return True
        except TimeoutException:
            return False

    # -------------------------
    # Delete Student Methods
    # -------------------------

    def click_delete_button(self):
        btn = self.wait.until(EC.element_to_be_clickable(self.delete_button))
        btn.click()
        # Confirmation modal visible hobe
        self.wait.until(EC.visibility_of_element_located(self.confirm_delete_button))

    def confirm_delete(self):
        self.driver.find_element(*self.confirm_delete_button).click()
        # Modal bondo hoye table reload hobe
        self.wait.until(EC.visibility_of_element_located(self.add_student_button))
        time.sleep(1)

    def cancel_delete(self):
        self.driver.find_element(*self.cancel_button).click()
        time.sleep(1)

    def is_student_in_table(self, name):
        try:
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located(
                    (By.XPATH, f"//tbody/tr/td[text()='{name}']")
                )
            )
            return True
        except TimeoutException:
            return False