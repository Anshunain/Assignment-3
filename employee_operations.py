ter"""
Employee Operations Module

This module provides functions for adding, deleting, and updating employee information.
"""

def add_employee():
ID = int(input("please enter the ID for the new employee: "))
    firstName = input("employee's firstname ")
    last_name = input("employee's lastname ")
    date_of_birth = input("employee's date of birth in (YYYY/MM/DD) ")
    start_of_year = int(input("employee's starting year "))
    position = input("employee's position")
    salary = float(input("employee's salary "))

    """
    Add Employee Function

    This function prompts the user to input details for a new employee and adds the employee
    to the system.

    """

def delete_employee():
    """
    Delete Employee Function

    This function prompts the user to input the ID of the employee to be deleted and
    removes the employee from the system.

    """

def update_employee():
    ID = int(input("ID of employee to be updated "))
    for employee in employees:
        if employee.id == id:
            firsr_name = input("new first name of thhe employee ")
            last_name = input("new last name of the employee ")
            date_of_birth = input("new date_of_birth of the employ (YYYY/MM/DD) ")
            start_of_year = int(input(new start year of employee ")
            position = input("enter new position of the employees ")
            salary = float(input("new salary of the employee ")
                           
            employee.first_name = first_name
            employee.last_name = last_name
            employee.date_of_birth = date_of_birth
            employee.salary = salary
            employee.position = position

            print(f"employee with ID {ID}update ")
            return
            print(f"No employee with ID{id}found in the system ")
    """
    Update Employee Function

    This function prompts the user to input the ID of the employee to be updated and
    allows the user to modify the employee's information such as name, department, or salary.

    """
