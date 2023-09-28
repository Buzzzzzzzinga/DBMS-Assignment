# DBMS-Assignment

```markdown
# Employee Database Management System

This Python script is a simple Employee Database Management System (DBMS) with a graphical user interface (GUI) built using the Tkinter library. It allows users to interact with an SQLite database to perform basic CRUD (Create, Read, Update, Delete) operations on employee records.

## Features

- **Database Connectivity**: The script connects to an SQLite database named "employee.sqlite" and initializes a cursor for executing SQL queries.

- **Table Checks and Creation**: It checks if the required database tables exist (Departments, Location, Employee, Education). If not, it creates these tables.

- **Delete Employee Information**: Users can delete employee records by providing an Employee ID. If the ID exists in the database, the corresponding records are deleted from the "Employee" and "Education" tables.

- **Update Employee Information**: Users can update employee information by specifying an Employee ID. They can modify attributes such as name, age, salary, department, location, education level, and year of passing.

- **Insert Employee Information**: New employee information can be added by entering details such as Employee ID, name, age, salary, department, location, education level, and year of passing. The script performs validation to prevent duplicate Employee IDs.

- **Display Employee Information**: Users can retrieve and display employee details by providing an Employee ID. The script displays information including ID, name, age, salary, department, location, education level, and year of passing.
```
## Getting Started

1. Clone the repository to your local machine:

   ```shell
   git clone https://github.com/Buzzzzzzzinga/DBMS-Assignment.git
   ```

2. Navigate to the project directory:

   ```shell
   cd employee-dbms
   ```

3. Run the script:

   ```shell
   python employee_dbms.py
   ```

4. The GUI application will open, allowing you to interact with the employee database.

## Dependencies

- Python (>= 3.6)
- Tkinter (Python's standard GUI library)
- SQLite (included with Python)

## Usage

1. Click the "Delete" button to open a window for deleting employee records by providing an Employee ID.

2. Click the "Update" button to open a window for updating employee records by providing an Employee ID and modifying details.

3. Click the "Insert" button to open a window for inserting new employee records by entering details.

4. Click the "Select" button to open a window for retrieving and displaying employee details by providing an Employee ID.

