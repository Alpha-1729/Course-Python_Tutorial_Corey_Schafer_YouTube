#!/usr/bin/python3
# Sqlite Creating Database Table And Running Queries

"""
>>>> Sqlite is part of standard library. 
>>>> Cursor allows us to execute sql commands.
>>>> In memory database is good for testing purposes.
        Every time you will get a new fresh database.
>>>> Sqlite will also work with sqlalchemy.
        sqlalchemy is a popular ORM for python.
"""

import sqlite3
from employee import Employee


# Connection to in-memory database.
# conn = sqlite3.connect(":memory:")

conn = sqlite3.connect("employee.db")

c = conn.cursor()

# Create an employee table.
# c.execute(
#     """CREATE TABLE employees (
#           first TEXT,
#           last TEXT,
#           pay INTEGER
#           )"""
# )


def insert_emp(emp):
    with conn:
        c.execute(
            "INSERT INTO employees VALUES (:first, :last, :pay)",
            {"first": emp.first, "last": emp.last, "pay": emp.pay},
        )


def get_emps_by_name(lastname):
    c.execute("SELECT * FROM employees WHERE last=:last", {"last": lastname})
    return c.fetchall()


def update_pay(emp, pay):
    with conn:
        c.execute(
            """UPDATE employees SET pay=:pay WHERE first=:first AND last=:last""",
            {"first": emp.first, "last": emp.last, "pay": pay},
        )


def remove_emp(emp):
    with conn:
        c.execute(
            "DELETE FROM employees WHERE first=:first AND last=:last",
            {"first": emp.first, "last": emp.last},
        )


emp_1 = Employee("Jane", "Doe", 50000)
emp_2 = Employee("John", "Doe", 60000)

# Inserting data into table.
# c.execute("""INSERT INTO employees VALUES ('Corey', 'Schafer', 5000)""")
# c.execute("""INSERT INTO employees VALUES ('Mary', 'Schafer', 70000)""")

# Inserting values in the variable to database using string formatting.
# This is a bad practice and this is vulnerable to sql injection.
# c.execute("""INSERT INTO employees VALUES ('{}', '{}', {})""".format(emp_1.first, emp_1.last, emp_1.pay))

# Inserting values in the variable to database using DB API placeholder.
# Always put values in a tuple.
# c.execute("""INSERT INTO employees VALUES (?, ?, ?)""", (emp_1.first, emp_1.last, emp_1.pay))

# Inserting values in the variable to database using dictionary.
# c.execute(
#     """INSERT INTO employees VALUES (:first, :last, :pay)""",
#     {"first": emp_1.first, "last": emp_1.last, "pay": emp_1.pay},
# )

# conn.commit()

# Getting data from the table.
# c.execute("""SELECT * FROM employees WHERE last='Schafer'""")
# c.execute("""SELECT * FROM employees WHERE last=?""", ("Schafer",))
# c.execute("""SELECT * FROM employees WHERE last=:last""", {"last": "Schafer"})

# Getting only the next row from the table.
# Return None if no more rows.
# print(c.fetchone())

# Getting multiple rows from the table as list.
# Same like the limit statement in SQL.
# Return None if no more rows available.
# c.fetchmany(5)

# Getting all results as list.
# print(c.fetchall())

conn.close()
