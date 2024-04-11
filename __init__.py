# Import modules to make them available when the package is imported
from . import employee_operations
from . import file_operations
from . import menu
from . import report_generation

# Define the list of modules to be imported when the package is imported
__all__ = ['employee_operations', 'file_operations', 'menu', 'report_generation']
