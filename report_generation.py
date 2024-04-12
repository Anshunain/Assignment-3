
"""
Report Generation Module

This module provides a function for generating reports based on employee data.
"""

def generate_reports():
    
#Generate Reports Function
    #This function generates various reports based on employee data, such as:
    - List of position
    - List of employees with ID, full name, and position
    - List of position with the average age and salary of employees
    - List of employees in position with ID, full name, date of birth, salary,
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
        avg_age, avg_salary = calculate_position_status(employees, position)
        print(f"employee: {position}, Average Age: {avg_age}, Average Salary: {avg_salary}")

    print("\nEmployees in Each position:")
    for employees in position:
        print(f"\nposition: {employee}")
        position_employees = [employee for employee in employees if employee['position'] == position]
        total_salary = sum(employee['salary'] for employee in position_employees)
        for employee in position_employees:
            print(
                f"ID: {employee['id']}, Name: {employee['name']}, Date of Birth: {employee['date of birth']}, Salary: {employee['salary']}, Total Salary for position: {total_salary}")


def get_position():
position1 = input("Manager")
position2 = input("Engineer")
position3 = input("Analyst")

if get:
return ["Analyst", "Engineer", "Manager"]
elif:
return error

def calculate_position_status(employees, position):
    position_employees = [employee for employee in employees if employee['position'] == position]
    if len(department_employees) == 0:
        return 0, 0
    avg_age = sum(get_age(employee['dob']) for employee in position_employees) / len(position_employees)
    avg_salary = sum(employee['salary'] for employee in position_employees) / len(position_employees)
    return avg_age, avg_salary


def get_age(date_of_birth):
    import datetime
    today = datetime.date.today()
    dob = datetime.datetime.strptime(date_of_birth, "Y-m-d").date()
    age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
    return age
    
def get_employees():
    return [
        {"id": 1, "name": "Komal", "position": "Manager", "dob": "1980-05-15", "salary": 160000},
        {"id": 2, "name": "Anshu", "position": "Engineer", "dob": "1975-12-20", "salary": 90000},
        {"id": 3, "name": "Manpreet", "position": "Analyst", "dob": "1990-08-10", "salary": 75000},
    ]
    
    """
