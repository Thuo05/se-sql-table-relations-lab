# STEP 1A
# Import the SQLite library to connect to and work with an SQLite database.
import sqlite3

# Import Pandas to retrieve SQL query results and display them as DataFrames.
import pandas as pd


# STEP 1B
# Connect to the SQLite database named data.sqlite.
# If the file does not exist, SQLite will create a new database file.
conn = sqlite3.connect("data.sqlite")


# STEP 1
# Retrieve all columns and all rows from the employees table.
# pd.read_sql() executes the SQL query and stores the results in a DataFrame.
employee_data = pd.read_sql(
    "SELECT * FROM employees",
    conn
)

# Print a heading before displaying the employee data.
print("---------------------Employee Data---------------------")

# Display all the employee records retrieved from the database.
print(employee_data)

# Print a closing heading after displaying the employee data.
print("-------------------End Employee Data-------------------")


# STEP 2
# Select only the employee number and last name columns.
# The query retrieves all employees but displays only these two columns.
df_first_five = pd.read_sql(
    """
    SELECT employeeNumber, lastName
    FROM employees;
    """,
    conn
)

# Display the employee number and last name for each employee.
print("\nSTEP 2: Employee Number and Last Name")
print(df_first_five)


# STEP 3
# Retrieve the same columns as Step 2, but reverse their order.
# The last name appears before the employee number.
df_five_reverse = pd.read_sql(
    """
    SELECT lastName, employeeNumber
    FROM employees;
    """,
    conn
)

# Display the results with the last name as the first column.
print("\nSTEP 3: Reversed Column Order")
print(df_five_reverse)


# STEP 4
# Use the AS keyword to give employeeNumber a temporary column name: ID.
# This changes the displayed column name without modifying the database.
df_alias = pd.read_sql(
    """
    SELECT employeeNumber AS ID, lastName
    FROM employees;
    """,
    conn
)

# Display the employee ID and last name.
print("\nSTEP 4: Employee ID and Last Name")
print(df_alias)


# STEP 5
# Use the CASE statement to categorize employees according to their job titles.
# Employees with the specified senior job titles are classified as Executives.
# All other employees are classified as Not Executive.
# The AS keyword names the new calculated column role.
df_executive = pd.read_sql(
    """
    SELECT
        employeeNumber,
        lastName,
        jobTitle,
        CASE
            WHEN jobTitle = 'President'
              OR jobTitle = 'VP Sales'
              OR jobTitle = 'VP Marketing'
            THEN 'Executive'
            ELSE 'Not Executive'
        END AS role
    FROM employees;
    """,
    conn
)

# Display employee details together with their assigned roles.
print("\nSTEP 5: Employee Roles")
print(df_executive)


# STEP 6
# Use the LENGTH() function to calculate the number of characters
# in each employee's last name.
# AS name_length gives the calculated column a readable name.
df_name_length = pd.read_sql(
    """
    SELECT LENGTH(lastName) AS name_length
    FROM employees;
    """,
    conn
)

# Display the length of each employee's last name.
print("\nSTEP 6: Last Name Length")
print(df_name_length)


# STEP 7
# Use SUBSTR() to extract the first two characters of each job title.
# The number 1 indicates the starting position.
# The number 2 indicates how many characters to extract.
df_short_title = pd.read_sql(
    """
    SELECT SUBSTR(jobTitle, 1, 2) AS short_title
    FROM employees;
    """,
    conn
)

# Display the first two characters of each job title.
print("\nSTEP 7: Short Job Titles")
print(df_short_title)


# STEP 8
# Multiply priceEach by quantityOrdered to calculate the value
# of each order-detail record.
# ROUND() rounds each calculated value to the nearest whole number.
# pd.read_sql() retrieves the calculated values as a DataFrame.
sum_total_price = pd.read_sql(
    """
    SELECT ROUND(priceEach * quantityOrdered) AS total_price
    FROM orderDetails;
    """,
    conn
).sum().reset_index(drop=True)

# Display the sum of the rounded order-detail values.
print("\nSTEP 8: Total Order Amount")
print(sum_total_price)


# STEP 9
# Retrieve each order date and extract its day, month, and year.
# STRFTIME('%d', orderDate) extracts the day.
# STRFTIME('%m', orderDate) extracts the month.
# STRFTIME('%Y', orderDate) extracts the year.
df_day_month_year = pd.read_sql(
    """
    SELECT
        orderDate,
        STRFTIME('%d', orderDate) AS day,
        STRFTIME('%m', orderDate) AS month,
        STRFTIME('%Y', orderDate) AS year
    FROM orders;
    """,
    conn
)

# Display the original order date and its separate date components.
print("\nSTEP 9: Order Dates")
print(df_day_month_year)


# STEP 10
# Close the database connection after completing all the queries.
# This releases the database resources used by the program.
conn.close()
