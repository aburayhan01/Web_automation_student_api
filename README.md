# Web Automation — Student Management System

[![Python Version](https://img.shields.io/badge/Python-3.9%2B-1E90FF?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Framework](https://img.shields.io/badge/Framework-Pytest-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white)](https://docs.pytest.org/)
[![Automation](https://img.shields.io/badge/Selenium-Web%20Automation-43B02A?style=for-the-badge&logo=selenium&logoColor=white)](https://www.selenium.dev/)
[![Reporting](https://img.shields.io/badge/Allure-Report-E40046?style=for-the-badge&logo=testinglibrary&logoColor=white)](https://docs.qameta.io/allure/)
[![Automation Level](https://img.shields.io/badge/Test%20Automation-Advanced-2ECC71?style=for-the-badge)]()

## Project Overview

This project demonstrates UI automation testing for a Student Management System using Selenium WebDriver and Pytest.
The framework covers full CRUD operations (Create, Read, Update, Delete) along with login and filter functionalities.
Page Object Model (POM) design pattern is followed for better maintainability and reusability.
Both pytest-html and Allure are used for test reporting.

---

## Tools & Technologies

- Python
- Pytest
- Selenium WebDriver
- WebDriver Manager
- python-dotenv
- Faker
- pytest-html
- Allure
- GitHub

---

## 📂 Project Structure

```text
Web_Automation/
│
├── pages/                        # Page Object Model layer
│   ├── login_page.py             # Login page locators & actions
│   └── student_page.py          # Student page locators & actions
│
├── testcases/                    # Test scripts
│   ├── test_login.py
│   ├── test_filter.py
│   ├── test_create_student.py
│   ├── test_update_student.py
│   └── test_delete_student.py
│
├── .env                          # Sensitive credentials (not committed)
├── .gitignore                    # Ignored files list
├── conftest.py                   # Fixtures & global setup
├── requirements.txt              # Project dependencies
└── README.md
```

---

## How to Run the Project

### 1. Clone the Repository

```bash
git clone https://github.com/aburayhan01/Web_automation_student_api.git
cd Web_automation_student_api
```

### 2. Create and Activate Virtual Environment

Windows:
```bash
python -m venv .venv
.venv\Scripts\activate
```
macOS / Linux:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up Environment File

Create a `.env` file in the project root:
```
BASE_URL=https://your-site-url.com
SITE_USERNAME=your_username
SITE_PASSWORD=your_password
```
> Note: Never commit `.env` to GitHub. It is listed in `.gitignore`.

### 5. Run All Tests

```bash
pytest testcases/
```

### 6. Run a Specific Test File

```bash
pytest testcases/test_login.py
```

### 7. Run a Specific Test Function

```bash
pytest testcases/test_delete_student.py::test_delete_student
```

---

## Generate & View HTML Report

```bash
pytest testcases/ --html=reports/report.html --self-contained-html
```

To view on Windows:
```bash
start reports/report.html
```
To view on macOS:
```bash
open reports/report.html
```

<img width="1918" height="933" alt="Screenshot 2026-06-13 110917" src="https://github.com/user-attachments/assets/c8f2bfef-88d4-4b12-82ba-48e642b7ce61" />


---

## Generate & View Allure Report

### Generate Allure Results:
```bash
pytest testcases/ --alluredir=reports/allure-results
```

### View Allure Report:
```bash
allure serve reports/allure-results
```

## Allure Test Report Dashboard

### 📌 Executive Overview (Allure Summary)

<img width="1918" height="863" alt="Screenshot 2026-06-13 111944" src="https://github.com/user-attachments/assets/c8b373f0-d07f-417d-ad89-95636ba5748c" />


---

### Test Execution Trends & Graphical Analysis

<img width="1906" height="1073" alt="Screenshot 2026-06-13 112402" src="https://github.com/user-attachments/assets/7c46ef26-e805-4316-b056-7a53a13f42d3" />


---

### Test Suite & Category Breakdown

<img width="1245" height="946" alt="Screenshot 2026-06-13 112046" src="https://github.com/user-attachments/assets/d9d6fdd3-7a24-49b9-b706-b262b2a22135" />


---

## Test Cases

### Login
- Login with valid credentials → SMS Panel visible
- Login with wrong password → Login fails
- Login with empty credentials → Login fails

### Filter
- Filter students by department → All rows match selected department
- Search student by name → Matching results returned

### Create Student
- Create student with valid data → Student added & info verified
- Create with empty form → Form does not submit
- Create with invalid email → Form does not submit
- Create with duplicate email → Form does not submit

### Update Student
- Update student name & age → Updated data visible in table
- Update with empty name → Form does not submit

### Delete Student
- Delete student → Student removed from table
- Delete student and verify gone → Confirmed before & after deletion

---

## Test Coverage Summary

| File | Tests | Result |
|------|-------|--------|
| test_login.py | 3 | ✅ Passed |
| test_filter.py | 2 | ✅ Passed |
| test_create_student.py | 4 | ✅ Passed |
| test_update_student.py | 2 | ✅ Passed |
| test_delete_student.py | 2 | ✅ Passed |

**Total: 13 test cases — All Passed ✅**

---

## Author

Abu Rayhan
GitHub: https://github.com/aburayhan01/Web_automation_student_api
