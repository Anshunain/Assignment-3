
"""
Report Generation Module

This module provides a function for generating reports based on employee data.
"""

def generate_reports():
    
#Generate Reports Function
    #This function generates various reports based on employee data, such as:
    - List of position
    - List of all employees with ID, full name, and position
    - List of all position with the average age and salary of employees
    - List of employees in each position with ID, full name, date of birth, salary,
      and total salary for employees position
    """
position = get_position()
employees = get_employees()

    print("List of position: ")
    for position:
        print(position)

    print("\nList of position: ")
    for employee in employees:
        print(f"ID: {employee['id']}, Name: {employee['name']}, position: {employee['position']}")

    print("\nList of position with Average Age and Salary:")
    for employee in position:
        avg_age, avg_salary = calculate_position_stats(employees, position)
        print(f"employee: {position}, Average Age: {avg_age}, Average Salary: {avg_salary}")

    print("\nEmployees in Each position:")
    for employees in position:
        print(f"\nposition: {employee}")
        position_employees = [employee for employee in employees if employee['position'] == position]
        total_salary = sum(employee['salary'] for employee in position_employees)
        for employee in position_employees:
            print(
                f"ID: {employee['id']}, Name: {employee['name']}, Date of Birth: {employee['dob']}, Salary: {employee['salary']}, Total Salary for position: {total_salary}")


def get_position():
    return ["Analyst", "Engineer", "Manager"]


def get_employees():
    return [
        {"id": 1, "name": "Pusker", "position": "Manager", "dob": "1980-05-15", "salary": 160000},
        {"id": 2, "name": "Anshu", "position": "Engineer", "dob": "1975-12-20", "salary": 90000},
        {"id": 3, "name": "Anshil", "position": "Analyst", "dob": "1990-08-10", "salary": 75000},
    ]


def calculate_department_stats(employees, department):
    department_employees = [employee for employee in employees if employee['department'] == department]
    if len(department_employees) == 0:
        return 0, 0
    avg_age = sum(get_age(employee['dob']) for employee in department_employees) / len(department_employees)
    avg_salary = sum(employee['salary'] for employee in department_employees) / len(department_employees)
    return avg_age, avg_salary


def get_age(date_of_birth):
    import datetime
    today = datetime.date.today()
    dob = datetime.datetime.strptime(date_of_birth, "%Y-%m-%d").date()
    age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
    return age

    """
