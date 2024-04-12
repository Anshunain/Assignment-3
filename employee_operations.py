ter"""
Employee Operations Module

This module provides functions for adding, deleting, and updating employee information.
"""

def add_employee():
ID = int(input("please enter the ID for the new employee: "))
    first_Name = input("first name of employees ")
    last_name = input("last name of the employees ")
    date_of_birth = input("date of birth of employees in (YYYY/MM/DD) ")
    start_of_year = int(input("employee's starting year "))
    position_hold = input("employee's hold position")
    salary = float(input("employee's salary "))
            
    """
    Add Employee Function
    def add(employee detail)
    return ("first_Name, last_name, date_of_birth, position_hold, salary")

    # This function prompts the user to input details for a new employee and adds the employee
    to the system.

    """

def delete_employee():
ID = int(input("ID for delete the employees: ")
         First_name = Input("first name of the employees: ")
         last_name =   Input("last name of the employees: ")  
         date_of_birth = input("date of birth of employees in (YYYY/MM/DD) ")
         start_of_year = int(input("employee's starting year "))
         position_hold = input("employee's hold position")
         salary = float(input("employee's salary "))
    
    """
    Delete Employee Function
    def delete(employee details)
    return none

    This function prompts the user to input the ID of the employee to be deleted and
    removes the employee from the system.

    """

def update_employee():
    ID = int(input("ID of employee to be updated "))
    for employee in employees:
        if employee.id == id:
            first_name = input("name of the employee ")
            last_name = input("new last name of the employee ")
            date_of_birth = input("new date_of_birth of the employ (YYYY/MM/DD) ")
            start_of_year = int(input(new start year of employee ")
            position_update = input("enter new position updated of the employees ")
            salary = float(input("new salary of the employee ")

            print(f"employee with ID {ID}update ")
            return
            print(f"No employee with ID{id}found in the system ")
    """
    Update Employee Function

    This function prompts the user to input the ID of the employee to be updated and
    allows the user to modify the employee's information such as name, department, or salary.

    """
