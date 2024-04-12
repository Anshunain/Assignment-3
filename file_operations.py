"""
File Operations Module

This module provides functions for reading from and writing to the text file
that stores employee data.
"""
def read_employees():
# Function to load employee data from the file
def load_employee_data():
    try:
        with open('employees.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Function to save employee data to the file
def save_employee_data(data):
    with open('employees.json', 'w') as file:
        json.dump(data, file, indent=4)

# Function to add a new employee
def add_employee():
    employees = load_employee_data()
    employee = {}
    employee['id'] = input("Enter employee ID: ")
    employee['first_name'] = input("Enter employee ID first name: ")
    employee['last_name'] = input("Enter employee ID last name: ")
    employee['date_of_birth'] = input("Enter employee's date of birth (YYY-MM-DD):")
    employee['department'] = input("Enter employee's department: ")
    employee['salary'] = float(input("Enter employee's salary: "))
    employees.append(employee)
    save_employee_data(employees)
    print("Employee added successfully:")

# Function to delete an existing employee
def delete_employee():
    employees = load_employee_data()
    employee_id = input("Enter the ID of the employee to delete: ")
    employees = [employee for employee in employees if employee['id'] != employee_id]
    save_employee_data(employees)
    print("Employee deleted successfully.")

    
    """
    Read Employees Function

    This function reads employee data from the text file and returns it.

    Returns:
        list: A list containing employee data read from the text file.
    """


def write_employees():
def update_employee():
    employees = load_employee_data()
    employee_id = input("Enter the ID of the employee to update: ")
    for employee in employees:
        if employee['id'] == employee_id:
            employee['first_name'] = input("Enter updated first name: ")
            employee['last_name'] = input("Enter updated last name: ")
            employee['date_of_birth'] = input("Enter updated date of birth (YYYY-MM-DD): ")
            employee['department'] = input("Enter updated department: ")
            employee['salary'] = float(input("Enter updated salary: "))
            break
    else:
        print("Employee not found.")
        return
    save_employee_data(employees)
    print("Employee details updated successfully.")

# Function to generate a report: List of all employees
def list_employees():
    employees = load_employee_data()
    print("List of all employees:")
    for employee in employees:
        print(f"ID: {employee['id']}, Name: {employee['first_name']} {employee['last_name']}, Department: {employee['department']}")

# Function to generate a report: List of departments
def list_departments():
    employees = load_employee_data()
    departments = set(employee['department'] for employee in employees)
    print("List of departments:")
    for department in departments:
        print(department)

# Main function to run the application
def main():
    while True:
        print("\nEmployee Management System")
        print("1. Add Employee")
        print("2. Delete Employee")
        print("3. Update Employee Details")
        print("4. List Employees")
        print("5. List Departments")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            add_employee()
        elif choice == '2':
            delete_employee()
        elif choice == '3':
            update_employee()
        elif choice == '4':
            list_employees()
        elif choice == '5':
            list_departments()
        elif choice == '6':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if 'name'== "main":
    main()
    
    """
    Write Employees Function

    This function writes employee data to the text file.

    Parameters:
        employees_data (list): A list containing employee data to be written to the text file.
    """
